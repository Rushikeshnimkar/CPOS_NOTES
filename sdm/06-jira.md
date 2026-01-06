---
layout: default
title: Atlassian Jira
---

# Introduction to Atlassian Jira

[← Back to Home](../index.md)

---

## What is Jira?

> **Jira** is a project management and issue tracking tool by Atlassian for agile software development.

### History
- Originally developed in 2002 by Atlassian (Australia)
- Named after "Gojira" (Japanese for Godzilla)
- Now used by 180,000+ organizations worldwide

### Jira Products
| Product | Purpose |
|---------|---------|
| **Jira Software** | Agile project management for dev teams |
| **Jira Service Management** | IT service desk and customer support |
| **Jira Work Management** | Business team project management |

---

## Key Concepts

| Component | Definition |
|-----------|------------|
| **Project** | Container for all related issues |
| **Issue** | Unit of work (story, bug, task) |
| **Epic** | Large body of work spanning sprints |
| **Sprint** | Time-boxed iteration (Scrum) |
| **Board** | Visual representation of work |
| **Backlog** | Prioritized list of work |
| **Component** | Logical grouping within a project |
| **Version** | Release or milestone |

---

## Issue Types

> Issues are the building blocks of Jira projects.

| Type | Definition | Icon |
|------|------------|------|
| **Epic** | Large feature spanning multiple sprints | 🟣 Purple |
| **User Story** | User-facing functionality from user's perspective | 🟢 Green |
| **Task** | Technical or general work item | 🔵 Blue |
| **Bug** | Defect that needs to be fixed | 🔴 Red |
| **Subtask** | Breakdown of parent issue | Smaller icon |

### Issue Hierarchy
```
Epic (months of work)
  └── User Story (days of work)
        └── Subtask (hours of work)
```

### Issue Fields

| Field | Description |
|-------|-------------|
| **Summary** | Brief title of the issue |
| **Description** | Detailed explanation |
| **Assignee** | Person responsible |
| **Reporter** | Person who created it |
| **Priority** | Highest, High, Medium, Low, Lowest |
| **Status** | Current state (To Do, In Progress, Done) |
| **Labels** | Tags for categorization |
| **Story Points** | Effort estimation (Scrum) |
| **Sprint** | Which sprint it belongs to |

---

## Workflows

> A **Workflow** defines the sequence of statuses an issue goes through from creation to completion.

### Default Workflow
```
┌────────┐    ┌─────────────┐    ┌──────┐
│ To Do  │───►│ In Progress │───►│ Done │
└────────┘    └─────────────┘    └──────┘
```

### Extended Workflow Example
```
┌────────┐   ┌─────────────┐   ┌───────────┐   ┌─────────┐   ┌──────┐
│  Open  │──►│ In Progress │──►│ In Review │──►│ Testing │──►│ Done │
└────────┘   └─────────────┘   └───────────┘   └─────────┘   └──────┘
      │                              │               │
      └──────────────────────────────┴───────────────┘
                    (Can be reopened)
```

### Workflow Components

| Component | Definition |
|-----------|------------|
| **Status** | Current state of an issue |
| **Transition** | Movement between statuses |
| **Condition** | Rules for when transition is allowed |
| **Validator** | Checks before transition completes |
| **Post Function** | Actions after transition |

---

## Agile Boards

### Scrum Board

> For teams working in **sprints** (time-boxed iterations).

| Feature | Description |
|---------|-------------|
| **Backlog** | Prioritized list of work |
| **Sprint** | Fixed 1-4 week iterations |
| **Sprint Planning** | Select items for sprint |
| **Velocity** | Story points completed per sprint |
| **Burndown Chart** | Track remaining work |

### Kanban Board

> For teams with **continuous flow** of work.

| Feature | Description |
|---------|-------------|
| **Continuous Flow** | No fixed iterations |
| **WIP Limits** | Limit work in each column |
| **Cycle Time** | Time from start to completion |
| **Lead Time** | Time from creation to completion |
| **Cumulative Flow** | Visualize work over time |

