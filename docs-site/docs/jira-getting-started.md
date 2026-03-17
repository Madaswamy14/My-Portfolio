---
title: Jira Getting Started
description: Jira documentation structured by topic type — concept overview, task workflow, reference, and common mistakes.
---

# Jira Getting Started Guide

---

## Concept: Jira Overview

### What is Jira?

Jira is a work tracking system used by software teams to plan, track, and deliver work.

It connects:

- Requirements (what to build)
- Work items (tasks, stories, bugs)
- Development (code changes)
- Delivery (completed features)

---

### Why Jira Matters

Jira acts as a single source of truth for:

- Who is working on what
- Current progress of tasks
- Status of features in development

When used correctly, it improves team visibility, collaboration, and delivery speed.

---

### Key Idea

Jira is not just a task list. It is a communication system for work across a team.

---

## Task: Complete Your First Jira Workflow

### Goal

Pick up a task, complete it, and move it through the workflow correctly.

---

### Prerequisites

- Access to a Jira project
- Assigned task or access to sprint board
- Basic understanding of development workflow

---

#### 1. Open Your Board

Navigate to:

- Scrum Board — for sprint teams
- Kanban Board — for continuous workflow

#### 2. Find Your Task

Locate work using **Assigned to me** or the current sprint.

#### 3. Review the Task

Check the description, acceptance criteria, and dependencies. If unclear, comment and ask for clarification before starting.

#### 4. Start Work

Move the task to **In Progress**. This indicates ownership and tells others not to pick it up.

#### 5. Implement and Link Code

1. Create a branch using the ticket ID — example: `feature/JIRA-123-login-api`
2. Open a Pull Request (PR)
3. Link the PR to the Jira ticket

#### 6. Request Review

Move the task to **Code Review**.

#### 7. Complete the Task

Move the task to **Done** only after:

- Code is merged
- Review is approved
- Acceptance criteria are met

---

### Result

Your task is fully tracked from **assignment → development → completion**.

---

## Reference: Core Jira Concepts

### Issue Types

| Type | Description |
| --- | --- |
| **Epic** | Large feature spanning multiple tasks |
| **Story** | User-level requirement |
| **Task** | Technical work |
| **Bug** | Defect or issue in existing functionality |

> In Jira, all of the above are technically referred to as **Issues**.

---

### Workflow States

```
Backlog → To Do → In Progress → Code Review → Done
```

---

### Acceptance Criteria

Defines what must be true for a task to be considered complete and how success is measured.

---

### Sprint

A fixed time period (typically two weeks) where a team completes planned work.

---

### Backlog

A prioritized list of upcoming tasks waiting to be assigned to a sprint.

---

## Reference: Common Mistakes

| Category | Mistake | Why It Matters |
| --- | --- | --- |
| Workflow | Moving task to Done before code is merged | Creates false visibility |
| Workflow | Not updating task status | Team loses visibility |
| Communication | Not commenting when blocked | Leaves task idle without context |
| Communication | Not asking for clarification | Code may miss requirements |
| Process | Ignoring acceptance criteria | Work may not match what was requested |
| Process | Working on unassigned tasks | Causes duplication and confusion |
| Process | Not linking PR to Jira | Breaks traceability between code and tasks |

These mistakes reduce visibility, team coordination, and delivery speed.

---

## Reference: Real-World Scenarios

### Blocked Task

If work is blocked:

1. Add a comment explaining the blocker
2. Tag the relevant teammate
3. Do not leave the task idle without context

### Reopened Task

If issues are found after completion, the task moves back to **In Progress**. Fix the issues and repeat the workflow.

### Changing Requirements

If requirements change, update the ticket and align with the team before continuing work.