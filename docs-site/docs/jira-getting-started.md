---
title: Jira Getting Started Guide
description: Getting Started Guide for Jira Software, from zero to your first sprint.
---

# Jira Getting Started Guide

**Version:** 1.0  
**Audience:** New Users & Team Leads  

## 1. Overview
Jira Software provides a comprehensive set of tools for teams to manage modern projects. Users can create issues to represent work items and organize them into backlogs for future planning. The system tracks the status of every task from the initial idea to the final release. Project managers depend on these features to allocate resources and set realistic deadlines. This introduction explains the core functions of the tool to help new users start quickly.

Benefits of using Jira Software:
* **Centralized Work Tracking**: Projects, issues, comments, and due dates stay in one system instead of being spread across chat, email, and spreadsheets.
* **Improved Collaboration**: Teams can assign work, add context, ask follow-up questions, and see status changes without losing history.
* **Visual Workflows**: Kanban and Scrum boards provide a shared view of the work process, making it easy to see bottlenecks and areas for improvement.
* **Powerful Reporting**: Dashboards, filters, and reports show issue trends, workload, and project progress over time.

This guide walks you through everything you need to get productive in Jira, from signing up to running your first sprint.

> **Scope:** This guide covers Jira Software (cloud edition). Steps may vary slightly for Jira Work Management or Data Center deployments.

## 2. Prerequisites
Before you begin, confirm the following:

| Requirement | Details |
| --- | --- |
| Web browser | Chrome 90+, Firefox 90+, Edge 90+, or Safari 14+ |
| Internet connection | Stable broadband connection |
| Email address | A valid business or personal email address |
| Permissions | Admin rights required to create a new project |
| Team size awareness | Free plan supports up to 10 users; Standard/Premium plans required beyond that |

## 3. Create a Jira Account
Jira is a cloud-based platform, so you will need to create an account to get started.
### 3.1 Sign Up for an Account
This section explains how to create a Jira account.
**Prerequisites:**
* A valid email address

To sign up,

1. On the desktop, open your browser and go to https://www.atlassian.com/software/jira.
2. On the top-right of the screen, click **Get it free**.
3. Enter your work email address and click **Continue**.
4. Check your inbox for a verification email from Atlassian and click the confirmation link.
5. Set a strong password. A minimum of 8 characters, including at least one number and one symbol.
6. Click **Continue**.
7. Click **Start using Jira**.
You have successfully created a Jira account.

> **Note:** Use your work email address. Atlassian uses your email domain to automatically link you to existing workspaces at your organization.

### 3.2 Choose a Plan
This section explains how to choose a plan for your Jira account.
**Prerequisites:**
* A Jira account

To choose,
1. On the top-right of the screen, click **Start free trial**.
2. Select a plan that fits your team.
| Plan | Best for |
| --- | --- |
| Free | Teams up to 10 users. Includes core boards, backlog, and reporting. |
| Standard | Growing teams that need user roles, audit logs, and 250 GB storage. |
| Premium | Teams that need advanced roadmaps, automation, and capacity planning. |
| Enterprise | Large organizations requiring unlimited sites, security, and SLAs. |

3. Click **Continue**.
4. Click **Start free trial**.
You have successfully chosen a plan for your Jira account.

## 4. Explore the Jira user interface
This section explains the key interface areas of Jira.

After you log in, the Jira home screen appears. The key interface areas are:

**Top Navigation Bar**
* **Your Work** : View a personalized dashboard of assigned issues and recent activity.
* **Projects** : Browse, search, and switch between all projects you have access to.
* **Filters** : Save and manage custom JQL (Jira Query Language) searches.
* **Dashboards** : Create visual dashboards with gadgets for your key metrics.
* **Teams** : Manage people and workload across your organization.

**Left Sidebar (Project Context)**
* **Board** : Visualize active sprint tasks on a Scrum or Kanban board.
* **Backlog** : Manage the full queue of work not yet in a sprint.
* **Roadmap** : View the high-level timeline across epics and versions.
* **Reports** : Access built-in charts like Burndown, Velocity, and Control charts.
* **Project Settings** : Configure workflows, permissions, and notifications.

> **Note:** The sidebar items vary based on whether your project uses a Scrum or Kanban template.

