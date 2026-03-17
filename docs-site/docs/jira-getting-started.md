---
title: Jira Getting Started
description: Get productive with Jira as a developer on a real team — find your work, manage the workflow, and collaborate effectively.
---

# Jira Getting Started Guide (Developer Workflow)

## Overview

This guide helps you get productive with Jira as a **developer on a real team**.

By the end, you'll be able to:

- Find and understand your assigned work
- Move tasks through the workflow correctly
- Collaborate with your team using Jira

---

## Who This Is For

- Software Developers (Frontend / Backend)
- QA Engineers
- New team members onboarding to Jira

---

## Mental Model: How Jira Works

Jira is a **work tracking system** used to manage software development.

### Core Concepts

| Term | Description |
| --- | --- |
| **Epic** | Large feature (e.g., "User Authentication") |
| **Story** | User-level requirement (e.g., "User can log in") |
| **Task** | Technical work (e.g., "Implement login API") |
| **Bug** | Something broken that needs fixing |

### Workflow States (Typical)

```
Backlog → To Do → In Progress → Code Review → Done
```

> Jira tracks the lifecycle of work from idea → production.

---

## Quickstart (5-Minute Workflow)

### 1. Open Your Project

- Navigate to your team's Jira project
- Go to **Backlog** or **Board**

---

### 2. Find Your Assigned Task

Use filters:

- **Assigned to me**
- Sprint board (current work)

Each task contains:

- Description
- Acceptance criteria
- Priority
- Assignee

---

### 3. Understand the Task Before Starting

Before writing any code, check:

- ✅ What is the expected outcome?
- ✅ Are acceptance criteria clear?
- ✅ Are dependencies mentioned?

If unclear → comment on the ticket or ask your team.

---

### 4. Move Task to "In Progress"

When you start working, change the status to **In Progress**.

This signals:
- You are actively working on it
- Others should not pick it up

---

### 5. Do the Work and Link Code

While working:

1. Create a branch named after the ticket — example:
   ```
   feature/JIRA-123-login-api
   ```
2. Link your Pull Request (PR) to the Jira ticket

This creates traceability between code, task, and feature.

---

### 6. Move to "Code Review"

After completing your work, change the status to **Code Review**.

This tells reviewers the work is ready for validation.

---

### 7. Move to "Done"

Once the PR is approved, code is merged, and QA (if applicable) is complete — move the task to **Done**.

---

## Real-World Workflow Example

**Scenario:** You joined a backend team. Your first task is:

> "Implement login API" — ticket JIRA-123

### Flow:

1. Open backlog
2. Find ticket → JIRA-123
3. Read acceptance criteria
4. Move to **In Progress**
5. Write code + create PR named `feature/JIRA-123-login-api`
6. Link PR to ticket
7. Move to **Code Review**
8. After approval → **Done**

---

## Common Mistakes to Avoid

| Mistake | Why It Matters |
| --- | --- |
| Moving task to "Done" without merging code | Creates false visibility; work may be incomplete |
| Not updating status | Team loses visibility into what's in progress |
| Ignoring acceptance criteria | Code may not match what was requested |
| Working on unassigned tickets | Causes duplication and confusion |
| Not linking PR to Jira | Breaks traceability between code and tasks |

---

## Team Collaboration Best Practices

- Use comments for updates and blockers
- Tag teammates when clarification is needed
- Keep ticket status updated at all times
- Break large tasks into smaller, trackable ones

---

## Advanced Concepts

### Sprint

A fixed time period (typically 2 weeks) in which the team commits to completing a defined set of tasks.

### Backlog Grooming

The process of refining tasks, adding details, and prioritizing work before a sprint begins.

### Labels and Tags

Used for categorization and filtering — helpful for searching issues across a large project.

---

## When to Use Jira vs Other Tools

Use Jira when:

- Work needs to be tracked across multiple people
- Tasks move through structured, multi-step workflows
- You need audit trails or sprint-level reporting

---

## Summary

Jira is not just a task list — it is a **system for managing and communicating work across a team**.

Used correctly, it helps:

- Improve visibility into what is being worked on
- Reduce confusion about task ownership
- Ship features faster with less coordination overhead

---

## Next Steps

- Learn how to create and groom tickets
- Understand sprint planning and capacity
- Explore dashboards and reporting
- Practice using Jira in real workflows with your team