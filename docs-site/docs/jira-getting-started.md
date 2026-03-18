---
title: Jira Getting Started Guide
description: Getting Started Guide for Jira Software, from zero to your first sprint.
---

# GETTING STARTED GUIDE: Jira Software
**From Zero to Your First Sprint**

**Version 1.0**  
**Audience:** New Users & Team Leads

## 1. Overview
Jira Software is a project management and issue-tracking platform developed by Atlassian. Originally built for software development teams, it has evolved into a versatile tool used by teams across IT, marketing, HR, and operations to plan work, track progress, and ship results.

This guide walks you through everything you need to get productive in Jira — from signing up to running your first sprint.

> **📋 Scope:** This guide covers Jira Software (cloud edition). Steps may vary slightly for Jira Work Management or Data Center deployments.

## 2. Prerequisites
Before you begin, confirm the following:

| Requirement | Details |
| --- | --- |
| Web Browser | Chrome 90+, Firefox 90+, Edge 90+, or Safari 14+ |
| Internet Connection | Stable broadband connection |
| Email Address | A valid business or personal email address |
| Permissions | Admin rights required to create a new project |
| Team Size Awareness | Free plan supports up to 10 users; Standard/Premium plans required beyond that |

## 3. Creating Your Jira Account
### 3.1 Sign Up for a Free Account
Follow these steps to create your Jira account:

1. Open your browser and navigate to https://www.atlassian.com/software/jira.
2. Click **Get it free** in the top-right navigation bar.
3. Enter your work email address and click **Continue**.
4. Check your inbox for a verification email from Atlassian and click the confirmation link.
5. Set a strong password (minimum 8 characters, including at least one number and one symbol).
6. Complete the short onboarding survey to help Atlassian tailor your experience.

> **💡 Tip:** Use your work email address. Atlassian uses your email domain to automatically link you to existing workspaces at your organization.

### 3.2 Choosing a Plan
Jira offers four plans. Choose the one that fits your team:

| Plan | Best For |
| --- | --- |
| Free | Teams up to 10 users. Includes core boards, backlog, and reporting. |
| Standard | Growing teams that need user roles, audit logs, and 250 GB storage. |
| Premium | Teams that need advanced roadmaps, automation, and capacity planning. |
| Enterprise | Large organizations requiring unlimited sites, security, and SLAs. |

## 4. Navigating the Jira Interface
Once logged in, you will land on the Jira home screen. Here is a breakdown of the key interface areas:

**Top Navigation Bar**
* **Your Work** – A personalized dashboard showing your assigned issues and recent activity.
* **Projects** – Browse, search, and switch between all projects you have access to.
* **Filters** – Save and manage custom JQL (Jira Query Language) searches.
* **Dashboards** – Create visual dashboards with gadgets for your key metrics.
* **Teams** – Manage people and workload across your organization.

**Left Sidebar (Project Context)**
* **Board** – Visualize active sprint tasks on a Scrum or Kanban board.
* **Backlog** – Manage the full queue of work not yet in a sprint.
* **Roadmap** – View the high-level timeline across epics and versions.
* **Reports** – Access built-in charts like Burndown, Velocity, and Control charts.
* **Project Settings** – Configure workflows, permissions, and notifications.

> **🔍 Note:** The sidebar items vary depending on whether your project uses a Scrum or Kanban template.

## 5. Creating Your First Project
### 5.1 Start a New Project
1. From the top navigation, click **Projects > Create project**.
2. Select a project template. For most software teams, choose **Scrum** or **Kanban**.
3. Enter a Project name (e.g., *My First Project*) and a Project key (e.g., *MFP*). The key is used to prefix all issue IDs.
4. Set the Access level: **Private** (recommended for new teams) or **Public**.
5. Click **Create**. Jira creates the project and lands you on the project board.

### 5.2 Scrum vs. Kanban — Which Should You Choose?

| Feature | Scrum vs. Kanban |
| --- | --- |
| Work cadence | Scrum uses time-boxed sprints (1–4 weeks); Kanban has a continuous flow |
| Best for | Scrum: feature development teams; Kanban: operations and support teams |
| Planning | Scrum requires sprint planning meetings; Kanban is on-demand |
| Reports | Scrum includes Burndown and Velocity charts; Kanban uses Cumulative Flow |
| Backlog | Both have a backlog; only Scrum has explicit sprint containers |

## 6. Working with Issues
An issue is the fundamental unit of work in Jira. It can represent a story, task, bug, epic, or subtask.

### 6.1 Issue Types

| Issue Type | Description |
| --- | --- |
| Epic | A large body of work that spans multiple sprints and breaks down into stories. |
| Story | A user-facing feature or requirement written from the end-user perspective. |
| Task | A unit of work that does not directly map to a user story (e.g., infrastructure). |
| Bug | A defect or unintended behavior that needs to be fixed. |
| Subtask | A smaller piece of work that belongs to a Story, Task, or Bug. |

### 6.2 Creating an Issue
1. Click the **+ Create** button in the top navigation or press `C` on your keyboard.
2. Select the Project and Issue Type.
3. Enter a clear Summary (e.g., *"As a user, I can reset my password via email"*).
4. Fill in optional fields: Description, Assignee, Priority, Labels, Story Points, Sprint, and Epic Link.
5. Click **Create**. The issue appears in your Backlog or active sprint.

