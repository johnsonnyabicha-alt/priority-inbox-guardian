# Database Schema

## Email Table

| Field          | Purpose                                                  |
| -------------- | -------------------------------------------------------- |
| `email_id`     | Unique email identifier                                  |
| `message_id`   | Original Caspian/Gmail message identifier                |
| `sender_name`  | Display name of the sender                               |
| `sender_email` | Original sender email address                            |
| `subject`      | Email subject                                            |
| `body`         | Full email body                                          |
| `summary`      | AI-generated one-sentence summary                        |
| `tag`          | `interview`, `finance`, `subscription`, `academic`, etc. |
| `urgency`      | `urgent`, `action`, `info`, `ignore`                     |
| `status`       | `classified`, `notified`, `replied`, `archived`          |
| `received_at`  | Timestamp when the email was received                    |
| `processed_at` | Timestamp when the email was processed by the agent      |

---

## Deadline Table

| Field              | Purpose                                         |
| ------------------ | ----------------------------------------------- |
| `task_id`          | Unique task identifier                          |
| `email_id`         | Link to the original email                      |
| `task_description` | What must be done                               |
| `due_date`         | Deadline extracted from the email               |
| `remind_at`        | Date when the reminder should be triggered      |
| `current_tag`      | `future_action` or `urgent`                     |
| `status`           | `pending`, `reminded`, `completed`, `cancelled` |
| `created_at`       | Timestamp when the task was created             |
| `reminded_at`      | Timestamp when the reminder was sent            |

---

## Draft Table

| Field             | Purpose                                    |
| ----------------- | ------------------------------------------ |
| `draft_id`        | Unique draft identifier                    |
| `email_id`        | Linked email (`NULL` for manual compose)   |
| `recipient_email` | Destination email address                  |
| `subject`         | Email subject                              |
| `body`            | Draft content                              |
| `version`         | Revision number for refinements            |
| `approval_status` | `pending`, `approved`, `sent`, `cancelled` |
| `created_at`      | Timestamp when the draft was created       |
| `updated_at`      | Timestamp when the draft was last modified |

---

## Relationship Overview

```text
Email Table
    │
    ├── 1 → many → Deadline Table
    │
    └── 1 → many → Draft Table
```

This allows a single email to:

* generate multiple future reminder tasks,
* have multiple draft revisions,
* maintain a complete history of notifications and responses.