## 5. Create a Project
This section explains how to create a project in Jira.
### 5.1 Start a New Project
This section explains how to start a new project in Jira.
**Prerequisites:**
* A Jira account
* A Jira plan with at least 1 active site
To start,
1. On the top navigation, click **Projects** and select **Create project**.
2. Select a project template and choose **Scrum** or **Kanban**.
3. Enter a project name. For example, My First Project.
4. Enter a project key. For example, MFP. The key is used to prefix all issue IDs.
5. Set the access level to **Private** or **Public**.
6. Click **Create**.
The project is created and you are taken to the project board.

### 5.2 Scrum or Kanban
This section explains the differences between Scrum and Kanban in Jira.

| Feature | Scrum or Kanban |
| --- | --- |
| Work cadence | Scrum uses time-boxed sprints with fixed duration of 1 to 4 weeks; Kanban has a continuous flow |
| Best for | Scrum: feature development teams; Kanban: operations and support teams |
| Planning | Scrum requires sprint planning meetings; Kanban is on-demand |
| Reports | Scrum includes Burndown and Velocity charts; Kanban uses Cumulative Flow |
| Backlog | Both have a backlog; only Scrum has explicit sprint containers |

## 6. Manage issues
An issue is the fundamental unit of work in Jira. It can represent a story, task, bug, epic, or subtask.

### 6.1 Issue Types
This section explains the different types of issues in Jira.

| Issue Type | Description |
| --- | --- |
| Epic | A large body of work that spans multiple sprints and breaks down into stories. |
| Story | A user-facing feature or requirement written from the end-user perspective. |
| Task | A unit of work that does not directly map to a user story. |
| Bug | A defect or unintended behavior that needs to be fixed. |
| Subtask | A smaller piece of work that belongs to a Story, Task, or Bug. |

### 6.2 Create an Issue
This section explains how to create an issue in Jira.
**Prerequisites:**
* A Jira account
* A Jira project
To create,
1. On the top navigation, click the **+ Create** button or press `C` on your keyboard.
2. On the **Create** screen, Select the Project and Issue Type.
3. Enter a Summary.
> **Note:** Write summaries in plain language that every team member can understand. Avoid abbreviations and acronyms in titles.
4. (Optional) Fill in the fields: Description, Assignee, Priority, Labels, Story Points, Sprint, and Epic Link.
5. Click **Create**.
The issue appears in your Backlog or active sprint.

### 6.3 Issue Workflow States
This section explains the different workflow states of an issue in Jira.

Every issue moves through a workflow. The default Jira workflow includes these statuses:

* **To Do** : Work has not yet started.
* **In Progress** : A team member is actively working on the issue.
* **In Review** : The work is complete and awaiting review or QA.
* **Done** : The issue is resolved and accepted.

You can drag and drop issues between columns on the board to transition their status, or open an issue and use the status dropdown.

## 7. Run Your First Sprint
### 7.1 Populate the Backlog
This section explains how to populate the backlog in Jira. Before starting a sprint, build up your backlog.
**Prerequisites:**
* A Jira account
* A Jira project
To populate,
1. On the top navigation, click **Projects** and select your project.
2. On the left pane, click **Backlog**.
3. At the bottom of each Epic section, select **+ Create Issue** to create Stories, Tasks, and Bugs.
4. Open each issue and set the **Story Points** field to estimate effort.
5. Drag issues up and down to prioritize the backlog. The highest-priority items should be at the top.
You have successfully populated the backlog.

### 7.2 Create and Start a Sprint
This section explains how to create and start a sprint in Jira.
**Prerequisites:**
* A Jira account
* A Jira project
* A populated backlog
To create and start,
1. In the Backlog view, click **Create Sprint**. A new sprint container appears at the top.
2. Drag issues from the backlog into the sprint container. Estimate the amount of work your team can complete.
3. Click **Start Sprint** and A dialog appears.
4. Enter Sprint name, Duration, and Start/End dates.
5. Click **Start**.
Your sprint is now active. Switch to the Board view to see all issues.

