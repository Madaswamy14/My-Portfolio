---
title: Jira Getting Started
description: Jira documentation structured by topic type covering concept overview, task workflow, reference, and common mistakes.
---

# Jira Getting Started Guide

---

## Concept: Jira Overview

Jira is a work-tracking system that software teams use to plan, track, and deliver work. It connects requirements, work items, code changes, and completed features. 

Jira acts as a single source of truth for assigned work, task progress, and feature status. When used correctly, it improves team visibility, collaboration, and delivery speed. Jira is not just a task list. It is a communication system for work across a team.

---

## Task: Complete Your First Jira Workflow

**Goal**: Pick up a task, complete it, and move it through the workflow correctly.

**Prerequisites**: Access to a Jira project, assigned task or access to sprint board, and a basic understanding of development workflow.

**Steps**:

1. Open your board. Navigate to **Scrum Board** for sprint teams or **Kanban Board** for continuous workflow.
2. Find your task. Locate work using **Assigned to me** or the current sprint.
3. Review the task. Check the description, acceptance criteria, and dependencies. If unclear, comment and ask for clarification before starting.
4. Start work. Move the task to **In Progress**. This status indicates ownership and prevents others from duplicating work.
5. Implement and link code. Create a branch using the ticket ID, open a Pull Request (PR), and link the PR to the Jira ticket.
6. Request review. Move the task to **Code Review**.
7. Complete the task. Move the task to **Done** only after the code is merged, the review is approved, and the acceptance criteria are met.

**Result**: Your task is fully tracked from assignment to completion.

---

## Reference: Core Jira Concepts

**Epic**: Large feature spanning multiple tasks

**Story**: User-level requirement

**Task**: Technical work

**Bug**: Defect or issue in existing functionality

In Jira, all of the above are technically referred to as **Issues**.

**Workflow States**: **Backlog** → **To Do** → **In Progress** → **Code Review** → **Done**

**Acceptance Criteria**: Defines what must be true for a task to be considered complete and how success is measured.

**Sprint**: A fixed time period where a team completes planned work.

**Backlog**: A prioritized list of upcoming tasks waiting to be assigned to a sprint.

---

## Reference: Common Mistakes

| Category | Mistake | Impact |
| --- | --- | --- |
| Workflow | Moving task to **Done** before merge | Creates false visibility |
| Process | Not linking PR to Jira | Breaks traceability |
| Comm. | Not commenting when blocked | Leaves task idle |

These mistakes reduce visibility, team coordination, and delivery speed.

---

## Reference: Real-World Scenarios

**Blocked Task**
Add a comment explaining the blocker. Tag the relevant teammate. Do not leave the task idle without context.

**Reopened Task**
If issues are found, the task moves back to **In Progress**. Fix the issues and repeat the workflow.

**Changing Requirements**
If requirements change, update the ticket and align with the team before continuing work.