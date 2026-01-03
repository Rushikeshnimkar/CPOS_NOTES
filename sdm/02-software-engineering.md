---
layout: default
title: Software Engineering
---

# Software Engineering

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to Software Engineering](#introduction-to-software-engineering)
- [Software Characteristics](#software-characteristics)
- [Software Crisis](#software-crisis)
- [Software Engineering Principles](#software-engineering-principles)
- [Software Process](#software-process)
- [Software Metrics](#software-metrics)
- [Software Quality](#software-quality)

---

## Introduction to Software Engineering

### What is Software?

> **Software** is a collection of programs, data, and documentation that performs specific tasks on a computer system.

### Components of Software

```
┌─────────────────────────────────────────┐
│              SOFTWARE                   │
├─────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐       │
│  │  Programs   │  │    Data     │       │
│  │  (Code)     │  │ (Databases) │       │
│  └─────────────┘  └─────────────┘       │
│           ┌─────────────┐               │
│           │Documentation│               │
│           │  (Manuals)  │               │
│           └─────────────┘               │
└─────────────────────────────────────────┘
```

### What is Software Engineering?

> **Software Engineering** is the application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software.

### IEEE Definition

"The application of a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software; that is, the application of engineering to software."

---

## Software Characteristics

### Unique Properties of Software

| Characteristic | Description |
|----------------|-------------|
| **Intangible** | Cannot be seen or touched |
| **No wear out** | Doesn't degrade physically |
| **Custom built** | Often tailor-made |
| **Complex** | High logical complexity |
| **Flexible** | Easy to modify |
| **Expensive** | Development costs are high |

### Software vs Hardware

| Aspect | Software | Hardware |
|--------|----------|----------|
| Nature | Logical | Physical |
| Development | Engineered | Manufactured |
| Wear | No wear | Wears out |
| Defects | Bugs from design | Manufacturing defects |
| Maintenance | Updates fix issues | Replacement needed |
| Cost | Development-heavy | Manufacturing-heavy |

### Software Failure Rate

```
Failure
Rate
  ^
  │     Hardware
  │    ┌──────────────────────
  │   /
  │  /
  │ /
  │/
  │                    Software (Actual)
  │    ┌────────────────────────────────
  │   /         ╲       ╱╲      ╱
  │──/           ╲─────╱  ╲────╱  (Changes cause spikes)
  │
  └──────────────────────────────────────► Time

Ideal Software: Flat line (no degradation)
Actual Software: Spikes due to changes/updates
```

---

## Software Crisis

### Definition

> **Software Crisis** refers to the problems encountered in software development, including budget overruns, time delays, poor quality, and unmet requirements.

### Causes of Software Crisis

| Category | Problems |
|----------|----------|
| **Size** | Larger programs, more complexity |
| **Quality** | Hard to ensure correctness |
| **Cost** | Difficult to estimate |
| **Schedule** | Frequent delays |
| **Maintenance** | Takes majority of budget |
| **Change** | Requirements constantly evolve |

### Historical Context

- **1960s-70s**: Recognition of crisis
- Large projects failing
- Cost overruns of 100-200%
- Delivered products not meeting needs

### Solutions

1. **Methodologies**: Structured approaches
2. **Tools**: CASE tools, IDEs
3. **Processes**: Established SDLC models
4. **Standards**: Quality standards (ISO, CMMI)
5. **Training**: Professional development

---

## Software Engineering Principles

### Core Principles

| Principle | Description |
|-----------|-------------|
| **Rigor and Formality** | Precise, systematic approach |
| **Separation of Concerns** | Divide problem into parts |
| **Modularity** | Divide into manageable modules |
| **Abstraction** | Hide complexity, show essentials |
| **Anticipation of Change** | Design for future modifications |
| **Generality** | Make solutions reusable |
| **Incrementality** | Develop in steps |

### SOLID Principles (OOP)

| Letter | Principle | Description |
|--------|-----------|-------------|
| S | Single Responsibility | One reason to change |
| O | Open/Closed | Open for extension, closed for modification |
| L | Liskov Substitution | Subtypes substitutable for base types |
| I | Interface Segregation | Many specific interfaces better than one |
| D | Dependency Inversion | Depend on abstractions, not concretions |

### DRY and KISS

- **DRY**: Don't Repeat Yourself
- **KISS**: Keep It Simple, Stupid
- **YAGNI**: You Aren't Gonna Need It

---

## Software Process

### Definition

> A **Software Process** is a structured set of activities required to develop a software system.

### Generic Process Framework

```
┌─────────────────────────────────────────────────────────┐
│                  SOFTWARE PROCESS                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌───────────────┐                                      │
│  │Communication │ → Requirements gathering              │
│  └───────┬───────┘                                      │
│          ▼                                              │
│  ┌───────────────┐                                      │
│  │   Planning    │ → Estimation, scheduling             │
│  └───────┬───────┘                                      │
│          ▼                                              │
│  ┌───────────────┐                                      │
│  │   Modeling    │ → Analysis, design                   │
│  └───────┬───────┘                                      │
│          ▼                                              │
│  ┌───────────────┐                                      │
│  │ Construction  │ → Coding, testing                    │
│  └───────┬───────┘                                      │
│          ▼                                              │
│  ┌───────────────┐                                      │
│  │  Deployment   │ → Delivery, support                  │
│  └───────────────┘                                      │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Umbrella Activities

Activities applied throughout the process:

- Project tracking and control
- Risk management
- Quality assurance
- Configuration management
- Technical reviews
- Measurement
- Reusability management

---

## Software Metrics

### What are Metrics?

> **Software Metrics** are quantitative measures used to estimate, assess, and improve software development processes and products.

### Categories of Metrics

| Category | Focus | Examples |
|----------|-------|----------|
| **Product** | Software characteristics | Size, complexity, quality |
| **Process** | Development activities | Productivity, cost, time |
| **Project** | Project management | Schedule, effort, resources |

### Common Metrics

#### Size Metrics

| Metric | Description |
|--------|-------------|
| **LOC** | Lines of Code |
| **KLOC** | Thousand Lines of Code |
| **Function Points** | Functionality-based measure |
| **Object Points** | Object-oriented measure |

#### Complexity Metrics

| Metric | Description |
|--------|-------------|
| **Cyclomatic Complexity** | Control flow complexity |
| **Halstead Metrics** | Program vocabulary and length |
| **Coupling** | Module interconnection |
| **Cohesion** | Module internal relatedness |

#### Quality Metrics

| Metric | Formula/Description |
|--------|---------------------|
| **Defect Density** | Defects / KLOC |
| **Defect Removal Efficiency** | Defects found before release / Total defects |
| **MTBF** | Mean Time Between Failures |
| **MTTR** | Mean Time To Repair |

### Cyclomatic Complexity

```
V(G) = E - N + 2

Where:
- E = number of edges
- N = number of nodes

Or: V(G) = P + 1 (P = predicate nodes/decision points)

Example:
if (a > b) {         // Decision 1
    if (c > d) {     // Decision 2
        ...
    }
}
Complexity = 2 + 1 = 3
```

---

## Software Quality

### Quality Definition

> **Software Quality** is the degree to which software meets specified requirements and user needs.

### Quality Attributes (ISO 9126 / 25010)

```
┌─────────────────────────────────────────────────────────┐
│                  SOFTWARE QUALITY                       │
├────────────────────┬────────────────────────────────────┤
│ Functionality      │ Suitability, accuracy, security   │
├────────────────────┼────────────────────────────────────┤
│ Reliability        │ Maturity, fault tolerance, recover│
├────────────────────┼────────────────────────────────────┤
│ Usability          │ Learnability, operability, UI     │
├────────────────────┼────────────────────────────────────┤
│ Efficiency         │ Time behavior, resource usage     │
├────────────────────┼────────────────────────────────────┤
│ Maintainability    │ Modifiability, testability        │
├────────────────────┼────────────────────────────────────┤
│ Portability        │ Adaptability, installability      │
└────────────────────┴────────────────────────────────────┘
```

### Quality Factors (McCall's Model)

```
                    ┌───────────────────┐
                    │  QUALITY FACTORS  │
                    └─────────┬─────────┘
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
    ┌───────────┐       ┌───────────┐       ┌───────────┐
    │ OPERATION │       │ REVISION  │       │TRANSITION │
    └─────┬─────┘       └─────┬─────┘       └─────┬─────┘
          │                   │                   │
    • Correctness       • Maintainability   • Portability
    • Reliability       • Flexibility       • Reusability
    • Efficiency        • Testability       • Interoperability
    • Integrity
    • Usability
```

### Quality Assurance vs Quality Control

| Aspect | Quality Assurance (QA) | Quality Control (QC) |
|--------|------------------------|----------------------|
| Focus | Process | Product |
| When | Throughout development | At specific points |
| Goal | Prevent defects | Find defects |
| Example | Reviews, audits | Testing |

### CMM/CMMI Levels

| Level | Name | Description |
|-------|------|-------------|
| 1 | Initial | Ad hoc, chaotic |
| 2 | Managed | Project-level discipline |
| 3 | Defined | Organization-wide standards |
| 4 | Quantitatively Managed | Metrics-based management |
| 5 | Optimizing | Continuous improvement |

---

## Software Development Challenges

### Brooks' Law

> "Adding manpower to a late software project makes it later."

### The Mythical Man-Month

- Software development is not linear
- Communication overhead increases with team size
- Training new members takes time

### Common Challenges

| Challenge | Description |
|-----------|-------------|
| **Changing requirements** | Requirements evolve constantly |
| **Estimation** | Hard to estimate time and cost |
| **Technology** | Rapid technology changes |
| **Integration** | Combining components is difficult |
| **Communication** | Team and stakeholder communication |
| **Quality** | Balancing speed and quality |

---

## Summary

- Software engineering applies systematic approach to software development
- Software has unique characteristics (intangible, complex, no wear)
- Software crisis led to development of methodologies and processes
- Key principles: modularity, abstraction, separation of concerns
- Metrics help measure and improve software quality
- Quality encompasses functionality, reliability, usability, and more

---

[← Previous: Git](01-git.md) | [Next: SDLC →](03-sdlc.md)