### Scrum vs Kanban

| Aspect | Scrum | Kanban |
|--------|-------|--------|
| **Iterations** | Fixed sprints | Continuous |
| **Planning** | Sprint planning | On-demand |
| **Roles** | Scrum Master, PO | Flexible |
| **Changes** | After sprint | Anytime |
| **Metrics** | Velocity | Cycle time |

---

## Jira Reports

| Report | Purpose | Board Type |
|--------|---------|------------|
| **Burndown Chart** | Track remaining work in sprint | Scrum |
| **Burnup Chart** | Track completed vs total work | Scrum |
| **Velocity Chart** | Story points per sprint trend | Scrum |
| **Sprint Report** | Sprint summary and analysis | Scrum |
| **Cumulative Flow** | Visualize work across statuses | Kanban |
| **Control Chart** | Cycle time over time | Both |

### Burndown Chart Interpretation
```
Ideal ──────────────────────────────────────
         \                                    
          \    AHEAD                          
           \       Actual ─────             
            \                  \              
             \                  \  BEHIND     
              \                   ─────────
               ▼                              
              Done                            
```

---

## JQL (Jira Query Language)

> **JQL** is a powerful search language to find and filter issues.

### Basic Syntax
```
field = value
field IN (value1, value2)
field IS EMPTY
field IS NOT EMPTY
```

### Common JQL Examples

```sql
-- My open issues
assignee = currentUser() AND resolution = Unresolved

-- High priority bugs in current sprint
project = "PROJ" AND type = Bug AND priority = High AND sprint in openSprints()

-- Issues created this week
project = "PROJ" AND created >= startOfWeek()

-- Unassigned stories in backlog
type = Story AND assignee IS EMPTY AND sprint IS EMPTY

-- Issues updated in last 7 days
updated >= -7d

-- Complex query
project = "PROJ" AND type IN (Bug, Task) AND status NOT IN (Done, Closed) 
AND priority >= High ORDER BY priority DESC, created ASC
```

### JQL Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `=`, `!=` | Equals, not equals | `status = "Done"` |
| `IN`, `NOT IN` | Multiple values | `type IN (Bug, Task)` |
| `~`, `!~` | Contains, not contains | `summary ~ "login"` |
| `>`, `<`, `>=`, `<=` | Comparison | `created >= -7d` |
| `IS EMPTY`, `IS NOT EMPTY` | Null check | `assignee IS EMPTY` |
| `WAS`, `WAS IN`, `CHANGED` | Historical | `status WAS "In Progress"` |

### JQL Functions

| Function | Description |
|----------|-------------|
| `currentUser()` | Logged-in user |
| `membersOf("team")` | Team members |
| `openSprints()` | Active sprints |
| `closedSprints()` | Completed sprints |
| `startOfDay()`, `endOfWeek()` | Date functions |

---

## Best Practices

### Project Setup
1. **Define clear issue types** - Know when to use story vs task
2. **Create simple workflows** - Start simple, add complexity later
3. **Use components** - Organize by module/feature
4. **Set up versions** - Track releases

### Daily Usage
1. **Keep issues updated** - Status, assignee, time tracking
2. **Link related issues** - Show dependencies
3. **Use labels wisely** - Don't over-tag
4. **Comment regularly** - Document decisions

### Sprint Management
1. **Groom backlog regularly** - Keep it prioritized
2. **Estimate consistently** - Use planning poker
3. **Limit sprint scope** - Don't overcommit
4. **Review and adapt** - Use retrospectives

---

## Jira Integrations

| Integration | Purpose |
|-------------|---------|
| **Confluence** | Documentation linked to issues |
| **Bitbucket/GitHub** | Link commits and PRs to issues |
| **Slack** | Notifications and updates |
| **Jenkins** | CI/CD build status |
| **Trello** | Simple board integration |

---

[← Previous: Agile](05-agile.md) | [Next: DevOps →](07-devops.md)
