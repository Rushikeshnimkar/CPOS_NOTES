---
layout: default
title: Agile Development
---

# Agile Development

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to Agile](#introduction-to-agile)
- [Agile Manifesto](#agile-manifesto)
- [Agile Principles](#agile-principles)
- [Scrum Framework](#scrum-framework)
- [Kanban](#kanban)
- [Extreme Programming (XP)](#extreme-programming-xp)
- [User Stories](#user-stories)
- [Agile Estimation](#agile-estimation)
- [Agile vs Traditional](#agile-vs-traditional)

---

## Introduction to Agile

### What is Agile?

> **Agile** is an iterative approach to software development that emphasizes flexibility, collaboration, and delivering working software frequently.

### Key Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Iterative** | Work in short cycles (sprints) |
| **Incremental** | Deliver working software in pieces |
| **Collaborative** | Team and customer work together |
| **Adaptive** | Respond to change quickly |
| **Feedback-driven** | Regular reviews and adjustments |

---

## Agile Manifesto

### Four Core Values

```
┌─────────────────────────────────────────────────────────┐
│              AGILE MANIFESTO (2001)                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  We are uncovering better ways of developing software   │
│  by doing it and helping others do it.                  │
│                                                         │
│  Through this work we have come to value:               │
│                                                         │
│  ┌───────────────────┐    ┌───────────────────┐        │
│  │ INDIVIDUALS AND   │ >  │ Processes and     │        │
│  │ INTERACTIONS      │    │ tools             │        │
│  └───────────────────┘    └───────────────────┘        │
│                                                         │
│  ┌───────────────────┐    ┌───────────────────┐        │
│  │ WORKING           │ >  │ Comprehensive     │        │
│  │ SOFTWARE          │    │ documentation     │        │
│  └───────────────────┘    └───────────────────┘        │
│                                                         │
│  ┌───────────────────┐    ┌───────────────────┐        │
│  │ CUSTOMER          │ >  │ Contract          │        │
│  │ COLLABORATION     │    │ negotiation       │        │
│  └───────────────────┘    └───────────────────┘        │
│                                                         │
│  ┌───────────────────┐    ┌───────────────────┐        │
│  │ RESPONDING TO     │ >  │ Following a       │        │
│  │ CHANGE            │    │ plan              │        │
│  └───────────────────┘    └───────────────────┘        │
│                                                         │
│  While there is value in items on right,                │
│  we value items on left MORE.                           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Agile Principles

### 12 Principles Behind the Manifesto

| # | Principle |
|---|-----------|
| 1 | Highest priority is customer satisfaction through early and continuous delivery |
| 2 | Welcome changing requirements, even late in development |
| 3 | Deliver working software frequently (weeks, not months) |
| 4 | Business people and developers work together daily |
| 5 | Build projects around motivated individuals; give them support and trust |
| 6 | Face-to-face conversation is the most efficient communication |
| 7 | Working software is the primary measure of progress |
| 8 | Maintain sustainable development pace indefinitely |
| 9 | Continuous attention to technical excellence and good design |
| 10 | Simplicity—maximizing work not done—is essential |
| 11 | Best architectures and designs emerge from self-organizing teams |
| 12 | Team regularly reflects on how to become more effective |

---

## Scrum Framework

### Overview

> **Scrum** is an agile framework for developing, delivering, and sustaining complex products.

### Scrum Roles

| Role | Responsibility |
|------|----------------|
| **Product Owner** | Defines features, prioritizes backlog, accepts/rejects work |
| **Scrum Master** | Facilitates process, removes impediments, coaches team |
| **Development Team** | Self-organizing, cross-functional, builds product |

### Scrum Events (Ceremonies)

```
┌─────────────────────────────────────────────────────────┐
│                   SCRUM EVENTS                          │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. Sprint Planning (Start of Sprint)                   │
│     └── Team selects items from backlog                 │
│     └── Creates sprint backlog                          │
│     └── Duration: 4-8 hours for 4-week sprint           │
│                                                         │
│  2. Daily Standup / Daily Scrum (15 min daily)          │
│     └── What did I do yesterday?                        │
│     └── What will I do today?                           │
│     └── Any impediments?                                │
│                                                         │
│  3. Sprint Review (End of Sprint)                       │
│     └── Demo completed work to stakeholders             │
│     └── Get feedback                                    │
│     └── Duration: 2-4 hours                             │
│                                                         │
│  4. Sprint Retrospective (After Review)                 │
│     └── What went well?                                 │
│     └── What could improve?                             │
│     └── Action items for next sprint                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Scrum Artifacts

| Artifact | Description |
|----------|-------------|
| **Product Backlog** | Prioritized list of all desired features |
| **Sprint Backlog** | Items committed for current sprint |
| **Increment** | Working product delivered at sprint end |

### Sprint Cycle

```
                    Product Backlog
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│                    SPRINT (2-4 weeks)                  │
│                                                        │
│    Sprint        Daily         Sprint       Sprint     │
│    Planning ──► Standup ──► Development ──► Review     │
│                   │                           │        │
│                   ▼                           │        │
│               (Repeat daily)                  │        │
│                                               ▼        │
│                                         Retrospective  │
│                                               │        │
└───────────────────────────────────────────────┼────────┘
                                                │
                                                ▼
                                    Potentially Shippable
                                         Increment
```

### Scrum Board

```
┌────────────────────────────────────────────────────────┐
│                     SCRUM BOARD                        │
├──────────┬──────────┬──────────┬──────────┬───────────┤
│  To Do   │  In      │   Code   │  Testing │   Done    │
│          │ Progress │  Review  │          │           │
├──────────┼──────────┼──────────┼──────────┼───────────┤
│ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │          │ ┌──────┐  │
│ │US-101│ │ │US-98 │ │ │US-95 │ │          │ │US-90 │  │
│ └──────┘ │ └──────┘ │ └──────┘ │          │ └──────┘  │
│ ┌──────┐ │ ┌──────┐ │          │ ┌──────┐ │ ┌──────┐  │
│ │US-102│ │ │US-99 │ │          │ │US-96 │ │ │US-91 │  │
│ └──────┘ │ └──────┘ │          │ └──────┘ │ └──────┘  │
│ ┌──────┐ │          │          │          │           │
│ │US-103│ │          │          │          │           │
│ └──────┘ │          │          │          │           │
└──────────┴──────────┴──────────┴──────────┴───────────┘
```

### Burndown Chart

```
Story
Points
  │
80│●
  │  ●
60│    ●               Ideal
  │      ●───●──●──────────────●
40│        ●                    
  │          ●        Actual
20│            ●───●         ●
  │                  ●───●
 0└────────────────────────────────► Days
   1  2  3  4  5  6  7  8  9  10
```

---

## Kanban

### Overview

> **Kanban** is a visual workflow management method that emphasizes continuous delivery without fixed iterations.

### Kanban Principles

| Principle | Description |
|-----------|-------------|
| Visualize workflow | Make work visible on board |
| Limit WIP | Set maximum items in each column |
| Manage flow | Monitor and optimize work movement |
| Make policies explicit | Define rules clearly |
| Continuous improvement | Regularly improve process |

### Kanban Board

```
┌────────────────────────────────────────────────────────┐
│                    KANBAN BOARD                        │
├──────────┬─────────────┬──────────────┬───────────────┤
│ Backlog  │ In Progress │    Done      │   Deployed    │
│          │   (WIP: 3)  │              │               │
├──────────┼─────────────┼──────────────┼───────────────┤
│ ┌──────┐ │ ┌──────┐    │ ┌──────┐     │ ┌──────┐      │
│ │Task 1│ │ │Task 4│    │ │Task 7│     │ │Task 9│      │
│ └──────┘ │ └──────┘    │ └──────┘     │ └──────┘      │
│ ┌──────┐ │ ┌──────┐    │ ┌──────┐     │ ┌──────┐      │
│ │Task 2│ │ │Task 5│    │ │Task 8│     │ │Task 10│     │
│ └──────┘ │ └──────┘    │ └──────┘     │ └──────┘      │
│ ┌──────┐ │ ┌──────┐    │              │               │
│ │Task 3│ │ │Task 6│    │              │               │
│ └──────┘ │ └──────┘    │              │               │
└──────────┴─────────────┴──────────────┴───────────────┘
```

### Scrum vs Kanban

| Aspect | Scrum | Kanban |
|--------|-------|--------|
| Iterations | Fixed sprints | Continuous |
| Roles | Defined (PO, SM, Team) | No prescribed roles |
| Changes | Not during sprint | Can change anytime |
| Metrics | Velocity | Lead time, cycle time |
| Board | Reset each sprint | Persistent |
| WIP Limits | Sprint capacity | Column limits |

---

## Extreme Programming (XP)

### Overview

> **Extreme Programming (XP)** is an agile methodology focused on engineering practices and technical excellence.

### XP Practices

| Practice | Description |
|----------|-------------|
| **Pair Programming** | Two developers work together |
| **TDD** | Write tests before code |
| **Continuous Integration** | Integrate code frequently |
| **Refactoring** | Improve code structure |
| **Simple Design** | Simplest solution that works |
| **Collective Ownership** | Anyone can change any code |
| **Coding Standards** | Consistent code style |
| **40-Hour Week** | Sustainable pace |
| **On-Site Customer** | Customer available to team |
| **Small Releases** | Frequent, small releases |

### XP Values

```
┌─────────────────────────────────────────────────────────┐
│                     XP VALUES                           │
├─────────────────────────────────────────────────────────┤
│                                                         │
│    ┌────────────┐    ┌────────────┐    ┌────────────┐  │
│    │Communication│    │ Simplicity │    │  Feedback  │  │
│    └────────────┘    └────────────┘    └────────────┘  │
│                                                         │
│         ┌────────────┐         ┌────────────┐          │
│         │  Courage   │         │  Respect   │          │
│         └────────────┘         └────────────┘          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## User Stories

### Format

```
As a [type of user],
I want [some goal],
So that [some reason].
```

### Examples

```
As a customer,
I want to view my order history,
So that I can track my past purchases.

As an administrator,
I want to generate monthly reports,
So that I can analyze business performance.
```

### INVEST Criteria

| Letter | Criterion | Description |
|--------|-----------|-------------|
| I | Independent | Story can be developed alone |
| N | Negotiable | Details can be discussed |
| V | Valuable | Delivers value to user |
| E | Estimable | Can be estimated |
| S | Small | Fits in one sprint |
| T | Testable | Has clear acceptance criteria |

### Acceptance Criteria

```
User Story: View Order History

Acceptance Criteria:
- GIVEN I am a logged-in customer
- WHEN I navigate to "My Orders"
- THEN I see a list of my past orders

- GIVEN I am on the orders page
- WHEN I click on an order
- THEN I see the order details
```

---

## Agile Estimation

### Story Points

> Story points measure relative effort, not time.

### Fibonacci Sequence

```
1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

Common values used: 1, 2, 3, 5, 8, 13, 21

Larger numbers = more uncertainty
```

### Planning Poker

```
Process:
1. PO presents user story
2. Team discusses and clarifies
3. Each member secretly selects card
4. All reveal simultaneously
5. Discuss differences
6. Repeat until consensus
```

### Velocity

```
Velocity = Sum of story points completed in a sprint

Example:
Sprint 1: 21 points
Sprint 2: 18 points
Sprint 3: 24 points
Sprint 4: 20 points

Average Velocity = (21+18+24+20) / 4 = 20.75 points/sprint
```

### Estimation Techniques

| Technique | Description |
|-----------|-------------|
| **Planning Poker** | Team estimates with cards |
| **T-Shirt Sizing** | S, M, L, XL categories |
| **Dot Voting** | Vote on relative size |
| **Affinity Mapping** | Group similar items |

---

## Agile vs Traditional

### Comparison

| Aspect | Agile | Waterfall |
|--------|-------|-----------|
| **Planning** | Adaptive, iterative | Predictive, upfront |
| **Requirements** | Evolving | Fixed |
| **Delivery** | Frequent increments | Single delivery |
| **Changes** | Welcomed | Difficult |
| **Documentation** | Light, essential | Comprehensive |
| **Customer** | Continuous involvement | Beginning and end |
| **Testing** | Throughout | At the end |
| **Team** | Self-organizing | Structured hierarchy |
| **Feedback** | Continuous | Post-delivery |

### When to Use Agile

| Use Agile When | Avoid Agile When |
|----------------|------------------|
| Requirements unclear | Requirements are fixed |
| Rapid delivery needed | Predictability required |
| High customer involvement | Limited customer access |
| Innovation required | Regulatory compliance |
| Small-medium teams | Very large, distributed teams |
| Complex, changing domain | Simple, well-understood domain |

---

## Summary

- Agile emphasizes individuals, working software, collaboration, and adaptability
- Scrum provides structure with sprints, roles, and ceremonies
- Kanban focuses on visualizing workflow and limiting WIP
- XP emphasizes engineering practices
- User stories capture requirements in user-centric format
- Story points estimate relative effort
- Choose methodology based on project needs

---

[← Previous: OOAD](04-ooad.md) | [Next: Jira →](06-jira.md)
