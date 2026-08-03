## **Incoming Email Workflow**
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
***

## **Deadline tracking workflow**
1. Email arrives through Caspian.
2. LLM scans through email to find a due_date and task.
3. The due-date, task & email in database according to closest remind_date
4. remind_date = due_date - 2 days
5. when remind_date is reached:
    - change the task to urgent 
    - send telegram a reminder
    - keep original email linked to task 

***

## **Telegram workflow**

***summary <span style ="color:green">`<id>`</span>***
    Returns concise AI-summary of a particular email.

***from <span style ="color:green">`<id>`</span>***
    Returns the sender's email & name 

***full <span style ="color:green">`<id>`</span>***
    Returns the full stored email body & subject

***draft <span style ="color:green">`<id>`</span>***
    Generates a professional draft email 

***refine <span style ="color:green">`<id>`</span> <span style ="color:yellow">`<feedback>`</span>***
    Improves the draft generated

***approve <span style ="color:green">`<id>`</span>***
    Sends the generated drafted email

***compose***
    Start a brand new manual-email workflow. Allowing you send subject,body & receivers email address. 