> **✅ Best Practice:** Write summaries in plain language that any team member can understand. Avoid abbreviations and acronyms in issue titles.

### 6.3 Issue Workflow States
Every issue moves through a workflow. The default Jira workflow includes these statuses:

* **To Do** – Work has not yet started.
* **In Progress** – A team member is actively working on the issue.
* **In Review** – The work is complete and awaiting review or QA.
* **Done** – The issue is resolved and accepted.

You can drag and drop issues between columns on the board to transition their status, or open an issue and use the status dropdown.

## 7. Running Your First Sprint
### 7.1 Populate the Backlog
Before starting a sprint, build up your backlog:

1. Navigate to your project and click **Backlog** in the left sidebar.
2. Create all known Stories, Tasks, and Bugs using the **+ Create Issue** shortcut at the bottom of each Epic section.
3. Estimate effort using Story Points by opening each issue and setting the *Story Points* field.
4. Prioritize the backlog by dragging issues up and down. The highest-priority items should be at the top.

### 7.2 Create and Start a Sprint
1. In the Backlog view, click **Create Sprint**. A new sprint container appears at the top.
2. Drag issues from the backlog into the sprint container. Focus on the amount of work your team can realistically complete.
3. Click **Start Sprint**. A dialog appears asking for Sprint name, Duration (1, 2, 3, or 4 weeks), and Start/End dates.
4. Click **Start** and your sprint is now active. Switch to the Board view to see all issues.

> **💡 Tip:** Aim to include only as many story points as your team has historically completed per sprint (your velocity). For new teams, start conservatively.

### 7.3 Complete a Sprint
1. At the end of the sprint period, click **Complete Sprint** in the Board view.
2. Jira will prompt you to move any incomplete issues: send them to the Backlog or to the next sprint.
3. A Sprint Report is automatically generated. Review it with your team in your retrospective.

## 8. Collaborating with Your Team
### 8.1 Inviting Team Members
1. Go to **Project Settings > People**.
2. Click **Add people** and enter their email addresses.
3. Assign a role: **Viewer**, **Member**, or **Administrator**.
4. Click **Add**. Invitees receive an email with a link to join the project.

### 8.2 Commenting and Mentioning
* Open any issue and scroll to the **Activity** section at the bottom.
* Type in the comment box. Use `@mention` to notify a specific team member (e.g., `@Jane Smith`).
* Use `/mention`, `/image`, `/table`, or `/code` in the description or comments to insert rich content.

### 8.3 Watching and Notifications
* Click the **Watch** icon (eye) on any issue to subscribe to updates.
* You will receive email notifications whenever the issue is updated, commented on, or transitioned.
* Configure your notification preferences under **Profile > Notification settings**.

## 9. Key Reports and Metrics
Jira's built-in reports give your team insight into velocity, quality, and delivery health.

| Report | What It Shows |
| --- | --- |
| Burndown Chart | Tracks how much work remains in the current sprint day by day. |
| Velocity Chart | Shows average story points completed across the last several sprints. |
| Cumulative Flow Diagram | Visualizes work-in-progress and bottlenecks across workflow states. |
| Sprint Report | Summarizes completed vs. incomplete work at the end of each sprint. |
| Epic Report | Tracks progress toward completing an epic over time. |
| Control Chart | Measures cycle time for individual issues to identify process efficiency. |

To access reports, click **Reports** in the left sidebar of your project. Select any report from the list on the left side of the Reports page.

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

| Problem | Solution |
| --- | --- |
| Cannot see a project | Ask a project administrator to add you via Project Settings > People. |
| Sprint Start button is greyed out | The backlog sprint container must have at least one issue before starting. |
| Cannot transition an issue | You may lack the required permission for that workflow transition. Contact your project admin. |
| Assignee dropdown is empty | Only project members can be assigned. Invite the user to the project first. |
| Reports show no data | Reports require at least one completed sprint. Complete your first sprint to generate data. |

## 12. Next Steps
Congratulations — you are ready to manage your first project in Jira! Here are some recommended next steps to deepen your knowledge:

* **Explore Automation:** Set up no-code automation rules under **Project Settings > Automation** to auto-assign issues, send notifications, or transition statuses.
* **Configure Custom Workflows:** Tailor the workflow states to match your team process under **Project Settings > Workflows**.
* **Connect Integrations:** Link Jira with Confluence (for documentation), Bitbucket or GitHub (for code), and Slack (for notifications).
* **Learn JQL:** Use Jira Query Language to build powerful custom filters and dashboard gadgets.
* **Set Up Roadmaps:** For Premium users, use Advanced Roadmaps to plan across multiple teams and projects.

> **📚 Resources:** Atlassian's official documentation is available at [https://support.atlassian.com/jira-software-cloud/](https://support.atlassian.com/jira-software-cloud/). The Atlassian Community forum at [https://community.atlassian.com](https://community.atlassian.com) is a great place to ask questions.

---
*End of Document — Jira Software Getting Started Guide v1.0*