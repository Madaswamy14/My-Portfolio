---
title: Jira Getting Started Guide
description: Getting Started Guide consist of Jira overview, complete your first Jira workflow, core Jira concepts, and common mistakes.
---

# Jira Getting Started Guide

---

## Jira Overview

 Jira is a work-tracking system for software teams to plan, track, and deliver work. It connects requirements, work items, code changes, and completed features. Jira acts as a central repository for assigned work, task progress, and feature status. Jira improves team visibility, collaboration, and delivery speed. Jira is not just a task list. It is a communication system for work across a team.

---

## Core Jira Concepts

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

## Complete Your First Jira Workflow

In this topic, you will learn how to select a task, work on it, submit for review, and complete it.

**Prerequisites**: 
- Access to a Jira project
- Assigned task or access to sprint board
- Basic understanding of development workflow

1. Open your board.
2. Navigate to **Scrum Board** for sprint teams or **Kanban Board** for continuous workflow.
3. Use **Assigned to me** or the current sprint to find your task.
4. Review the task. Check the description, acceptance criteria, and dependencies. 
   >**Note:** If unclear, comment and ask for clarification before starting.
5. Move the task to **In Progress** and start working. 
This status indicates ownership and prevents others from duplicating work.

6. Once completed, to submit for review, do the following: 
   1. Create a branch using the ticket ID
   2. Open a Pull Request (PR), and link the PR to the Jira ticket.
   >**Note:** If you are not sure how to create a branch and open a PR, refer to the [Git and GitHub documentation](https://docs.github.com/en/get-started/quickstart/hello-world).
   3. Request review. Move the task to **Code Review**.
   
7. After the review is completed, merge the code to main branch.
8. Change the task status to **Done**.

Your task is fully tracked from assignment to completion.

---

## Common Mistakes

| Category | Mistake | Impact |
| --- | --- | --- |
| Workflow | Moving task to **Done** before merge | Creates false visibility |
| Process | Not linking PR to Jira | Breaks traceability |
| Comm. | Not commenting when blocked | Leaves task idle |

These mistakes reduce visibility, team coordination, and delivery speed.

---

## Real-World Scenarios

**Blocked Task**
Add a comment explaining the blocker. Tag the relevant teammate. Do not leave the task idle without context.

**Reopened Task**
If issues are found, the task moves back to **In Progress**. Fix the issues and repeat the workflow.

**Changing Requirements**
If requirements change, update the ticket and align with the team before continuing work.