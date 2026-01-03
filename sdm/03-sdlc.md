---
layout: default
title: Software Development Life Cycle
---

# Software Development Life Cycle (SDLC)

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to SDLC](#introduction-to-sdlc)
- [SDLC Phases](#sdlc-phases)
- [Waterfall Model](#waterfall-model)
- [Iterative Model](#iterative-model)
- [Spiral Model](#spiral-model)
- [V-Model](#v-model)
- [RAD Model](#rad-model)
- [Prototype Model](#prototype-model)
- [Model Comparison](#model-comparison)

---

## Introduction to SDLC

### What is SDLC?

> **Software Development Life Cycle (SDLC)** is a process used by the software industry to design, develop, and test high-quality software.

### Purpose of SDLC

- Provides structured approach to development
- Ensures quality deliverables
- Facilitates project management
- Reduces risks and costs
- Improves communication

---

## SDLC Phases

### Standard Phases

```
┌─────────────────────────────────────────────────────────┐
│                      SDLC PHASES                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. Planning & Requirements Analysis                    │
│     └── Define scope, feasibility, gather requirements  │
│                       ▼                                 │
│  2. System Design                                       │
│     └── Architecture, HLD, LLD                          │
│                       ▼                                 │
│  3. Implementation/Coding                               │
│     └── Write code based on design                      │
│                       ▼                                 │
│  4. Testing                                             │
│     └── Verify software meets requirements              │
│                       ▼                                 │
│  5. Deployment                                          │
│     └── Release to production                           │
│                       ▼                                 │
│  6. Maintenance                                         │
│     └── Updates, fixes, enhancements                    │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Phase Details

| Phase | Input | Activities | Output |
|-------|-------|------------|--------|
| **Requirements** | Business needs | Gathering, analysis | SRS document |
| **Design** | SRS | Architecture design | Design documents |
| **Implementation** | Design docs | Coding, unit testing | Source code |
| **Testing** | Code | Integration, system test | Test reports |
| **Deployment** | Tested software | Installation, training | Live system |
| **Maintenance** | Live system | Support, updates | Updated system |

---

## Waterfall Model

### Overview

> The **Waterfall Model** is a linear sequential approach where each phase must be completed before the next begins.

### Diagram

```
┌─────────────────────┐
│     Requirements    │
│       Analysis      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   System Design     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Implementation    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Testing        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     Deployment      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    Maintenance      │
└─────────────────────┘
```

### Characteristics

| Aspect | Description |
|--------|-------------|
| **Flow** | Linear, sequential |
| **Phases** | Each completed before next |
| **Documentation** | Extensive at each phase |
| **Customer involvement** | Only at beginning and end |

### Advantages

- Simple and easy to understand
- Well-defined stages
- Easy to manage
- Works well for smaller projects with clear requirements

### Disadvantages

- No working software until late
- Difficult to accommodate changes
- High risk and uncertainty
- Not suitable for complex projects
- Poor model for long projects

### When to Use

- Requirements are very clear and fixed
- Product definition is stable
- Technology is understood
- Ample resources available
- Short project duration

---

## Iterative Model

### Overview

> The **Iterative Model** develops the system through repeated cycles (iterations), allowing refinement based on feedback.

### Diagram

```
┌────────────────────────────────────────────────────────┐
│                                                        │
│    ┌──────────┐                                        │
│    │ Initial  │                                        │
│    │ Planning │                                        │
│    └────┬─────┘                                        │
│         │                                              │
│         ▼                                              │
│    ┌──────────────────────────────────────────────┐   │
│    │              Iteration Cycle                  │   │
│    │  ┌────────┐  ┌────────┐  ┌────────┐         │   │
│    │  │Planning│→ │Design &│→ │ Test & │ ──────┐ │   │
│    │  │        │  │ Code   │  │Evaluate│       │ │   │
│    │  └────────┘  └────────┘  └────────┘       │ │   │
│    │       ▲                                    │ │   │
│    │       └────────── Feedback ───────────────┘ │   │
│    └──────────────────────────────────────────────┘   │
│         │                                              │
│         ▼                                              │
│    ┌──────────┐                                        │
│    │Deployment│                                        │
│    └──────────┘                                        │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### Advantages

- Working software early
- Flexible to changing requirements
- Risk management improved
- Parallel development possible
- Constant feedback

### Disadvantages

- More resources required
- Management complexity
- System architecture may change
- End of project not clearly defined

---

## Spiral Model

### Overview

> The **Spiral Model** combines iterative development with systematic risk analysis.

### Diagram

```
                    Planning
                       │
            ┌──────────┴──────────┐
            │                     │
     Risk Analysis          Requirements
            │                     │
            │    ┌───────────┐    │
            │    │           │    │
            └───►│  SPIRAL   │◄───┘
                 │  CENTER   │
            ┌───►│           │◄───┐
            │    └───────────┘    │
            │                     │
      Prototypes              Design
            │                     │
            └──────────┬──────────┘
                       │
                   Development
                    & Testing
```

### Four Quadrants

```
┌─────────────────────┬─────────────────────┐
│                     │                     │
│    DETERMINE        │       IDENTIFY      │
│    OBJECTIVES       │       AND RESOLVE   │
│                     │       RISKS         │
│   • Requirements    │   • Risk analysis   │
│   • Alternatives    │   • Prototyping     │
│   • Constraints     │   • Simulation      │
│                     │                     │
├─────────────────────┼─────────────────────┤
│                     │                     │
│    PLAN NEXT        │       DEVELOP       │
│    ITERATION        │       AND TEST      │
│                     │                     │
│   • Review results  │   • Design          │
│   • Plan next phase │   • Coding          │
│                     │   • Testing         │
│                     │                     │
└─────────────────────┴─────────────────────┘
```

### Advantages

- Strong risk management
- Good for large projects
- Customer feedback incorporated
- Early development visibility
- Flexible

### Disadvantages

- Complex and costly
- Requires expertise in risk assessment
- Not suitable for small projects
- Excessive documentation
- Difficult to manage

### When to Use

- Large, high-risk projects
- Requirements unclear initially
- Significant changes expected
- Long-term commitment required

---

## V-Model

### Overview

> The **V-Model** is an extension of Waterfall where testing phases are parallel to development phases.

### Diagram

```
Requirements ─────────────────────────────── Acceptance Testing
Analysis          \                      /
                   \                    /
    System ─────────\──────────────────/───── System Testing
    Design           \                /
                      \              /
         Architecture ─\────────────/──── Integration Testing
         Design         \          /
                         \        /
              Module ─────\──────/────── Unit Testing
              Design       \    /
                            \  /
                             \/
                         Coding
```

### Phases Correlation

| Development Phase | Testing Phase |
|-------------------|---------------|
| Requirements Analysis | Acceptance Testing |
| System Design | System Testing |
| Architecture Design | Integration Testing |
| Module Design | Unit Testing |
| Coding | - |

### Advantages

- Test planning starts early
- Clear deliverables per stage
- High discipline
- Works well for small projects
- Easy to manage

### Disadvantages

- Very rigid
- Software produced late
- No early prototypes
- No risk handling
- Not for complex projects

---

## RAD Model

### Overview

> **Rapid Application Development (RAD)** emphasizes quick development using component-based construction.

### Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    RAD Model                            │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │           Business Modeling                       │  │
│  │    (Understand business functions)                │  │
│  └─────────────────────┬────────────────────────────┘  │
│                        ▼                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │            Data Modeling                          │  │
│  │    (Define data objects and relationships)        │  │
│  └─────────────────────┬────────────────────────────┘  │
│                        ▼                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │           Process Modeling                        │  │
│  │    (Transform data objects)                       │  │
│  └─────────────────────┬────────────────────────────┘  │
│                        ▼                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │         Application Generation                    │  │
│  │    (Use automated tools, reusable components)     │  │
│  └─────────────────────┬────────────────────────────┘  │
│                        ▼                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │         Testing and Turnover                      │  │
│  │    (Test components, full system)                 │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Key Features

- 60-90 day development cycle
- Component reuse
- CASE tools usage
- Parallel development teams

### Advantages

- Reduced development time
- Quick customer feedback
- Component reusability
- Better customer involvement

### Disadvantages

- Requires skilled developers
- Needs strong commitment
- Not for all applications
- Complex management

---

## Prototype Model

### Overview

> **Prototype Model** builds an initial prototype to understand requirements before developing the actual system.

### Types of Prototypes

| Type | Description | Fate |
|------|-------------|------|
| **Throwaway** | Quick prototype for requirements | Discarded after use |
| **Evolutionary** | Refined into final product | Becomes the product |
| **Incremental** | Multiple prototypes combined | Parts become product |

### Diagram

```
┌─────────────────────────────────────────────────────────┐
│                  Prototype Model                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│    ┌───────────────────────────────────────────────┐   │
│    │         Requirements Gathering                 │   │
│    └────────────────────┬──────────────────────────┘   │
│                         │                               │
│                         ▼                               │
│    ┌───────────────────────────────────────────────┐   │
│    │            Quick Design                        │   │
│    └────────────────────┬──────────────────────────┘   │
│                         │                               │
│                         ▼                               │
│    ┌───────────────────────────────────────────────┐   │
│    │          Build Prototype                       │   │
│    └────────────────────┬──────────────────────────┘   │
│                         │                               │
│                         ▼                               │
│    ┌───────────────────────────────────────────────┐   │
│    │        Customer Evaluation ◄─────────────────┐│   │
│    └────────────────────┬─────────────────────────┘│   │
│                         │                          │   │
│                    Satisfied?                      │   │
│                         │                          │   │
│            No ─────────►└──────────────────────────┘   │
│            │                                            │
│            │ Yes                                        │
│            ▼                                            │
│    ┌───────────────────────────────────────────────┐   │
│    │            Engineer Product                    │   │
│    └───────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Advantages

- Better understanding of requirements
- User involvement throughout
- Reduced time and cost
- Early identification of flaws

### Disadvantages

- User may think prototype is final
- Poor documentation
- May increase complexity
- Excessive development time

---

## Model Comparison

### Summary Table

| Model | Best For | Risk Level | Flexibility |
|-------|----------|------------|-------------|
| Waterfall | Small, clear requirements | High | Low |
| Iterative | Medium projects | Medium | Medium |
| Spiral | Large, high-risk | Low | High |
| V-Model | Small, clear requirements | Medium | Low |
| RAD | Quick delivery needed | Medium | High |
| Prototype | Unclear requirements | Low | High |
| Agile | Changing requirements | Low | Very High |

### Decision Factors

```
┌─────────────────────────────────────────────────────────┐
│              CHOOSING AN SDLC MODEL                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  Requirements                                           │
│    Clear? ────► Waterfall / V-Model                     │
│    Unclear? ──► Prototype / Agile                       │
│                                                         │
│  Project Size                                           │
│    Small? ────► Waterfall / V-Model                     │
│    Large? ────► Spiral / Iterative                      │
│                                                         │
│  Risk Level                                             │
│    High? ─────► Spiral                                  │
│    Low? ──────► Waterfall / RAD                         │
│                                                         │
│  Time Constraint                                        │
│    Tight? ────► RAD / Agile                             │
│    Flexible? ─► Waterfall / Spiral                      │
│                                                         │
│  Customer Involvement                                   │
│    High? ─────► Agile / Prototype                       │
│    Low? ──────► Waterfall                               │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Summary

- SDLC provides structured approach to software development
- Waterfall: Linear, sequential, good for clear requirements
- Iterative: Repeated cycles, flexible to changes
- Spiral: Risk-driven, good for large complex projects
- V-Model: Testing parallel to development
- RAD: Quick development with reusable components
- Prototype: Build prototype first, clarify requirements
- Choose model based on project characteristics

---

[← Previous: Software Engineering](02-software-engineering.md) | [Next: OOAD →](04-ooad.md)
