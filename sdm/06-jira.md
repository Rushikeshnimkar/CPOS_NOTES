---
layout: default
title: Atlassian Jira
---

# Introduction to Atlassian Jira

[← Back to Home](../index.md)

---

## What is Jira?

> **Jira** is a project management and issue tracking tool by Atlassian for agile software development.

## Key Concepts

| Component | Description |
|-----------|-------------|
| **Project** | Container for all related issues |
| **Issue** | Unit of work (story, bug, task) |
| **Epic** | Large body of work spanning sprints |
| **Sprint** | Time-boxed iteration |
| **Board** | Visual representation of work |
| **Backlog** | Prioritized list of work |

## Issue Types

| Type | Purpose |
|------|---------|
| **Epic** | Large feature spanning sprints |
| **Story** | User-facing functionality |
| **Task** | Technical or general work |
| **Bug** | Defect to fix |
| **Subtask** | Breakdown of parent issue |

## Workflows

A **Workflow** defines the sequence of statuses an issue goes through.

```
Open → In Progress → In Review → Testing → Done
```

## Boards

### Scrum Board
- Sprint-based
- Fixed iterations
- Velocity tracking

### Kanban Board
- Continuous flow
- WIP limits
- Lead/cycle time metrics

## Reports

| Report | Purpose |
|--------|---------|
| **Burndown** | Track remaining work |
| **Velocity** | Story points per sprint |
| **Sprint Report** | Sprint summary |

## JQL Examples

```
project = "PROJ" AND type = Bug AND status != Done
assignee = currentUser() AND resolution = Unresolved
priority = High AND sprint in openSprints()
```

---

[← Previous: Agile](05-agile.md) | [Next: DevOps →](07-devops.md)
