---
layout: default
title: Object Oriented Analysis and Design
---

# Object Oriented Analysis and Design (OOAD)

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to OOAD](#introduction-to-ooad)
- [Object-Oriented Concepts](#object-oriented-concepts)
- [UML Overview](#uml-overview)
- [Use Case Diagrams](#use-case-diagrams)
- [Class Diagrams](#class-diagrams)
- [Sequence Diagrams](#sequence-diagrams)
- [Activity Diagrams](#activity-diagrams)
- [State Diagrams](#state-diagrams)
- [Design Patterns](#design-patterns)

---

## Introduction to OOAD

### What is OOAD?

> **Object-Oriented Analysis and Design (OOAD)** is a technical approach for analyzing and designing an application by applying object-oriented programming concepts.

### Analysis vs Design

| Analysis | Design |
|----------|--------|
| WHAT the system should do | HOW to implement it |
| Problem domain focus | Solution domain focus |
| Conceptual model | Technical model |
| User perspective | Developer perspective |

### OOAD Process

```
┌─────────────────────────────────────────────────────────┐
│                     OOAD Process                        │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  1. Object-Oriented Analysis (OOA)                      │
│     └── Identify objects, classes, relationships        │
│     └── Define use cases                                │
│     └── Create analysis model                           │
│                                                         │
│  2. Object-Oriented Design (OOD)                        │
│     └── Refine analysis model                           │
│     └── Design system architecture                      │
│     └── Design classes and interfaces                   │
│                                                         │
│  3. Object-Oriented Programming (OOP)                   │
│     └── Implement designed classes                      │
│     └── Write code following OOP principles             │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Object-Oriented Concepts

### Core Concepts

| Concept | Description |
|---------|-------------|
| **Object** | Instance of a class with state and behavior |
| **Class** | Blueprint/template for objects |
| **Encapsulation** | Bundling data and methods together |
| **Abstraction** | Hiding complexity, showing essentials |
| **Inheritance** | Deriving new classes from existing ones |
| **Polymorphism** | Same interface, different implementations |

### Object

```
┌───────────────────────────┐
│         Object            │
├───────────────────────────┤
│   State (Attributes)      │
│   • name = "John"         │
│   • age = 25              │
│   • salary = 50000        │
├───────────────────────────┤
│   Behavior (Methods)      │
│   • calculateBonus()      │
│   • updateSalary()        │
│   • getDetails()          │
└───────────────────────────┘
```

### Class

```
┌───────────────────────────┐
│      Class: Employee      │
├───────────────────────────┤
│   Attributes              │
│   - name: String          │
│   - age: int              │
│   - salary: double        │
├───────────────────────────┤
│   Methods                 │
│   + calculateBonus()      │
│   + updateSalary()        │
│   + getDetails()          │
└───────────────────────────┘
```

### Inheritance

```
        ┌───────────────┐
        │    Animal     │  (Parent/Base Class)
        │ ─────────────│
        │ + eat()       │
        │ + sleep()     │
        └───────┬───────┘
                │
       ┌────────┴────────┐
       │                 │
┌──────┴──────┐   ┌──────┴──────┐
│     Dog     │   │     Cat     │  (Child Classes)
│ ───────────│   │ ───────────│
│ + bark()    │   │ + meow()    │
└─────────────┘   └─────────────┘
```

### Polymorphism

```java
// Method Overloading (Compile-time)
class Calculator {
    int add(int a, int b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
}

// Method Overriding (Runtime)
class Animal {
    void sound() { System.out.println("Animal sound"); }
}

class Dog extends Animal {
    void sound() { System.out.println("Bark"); }
}
```

---

## UML Overview

### What is UML?

> **Unified Modeling Language (UML)** is a standardized visual modeling language for software systems.

### UML Diagram Types

```
┌─────────────────────────────────────────────────────────┐
│                    UML DIAGRAMS                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  STRUCTURAL (Static)         BEHAVIORAL (Dynamic)       │
│  ──────────────────         ────────────────────       │
│  • Class Diagram             • Use Case Diagram         │
│  • Object Diagram            • Sequence Diagram         │
│  • Component Diagram         • Activity Diagram         │
│  • Deployment Diagram        • State Machine Diagram    │
│  • Package Diagram           • Communication Diagram    │
│  • Composite Structure       • Interaction Overview     │
│                              • Timing Diagram           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

---

## Use Case Diagrams

### Components

| Element | Symbol | Description |
|---------|--------|-------------|
| **Actor** | Stick figure | External entity interacting with system |
| **Use Case** | Ellipse | Functionality provided by system |
| **System Boundary** | Rectangle | Scope of the system |
| **Association** | Line | Connection between actor and use case |
| **Include** | Dashed arrow (<<include>>) | Mandatory included functionality |
| **Extend** | Dashed arrow (<<extend>>) | Optional extended functionality |

### Example: Online Shopping System

```
┌────────────────────────────────────────────────────────────┐
│              Online Shopping System                        │
│                                                            │
│    ┌──────────┐                          ┌──────────┐     │
│    │  Browse  │                          │  Admin   │     │
│    │ Products │                          │ Panel    │     │
│    └────┬─────┘                          └────┬─────┘     │
│   ╱╲    │                                     │    ╲      │
│  ╱  ╲   │     ┌──────────┐                   │     ╲     │
│ │User│──┼────►│Add to Cart│                  │    Admin  │
│  ╲  ╱   │     └─────┬────┘                   │     ╱     │
│   ╲╱    │           │ <<include>>            │    ╱      │
│         │           ▼                        │           │
│         │     ┌──────────┐     <<extend>>    │           │
│         ├────►│ Checkout │◄─────────────────┤           │
│         │     └─────┬────┘                   │           │
│         │           │ <<include>>            │           │
│         │           ▼                        │           │
│         │     ┌──────────┐                   │           │
│         │     │  Payment │                   │           │
│         │     └──────────┘                   │           │
│         │                                    │           │
│         │     ┌──────────┐                   │           │
│         └────►│View Orders│◄─────────────────┘           │
│               └──────────┘                               │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

### Relationships

| Relationship | Meaning |
|--------------|---------|
| **Association** | Actor participates in use case |
| **Include** | Use case always includes another |
| **Extend** | Use case may optionally extend another |
| **Generalization** | Inheritance between actors/use cases |

---

## Class Diagrams

### Class Notation

```
┌─────────────────────────────────────┐
│           ClassName                 │
├─────────────────────────────────────┤
│  Attributes (Properties)            │
│  ──────────────────────────         │
│  - privateAttr: DataType            │
│  + publicAttr: DataType             │
│  # protectedAttr: DataType          │
│  ~ packageAttr: DataType            │
├─────────────────────────────────────┤
│  Methods (Operations)               │
│  ────────────────────               │
│  + publicMethod(): ReturnType       │
│  - privateMethod(): void            │
│  # protectedMethod(): String        │
└─────────────────────────────────────┘
```

### Visibility Symbols

| Symbol | Visibility |
|--------|------------|
| `+` | Public |
| `-` | Private |
| `#` | Protected |
| `~` | Package |

### Relationships

```
Association:        A ────────────── B

Aggregation:        A ◇────────────── B  (has-a, weak)

Composition:        A ◆────────────── B  (has-a, strong)

Inheritance:        A ◁───────────── B  (is-a)

Dependency:         A - - - - - - - ► B  (uses)

Realization:        A ◁- - - - - - - B  (implements)
```

### Multiplicity

| Notation | Meaning |
|----------|---------|
| `1` | Exactly one |
| `0..1` | Zero or one |
| `*` or `0..*` | Zero or more |
| `1..*` | One or more |
| `n..m` | Between n and m |

### Example: Library System

```
┌───────────────────┐         ┌───────────────────┐
│      Library      │         │       Book        │
├───────────────────┤ 1    * ├───────────────────┤
│ - name: String    │◆───────│ - isbn: String    │
│ - address: String │         │ - title: String   │
├───────────────────┤         │ - author: String  │
│ + addBook()       │         ├───────────────────┤
│ + removeBook()    │         │ + getDetails()    │
└───────────────────┘         └─────────┬─────────┘
                                        △
                              ┌─────────┴─────────┐
                              │                   │
                    ┌─────────┴───────┐ ┌─────────┴───────┐
                    │    Fiction      │ │   NonFiction    │
                    ├─────────────────┤ ├─────────────────┤
                    │ - genre: String │ │ - subject: String│
                    └─────────────────┘ └─────────────────┘
```

---

## Sequence Diagrams

### Components

| Element | Description |
|---------|-------------|
| **Object/Actor** | Participant in interaction |
| **Lifeline** | Vertical dashed line showing time |
| **Activation Box** | Period when object is active |
| **Message** | Communication between objects |
| **Return** | Response to a message |

### Message Types

| Type | Symbol | Description |
|------|--------|-------------|
| Synchronous | ────►| | Wait for response |
| Asynchronous | ─ ─ ─►| | Don't wait |
| Return | ◄─ ─ ─ | Response |
| Self | Loop back | Object calls itself |

### Example: Login Process

```
  User          LoginController      UserService        Database
   │                  │                  │                 │
   │  login(user,pwd) │                  │                 │
   │─────────────────>│                  │                 │
   │                  │  authenticate()  │                 │
   │                  │─────────────────>│                 │
   │                  │                  │  findUser()     │
   │                  │                  │────────────────>│
   │                  │                  │                 │
   │                  │                  │  user data      │
   │                  │                  │<────────────────│
   │                  │                  │                 │
   │                  │  auth result     │                 │
   │                  │<─────────────────│                 │
   │                  │                  │                 │
   │  success/failure │                  │                 │
   │<─────────────────│                  │                 │
   │                  │                  │                 │
```

### Combined Fragments

| Fragment | Purpose |
|----------|---------|
| `alt` | Alternative (if-else) |
| `opt` | Optional (if) |
| `loop` | Iteration |
| `par` | Parallel execution |
| `break` | Exit loop |

---

## Activity Diagrams

### Components

| Element | Symbol | Description |
|---------|--------|-------------|
| Initial Node | ● | Start of activity |
| Final Node | ⊕ | End of activity |
| Action | Rectangle | Task/activity |
| Decision | ◇ | Branch point |
| Merge | ◇ | Join branches |
| Fork | Thick bar | Start parallel |
| Join | Thick bar | End parallel |

### Example: Order Processing

```
        ●
        │
        ▼
┌───────────────┐
│ Receive Order │
└───────┬───────┘
        │
        ▼
       ◇───────────────────────────────┐
    Stock?                              │
       │                                │
     Yes                               No
       │                                │
       ▼                                ▼
┌───────────────┐               ┌───────────────┐
│ Process Order │               │ Notify Out of │
└───────┬───────┘               │    Stock      │
        │                       └───────┬───────┘
        │                               │
    ════╧═════                          │
    ║        ║                          │
    ▼        ▼                          │
┌──────┐  ┌──────┐                      │
│ Pack │  │Invoice│                     │
└──┬───┘  └──┬───┘                      │
   ║         ║                          │
   ════╤═════                           │
        │                               │
        ▼                               │
┌───────────────┐                       │
│    Ship       │                       │
└───────┬───────┘                       │
        │                               │
        ◇◄──────────────────────────────┘
        │
        ▼
       ⊕
```

---

## State Diagrams

### Components

| Element | Description |
|---------|-------------|
| State | Condition of object |
| Initial State | Starting state |
| Final State | End state |
| Transition | Change between states |
| Event | Trigger for transition |
| Guard | Condition for transition |
| Action | Activity during transition |

### Example: Order State Machine

```
       ●
       │
       ▼
  ┌─────────┐   place order   ┌─────────┐
  │  New    │────────────────►│ Pending │
  └─────────┘                 └────┬────┘
                                   │
                          payment received
                                   │
                                   ▼
                             ┌─────────┐
              cancel         │Confirmed│
       ┌─────────────────────┤         │
       │                     └────┬────┘
       │                          │
       ▼                     ship order
  ┌─────────┐                     │
  │Cancelled│                     ▼
  └─────────┘                ┌─────────┐
                             │ Shipped │
                             └────┬────┘
                                  │
                             delivered
                                  │
                                  ▼
                             ┌─────────┐
                             │Delivered│
                             └────┬────┘
                                  │
                                  ▼
                                  ⊕
```

---

## Design Patterns

### Categories

| Category | Purpose | Examples |
|----------|---------|----------|
| **Creational** | Object creation | Singleton, Factory, Builder |
| **Structural** | Object composition | Adapter, Decorator, Facade |
| **Behavioral** | Object interaction | Observer, Strategy, Command |

### Common Patterns

#### Singleton Pattern

```
┌────────────────────────────┐
│       Singleton            │
├────────────────────────────┤
│ - instance: Singleton      │
├────────────────────────────┤
│ - Singleton()              │
│ + getInstance(): Singleton │
└────────────────────────────┘

// Usage: Ensures only one instance exists
```

#### Factory Pattern

```
┌───────────────────┐           ┌───────────────────┐
│     Creator       │           │     Product       │
├───────────────────┤           ├───────────────────┤
│                   │           │                   │
│ + factoryMethod() │──────────►│  <<interface>>    │
└─────────┬─────────┘           └─────────┬─────────┘
          △                               △
          │                               │
┌─────────┴─────────┐           ┌─────────┴─────────┐
│ ConcreteCreator   │           │  ConcreteProduct  │
└───────────────────┘           └───────────────────┘
```

#### Observer Pattern

```
┌───────────────────┐      *     ┌───────────────────┐
│     Subject       │◇──────────│     Observer      │
├───────────────────┤            ├───────────────────┤
│ + attach()        │            │ + update()        │
│ + detach()        │            └───────────────────┘
│ + notify()        │
└───────────────────┘

// Usage: One-to-many dependency for notifications
```

#### MVC Pattern

```
        ┌─────────────────────────────────────────┐
        │                                         │
        ▼                                         │
┌───────────────┐         ┌───────────────┐      │
│    Model      │◄────────│  Controller   │      │
│ (Data/Logic)  │         │ (Handles Input│──────┤
└───────┬───────┘         └───────────────┘      │
        │                         ▲              │
        │                         │              │
        ▼                         │              │
┌───────────────┐                 │              │
│     View      │─────────────────┘              │
│ (UI Display)  │────────────────────────────────┘
└───────────────┘          User Interaction
```

---

## Summary

- OOAD uses objects to model systems
- UML provides standardized notation
- Use Case diagrams capture requirements
- Class diagrams show structure
- Sequence diagrams show interactions
- Activity diagrams show workflows
- State diagrams show object lifecycle
- Design patterns provide reusable solutions

---

[← Previous: SDLC](03-sdlc.md) | [Next: Agile →](05-agile.md)
