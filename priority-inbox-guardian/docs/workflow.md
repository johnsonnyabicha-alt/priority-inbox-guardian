**Incoming Email Workflow**
1. Email arrives through Caspian.
2. The email is tracked through a message_id.
3. Check whether the email has been tracked before
4. If it has been tracked before don't do anything to the email
5. Otherwise introduce the LLM(featherless.ai) to analyze the body and subject.
6. The LLM should return:
    - urgency 
    - one-sentence summary 
    - due-date 
    - category-tag 
7. Store the email in the database including the message_id and due_date most importantly.
8. If the email is urgent notify the user on Telegram through Caspian. 
9. If a future deadline is detected, create a reminder task. 