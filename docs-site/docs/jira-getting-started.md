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

This guide walks you through everything you need to get productive in Jira, from signing up to running your first sprint.

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
* **Your Work** : A personalized dashboard showing your assigned issues and recent activity.
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

> **🔍 Note:** The sidebar items vary depending on whether your project uses a Scrum or Kanban template.

## 5. Creating Your First Project
### 5.1 Start a New Project
1. From the top navigation, click **Projects** and select **Create project**.
2. Select a project template and choose **Scrum** or **Kanban**.
> **🔍 Note:** The sidebar items vary depending on whether your project uses a Scrum or Kanban template.
3. Enter a project name. For example, My First Project.
4. Enter a project key. For example, MFP. The key is used to prefix all issue IDs.
5. Set the access level to **Private** (recommended for new teams) or **Public**.
6. Click **Create**. 
    Jira creates the project and lands you on the project board.

## 5.2 Scrum or Kanban

| Feature | Scrum or Kanban |
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
| Task | A unit of work that does not directly map to a user story. For example: infrastructure. |
| Bug | A defect or unintended behavior that needs to be fixed. |
| Subtask | A smaller piece of work that belongs to a Story, Task, or Bug. |

### 6.2 Creating an Issue
1. Click the **+ Create** button in the top navigation or press `C` on your keyboard.
2. Select the Project and Issue Type.
3. Enter a Summary. For example, As a user, I can reset my password via email.
> **Note:** Write summaries in plain language that any team member can understand. Avoid abbreviations and acronyms in issue titles.
4. (Optional) Fill in the fields: Description, Assignee, Priority, Labels, Story Points, Sprint, and Epic Link.
5. Click **Create**.
    The issue appears in your Backlog or active sprint.



### 6.3 Issue Workflow States
Every issue moves through a workflow. The default Jira workflow includes these statuses:

* **To Do** : Work has not yet started.
* **In Progress** : A team member is actively working on the issue.
* **In Review** : The work is complete and awaiting review or QA.
* **Done** : The issue is resolved and accepted.

You can drag and drop issues between columns on the board to transition their status, or open an issue and use the status dropdown.

## 7. Running Your First Sprint
### 7.1 Populate the Backlog
Before starting a sprint, build up your backlog:

1. Navigate to your project.
2. Click **Backlog** in the left sidebar.
3. At the bottom of each Epic section, select **+ Create Issue** to create Stories, Tasks, and Bugs.
4. Open each issue and set the **Story Points** field to estimate effort.
5. Drag issues up and down to prioritize the backlog. The highest-priority items should be at the top.

### 7.2 Create and Start a Sprint
1. In the Backlog view, click **Create Sprint**. A new sprint container appears at the top.
2. Drag issues from the backlog into the sprint container. Estimate the amount of work your team can complete.
3. Click **Start Sprint** and A dialog appears.
4. Enter Sprint name, Duration, and Start/End dates.
5. Click **Start**.
   Your sprint is now active. Switch to the Board view to see all issues.

> **💡 Tip:** Aim to include only as many story points as your team has historically completed per sprint (your velocity). For new teams, start conservatively.

### 7.3 Complete a Sprint
1. At the end of the sprint period, in the Board view, click **Complete Sprint**.
2. Jira will prompt you to move any incomplete issues. You can move them to the Backlog or to the next sprint.
3. Jira will generate a Sprint Report. Review it with your team in your retrospective.

## 8. Collaborating with Your Team
### 8.1 Inviting Team Members
1. Go to **Project Settings** and select **People**.
2. Click **Add people** and enter the email addresses of the team members you want to invite.
3. Assign a role: **Viewer**, **Member**, or **Administrator**.
4. Click **Add**. 
    Invitees receive an email with a link to join the project.

### 8.2 Commenting and Mentioning
1. Open any issue and scroll to the bottom of the page.
2. On the **Activity** section, in the comment box, type the description or comments.
 * To notify a specific team member, for example, `@Jane Smith`, use `@mention`.
 * To insert rich content, use `/mention`, `/image`, `/table`, or `/code`.

### 8.3 Watching and Notifications
1. On a issue, click the **Watch** icon (eye) to subscribe to updates.
2. When an issue is updated, commented, or transitioned you will receive email notifications.
3. To configure your notification, 
  1. Go to **Profile**. 
  2. Select **Notification settings** and choose your preference.

## 9. Key Reports and Metrics
Jira built-in reports give your team insight into velocity, quality, and delivery health.

| Report | What It Shows |
| --- | --- |
| Burndown Chart | Tracks how much work remains in the current sprint day by day. |
| Velocity Chart | Shows average story points completed across the last several sprints. |
| Cumulative Flow Diagram | Visualizes work-in-progress and bottlenecks across workflow states. |
| Sprint Report | Summarizes completed vs. incomplete work at the end of each sprint. |
| Epic Report | Tracks progress toward completing an epic over time. |
| Control Chart | Measures cycle time for individual issues to identify process efficiency. |

To access reports, 
1. On the left sidebar of your project, click **Reports**.
2. On the left side of the Reports page, select the report from the list.


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
| Cannot see a project | Ask the project administrator to go to **Project Settings** page and select **People** option to add you. |
| Sprint Start button is greyed out | The backlog sprint container must have at least one issue before starting. |
| Cannot transition an issue | You does not have the required permission for that workflow transition. Contact your project admin. |
| Assignee dropdown is empty | Only project members can be assigned. Invite the user to the project first. |
| Reports show no data | Reports require at least one completed sprint. Complete your first sprint to generate data. |

## 12. Next Steps
You are now ready to manage your first project in Jira. Here are some recommended next steps to deepen your knowledge:

* **Explore Automation:** Set up no-code automation rules by using the **Automation** option in **Project Settings** to auto-assign issues, send notifications, or transition statuses.
* **Configure Custom Workflows:** Verify and customize the workflow states to match your team process using the **Workflows** option in **Project Settings**.
* **Connect Integrations:** Link Jira with Confluence (for documentation), Bitbucket or GitHub (for code), and Slack (for notifications).
* **Learn JQL:** Use Jira Query Language to build powerful custom filters and dashboard gadgets.
* **Set Up Roadmaps:** For Premium users, use Advanced Roadmaps to plan across multiple teams and projects.

> **📚 Resources:** Atlassian's official documentation is available at [https://support.atlassian.com/jira-software-cloud/](https://support.atlassian.com/jira-software-cloud/). The Atlassian Community forum at [https://community.atlassian.com](https://community.atlassian.com) is a great place to ask questions.

---