### 7.3 Complete a Sprint
This section explains how to complete a sprint in Jira.
**Prerequisites:**
* A Jira account
* A Jira project
* An active sprint
To complete,
1. At the end of the sprint period, in the Board view, click **Complete Sprint**.
2. Jira will prompt you to move any incomplete issues. You can move them to the Backlog or to the next sprint.
3. Jira will generate a Sprint Report. Review it with your team in your retrospective.
You have successfully completed a sprint.

## 8. Collaborate with Your Team
This section explains how to collaborate with your team in Jira.
### 8.1 Invite Team Members
This section explains how to invite team members to a project in Jira.
**Prerequisites:**
* A Jira account
* A Jira project
To invite,
1. On the top navigation, click **Projects** and select your project.
2. On the left pane, click **Settings** and select **People**.
3. On the **People** page, click **Add people**.
4. Enter the email addresses of the team members you want to invite.
5. Assign a role: **Viewer**, **Member**, or **Administrator**.
6. Click **Add**. 
You have successfully invited team members. Invitees receive an email with a link to join the project.

### 8.2 Comment and Mention
This section explains how to comment and mention in Jira.
**Prerequisites:**
* A Jira account
* A Jira project
* A team member to comment and mention
To comment and mention,
1. On the top navigation, click **Projects** and select your project.
2. On the left pane, click **Board**.
3. Click an issue to open it.
4. Scroll to the bottom of the page.
5. In the comment box, type the description or comments.
  * To notify a specific team member, for example, `@Jane Smith`, use `@mention`.
  * To insert rich content, use `/mention`, `/image`, `/table`, or `/code`.
6. Click **Comment**.
You have successfully commented and mentioned.

### 8.3 Watch and Notifications
This section explains how to watch and notifications in Jira.
**Prerequisites:**
* A Jira account
* A Jira project
* A team member to watch and notifications
To watch and notifications,
1. On the top navigation, click **Projects** and select your project.
2. On the left pane, click **Board**.
3. Click an issue to open it.
4. On the top of the page, click the **Watch** icon (eye).
You have successfully watched an issue. You will receive email notifications when the issue is updated, commented, or transitioned.

## 9. Reports
### 9.1 Report Types
This section explains the different types of reports in Jira.
| Report | Description |
| --- | --- |
| Burndown Chart | Tracks how much work remains in the current sprint day by day. |
| Velocity Chart | Shows average story points completed across the last several sprints. |
| Cumulative Flow Diagram | Visualizes work-in-progress and bottlenecks across workflow states. |
| Sprint Report | Summarizes completed vs. incomplete work at the end of each sprint. |
| Epic Report | Tracks progress toward completing an epic over time. |
| Control Chart | Measures cycle time for individual issues to identify process efficiency. |

### 9.2 View Reports
This section explains how to view reports in Jira.
**Prerequisites:**
* A Jira account
* A Jira project
* A completed sprint

To view,
1. On the top navigation, click **Projects** and select your project.
2. On the left pane, click **Reports**.
3. On the left side of the Reports page, select the report from the list.
4. View the report.
You have successfully viewed the report.

## 10. Keyboard Shortcuts
Learning these shortcuts will significantly speed up your workflow:

| Shortcut | Action |
| --- | --- |
| `C` | Create a new issue from anywhere in Jira |
| `/` or `F` | Open the quick search bar |
| `G` then `D` | Go to your personal Dashboard |
| `G` then `P` | Go to the current Project board |
| `E` | Edit the currently open issue |
| `A` | Assign the current issue to yourself |
| `M` | Leave a comment on the current issue |
| `?` (Shift + /) | Open the full keyboard shortcuts reference |

## 11. Troubleshooting Common Issues
This section explains how to troubleshoot common issues in Jira.
| Problem | Solution |
| --- | --- |
| Cannot see a project | Ask the project administrator to go to **Project Settings** page and select **People** option to add you. |
| Sprint Start button is greyed out | The backlog sprint container must have at least one issue before starting. |
| Cannot transition an issue | You does not have the required permission for that workflow transition. Contact your project admin. |
| Assignee dropdown is empty | Only project members can be assigned. Invite the user to the project first. |
| Reports show no data | Reports require at least one completed sprint. Complete your first sprint to generate data. |

You have successfully troubleshooted common issues.

---
