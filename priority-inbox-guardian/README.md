# Priority Inbox Guardian

**Built for the Caspian Buildathon 2026**

An AI-powered **multi-channel inbox assistant** that turns your email inbox into a proactive task and communication system.

Instead of only notifying you when an email arrives, the agent can also **remember future obligations**, track deadlines, escalate them when they become urgent, and let you manage email replies directly from **Telegram**.

---

## The Problem

Important emails are often forgotten because they are not urgent **when they arrive**. Examples include:

* paying rent before a deadline,
* cancelling a subscription before renewal,
* submitting university forms,
* confirming interviews,
* paying invoices before late fees apply.

Most inbox assistants summarize emails, but they do not **remember to remind you later**.

---

## The Solution

Priority Inbox Guardian combines **Caspian**, **Featherless.ai**, **persistent memory**, and **Telegram** to create a deadline-aware communication agent.

### Core Features

* **Email ingestion through Caspian**
* **Duplicate detection using `message_id`**
* **AI classification with Featherless.ai**
* **Automatic one-sentence summaries**
* **Future deadline extraction**
* **Persistent deadline tracking**
* **Proactive Telegram reminders**
* **AI-assisted reply drafting**
* **Manual email composition from Telegram**
* **Human approval before sending outbound emails**

---

## Channels

| Channel      | Purpose                                                               |
| ------------ | --------------------------------------------------------------------- |
| **Email**    | Receive incoming emails and send approved replies                     |
| **Telegram** | Receive alerts, inspect emails, manage deadlines, and compose replies |

This satisfies the hackathon requirement of **one agent operating across multiple channels through a single handler**.

---

## High-Level Workflow

The following diagram shows the complete message flow between **Gmail**, **Caspian**, the **Python agent**, **Featherless.ai**, the **Email/Deadline databases**, and the **Telegram command center**.

![Priority Inbox Guardian Architecture](diagrams/architectural_design.png)

---

## AI Classification Output

For each new email, the LLM returns:

```json
{
  "urgency": "urgent",
  "summary": "Confirm interview attendance by 5 PM today.",
  "due_date": "2026-08-15",
  "category_tag": "interview",
  "future_task": "Confirm interview attendance"
}
```

---

## Deadline Tracking

If a future obligation is detected, the agent creates a reminder task:

```text
due_date   = 2026-09-15
remind_at  = due_date - 2 days
```

When the reminder date is reached, the task is automatically escalated to **urgent** and a Telegram reminder is sent.

---

## Telegram Commands

| Command                  | Description                             |
| ------------------------ | --------------------------------------- |
| `summary <id>`           | AI-generated summary                    |
| `from <id>`              | Show sender information                 |
| `full <id>`              | Show full email subject and body        |
| `draft <id>`             | Generate a professional reply draft     |
| `refine <id> <feedback>` | Improve a generated draft               |
| `approve <id>`           | Send the approved draft through Caspian |
| `compose`                | Start a brand-new manual email workflow |
| `deadlines`              | List upcoming tracked deadlines         |

---

## Database Design

The project uses three logical tables:

* **Email Table** — stores processed emails and AI metadata
* **Deadline Table** — stores future obligations and reminder schedules
* **Draft Table** — stores AI-generated and manually composed email drafts

See [`docs/database-schema.md`](docs/database-schema.md) for the full schema.

---

## Tech Stack

* **Python**
* **Caspian SDK**
* **Featherless.ai** (LLM inference)
* **Telegram Bot API**
* **SQLite** (persistent memory)
* **GitHub** (version control and documentation)

---

## Project Status

### Planning

* [x] Problem definition
* [x] Workflow specification
* [x] Database schema design
* [x] System architecture diagram

### Implementation

* [ ] Caspian email integration
* [ ] Telegram bot integration
* [ ] SQLite persistence layer
* [ ] Featherless LLM integration
* [ ] Deadline reminder scheduler
* [ ] AI draft and refinement workflow
* [ ] Manual compose and send workflow

---

## Repository Structure

```text
priority-inbox-guardian/
├── README.md
├── PROJECT.md
├── docs/
│   ├── workflow.md
│   ├── database-schema.md
│   ├── telegram-commands.md
│   └── roadmap.md
└── diagrams/
```

---

## Setup

Setup instructions will be added as the implementation progresses during the hackathon window.

The final version will include:

1. Python virtual environment setup
2. Dependency installation
3. Caspian configuration
4. Telegram bot configuration
5. Featherless API key configuration
6. Database initialization
7. Agent startup instructions

---

## Why This Project Is Different

Most email assistants are **reactive**:

```text
Email arrives → Notify user
```

This project is **proactive**:

```text
Email arrives
      ↓
AI extracts future obligation
      ↓
Task is remembered for days or weeks
      ↓
Agent reminds the user when the deadline becomes important
```

The goal is to build an agent that does not just **understand communication**, but also **remembers commitments and helps prevent missed deadlines**.

---

## Hackathon Compliance

* **Uses `caspian-sdk`**
* **Runs across Email and Telegram**
* **Single Python agent / single handler architecture**
* **Public GitHub repository**
* **Original project developed during the hackathon window**

---

## Author

**Johnson Nyabicha**

University of Exeter — BSc Computer Science with Industrial Placement

