from memory.deadline_repository import list_upcoming_deadlines

# Service function: reads deadlines and decides what to do with them
def check_reminders():
    # Get all pending deadlines from the repository
    deadlines = list_upcoming_deadlines()

    # Handle the case where there are no reminders
    if not deadlines:
        print("No pending reminders.")
        return

    # Process each deadline returned from the database
    for task_id, description, due_date, remind_at in deadlines:
        print(f"Reminder: {description} is due on {due_date}")
        print(f"  Task ID: {task_id}")
        print(f"  Remind on: {remind_at}")
        print()

# Run the service wi
if __name__ == '__main__':
    check_reminders()