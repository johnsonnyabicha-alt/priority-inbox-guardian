import os

from dotenv import load_dotenv
from caspian_sdk import CommClient

from agent.orchestrator import (
    process_incoming_email,
    telegram_command,
)


load_dotenv()

print(
    "Caspian key loaded:",
    os.getenv("CASPIAN_API_KEY") is not None,
)

client = CommClient()

email = client.connect_email(username="priorityguardian")
print("Agent email:", email["address"])

client.connect_telegram(
    bot_token=os.getenv("TELEGRAM_BOT_TOKEN")
)


@client.on_message
def handle(message):
    """
    One shared handler for all Caspian channels.
    """

    # Email messages have a subject attribute
    if getattr(message, "subject",None):
        print("=== NEW EMAIL ===")
        print(message.sender)
        print(type(message.sender))

        sender = message.sender

        # Caspian supplies the sender as a dictionary.
        if isinstance(sender, dict):
            sender_name = sender.get("name", "Unknown")
            sender_email = sender.get("address", "")
        else:
            sender_name = str(sender)
            sender_email = str(sender)

        email_event = {
            "message_id": message.id,
            "sender_name": sender_name,
            "sender_email": sender_email,
            "subject": message.subject,
            "body": message.text,
        }

        result = process_incoming_email(email_event)
        print("Processing result:", result)

        # Do not send another reply for a duplicate delivery.
        if result.get("reason") == "duplicate email":
            print("Duplicate ignored; no second reply sent.")
            return

        if result.get("stored"):
            message.reply(
                "Email processed successfully.\n"
                f"Summary: {result.get('summary', 'No summary available.')}"
            )
        else:
            message.reply(
                "Email could not be processed.\n"
                f"Reason: {result.get('reason', 'unknown error')}"
            )

        return

    # Telegram text commands
    reply = telegram_command(message.text)
    message.reply(reply)


if __name__ == "__main__":
    print("Listening for email and Telegram messages...")
    client.listen()