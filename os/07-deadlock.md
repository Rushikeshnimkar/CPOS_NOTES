---
layout: default
title: Deadlock
---

# Deadlock

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to Deadlock](#introduction-to-deadlock)
- [Necessary Conditions](#necessary-conditions)
- [Resource Allocation Graph](#resource-allocation-graph)
- [Deadlock Prevention](#deadlock-prevention)
- [Deadlock Avoidance](#deadlock-avoidance)
- [Banker's Algorithm](#bankers-algorithm)
- [Deadlock Detection](#deadlock-detection)
- [Deadlock Recovery](#deadlock-recovery)
- [Numerical Problems](#numerical-problems)

---

## Introduction to Deadlock

### What is Deadlock?

> **Deadlock** is a situation where a set of processes are blocked because each process is holding a resource and waiting for another resource acquired by some other process.

### Real-World Example

```
┌─────────────────────────────────────────────────────────┐
│                     Traffic Deadlock                    │
│                                                         │
│              Car B                                      │
│                ↓                                        │
│    Car A → ┌─────┐ ← Car C                             │
│            │     │                                      │
│            └─────┘                                      │
│                ↑                                        │
│              Car D                                      │
│                                                         │
│    Each car is waiting for the other to move first!    │
└─────────────────────────────────────────────────────────┘
```

### System Model

```
Process P1                    Process P2
    │                             │
    │ Request(R1)                 │ Request(R2)
    ▼                             ▼
   R1 ────────────────────────  R2
(Holds R1)                   (Holds R2)
    │                             │
    │ Request(R2)                 │ Request(R1)
    ▼                             ▼
  WAITING                      WAITING
    │                             │
    └──────── DEADLOCK ───────────┘
```

---

## Necessary Conditions

### Four Conditions for Deadlock

All four conditions must hold simultaneously for deadlock to occur:

| # | Condition | Description |
|---|-----------|-------------|
| 1 | **Mutual Exclusion** | At least one resource must be non-sharable |
| 2 | **Hold and Wait** | Process holds at least one resource while waiting for others |
| 3 | **No Preemption** | Resources cannot be forcibly taken away |
| 4 | **Circular Wait** | Circular chain of processes waiting for resources |

### Circular Wait Example

```
       ┌─────────────────┐
       │                 │
       ▼                 │
    ┌─────┐           ┌─────┐
    │ P1  │──────────►│ P2  │
    └─────┘  Waits    └─────┘
       ▲     for R2      │
       │                 │ Waits for R3
       │                 ▼
       │              ┌─────┐
       │              │ P3  │
       │              └─────┘
       │                 │
       │                 │ Waits for R1
       │                 │
       └─────────────────┘
       
P1 holds R1, waits for R2
P2 holds R2, waits for R3  
P3 holds R3, waits for R1
```

---

## Resource Allocation Graph

### Components

```
Process Node:     ○ (Circle)
Resource Node:    □ (Rectangle) with dots for instances

Request Edge:     P ────────► R (Process requests resource)
Assignment Edge:  R ────────► P (Resource assigned to process)
```

### Example Graph

```
     ┌─────────────┬─────────────┐
     │             │             │
     ▼             │             │
  ┌──────┐      ┌──┴──┐      ┌──┴──┐
  │  R1  │      │ P1  │      │ P2  │
  │  ●   │◄─────│     │      │     │
  └──────┘      └──┬──┘      └──┬──┘
                   │  Request    │ Request
                   │             │
                   ▼             ▼
                ┌──────┐     ┌──────┐
                │  R2  │     │  R3  │
                │  ●●  │     │  ●   │
                └──────┘     └──────┘
```

### Deadlock Detection from Graph

**Single Instance Resources:**
- Deadlock exists if and only if there is a **cycle** in the graph

**Multiple Instance Resources:**
- Cycle is necessary but not sufficient
- Need to check if processes can complete

### Example: Deadlock Detection

```
Graph with Cycle (Deadlock):

  ┌─────┐         ┌─────┐
  │ R1  │◄────────│ P1  │
  │  ●  │         │     │
  └──┬──┘         └──┬──┘
     │               │
     │ Assigned      │ Request
     ▼               │
  ┌─────┐            │
  │ P2  │────────────┘
  │     │ (P2 requests R1)
  └──┬──┘
     │ Holds
     ▼
  ┌─────┐
  │ R2  │
  │  ●  │◄───────────┐
  └─────┘            │
                     │ Request
                  ┌──┴──┐
                  │ P1  │
                  └─────┘

Cycle: P1 → R2 → P2 → R1 → P1
DEADLOCK EXISTS!
```

---

## Deadlock Prevention

### Strategy

**Break at least one of the four necessary conditions.**

### 1. Breaking Mutual Exclusion

- Make resources shareable where possible
- Example: Read-only files can be shared
- **Limitation:** Not always possible (e.g., printers)

### 2. Breaking Hold and Wait

**Method A:** Request all resources before starting
```
// Before execution
Request(R1, R2, R3)  // Request all at once
Execute()
Release(R1, R2, R3)
```

**Method B:** Release all before requesting new
```
Hold(R1)
Release(R1)
Request(R1, R2)  // Request both together
```

**Disadvantages:**
- Low resource utilization
- Starvation possible

### 3. Breaking No Preemption

If a process requests unavailable resource:
1. Release all currently held resources
2. Wait for all needed resources

```
P1 holds R1, requests R2 (unavailable):
   - R1 is preempted from P1
   - P1 waits for both R1 and R2
```

**Applicable for:** CPU registers, memory

### 4. Breaking Circular Wait

**Impose total ordering on resources:**

```
Resources ordered: R1 < R2 < R3 < R4

Rule: Process can only request resources in increasing order

Valid:   Request(R1) → Request(R3) → Request(R4)
Invalid: Request(R3) → Request(R1)  // R1 < R3, not allowed
```

---

## Deadlock Avoidance

### Concept

> **Deadlock Avoidance** ensures that the system will never enter an unsafe state by checking resource requests before granting them.

### Safe State

> A state is **safe** if the system can allocate resources to each process in some order and still avoid deadlock.

### Safe Sequence

A sequence of processes <P1, P2, ..., Pn> is safe if:
- For each Pi, the resources Pi needs can be satisfied by:
  - Currently available resources, plus
  - Resources held by all Pj, where j < i

### Safe vs Unsafe States

```
                    ┌─────────────────────────┐
                    │       ALL STATES        │
                    │                         │
                    │   ┌─────────────────┐   │
                    │   │   SAFE STATES   │   │
                    │   │                 │   │
                    │   │                 │   │
                    │   └─────────────────┘   │
                    │                         │
                    │   ┌─────────────────┐   │
                    │   │ UNSAFE STATES   │   │
                    │   │                 │   │
                    │   │ ┌───────────┐   │   │
                    │   │ │ DEADLOCK  │   │   │
                    │   │ └───────────┘   │   │
                    │   └─────────────────┘   │
                    └─────────────────────────┘

Safe State → Cannot lead to deadlock
Unsafe State → MAY lead to deadlock (not guaranteed)
```

---

## Banker's Algorithm

### Overview

The Banker's Algorithm is a deadlock avoidance algorithm named after the way bankers might handle loans.

### Data Structures

For n processes and m resource types:

| Structure | Size | Description |
|-----------|------|-------------|
| **Available** | m | Available instances of each resource |
| **Max** | n × m | Maximum demand of each process |
| **Allocation** | n × m | Currently allocated to each process |
| **Need** | n × m | Remaining need (Max - Allocation) |

### Safety Algorithm

```
1. Initialize:
   Work = Available
   Finish[i] = false for all i

2. Find an i such that:
   - Finish[i] = false
   - Need[i] ≤ Work

   If no such i exists, go to step 4

3. Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 2

4. If Finish[i] = true for all i:
   System is in SAFE state
   Else:
   System is in UNSAFE state
```

### Resource Request Algorithm

```
When process Pi requests resources:

1. If Request[i] > Need[i]:
   Error (exceeded maximum claim)

2. If Request[i] > Available:
   Pi must wait

3. Pretend to allocate:
   Available = Available - Request[i]
   Allocation[i] = Allocation[i] + Request[i]
   Need[i] = Need[i] - Request[i]

4. Run Safety Algorithm:
   If safe: Grant request
   Else: Restore state, make Pi wait
```

---

## Banker's Algorithm Examples

### Example 1: Safety Check

**Given:**

| Process | Allocation | Max | Need |
|---------|------------|-----|------|
| | A B C | A B C | A B C |
| P0 | 0 1 0 | 7 5 3 | 7 4 3 |
| P1 | 2 0 0 | 3 2 2 | 1 2 2 |
| P2 | 3 0 2 | 9 0 2 | 6 0 0 |
| P3 | 2 1 1 | 2 2 2 | 0 1 1 |
| P4 | 0 0 2 | 4 3 3 | 4 3 1 |

**Available:** A=3, B=3, C=2

**Solution:**

```
Step 1: Initialize
Work = [3, 3, 2]
Finish = [F, F, F, F, F]

Step 2: Find process where Need ≤ Work

Check P0: Need[7,4,3] ≤ Work[3,3,2]? NO
Check P1: Need[1,2,2] ≤ Work[3,3,2]? YES ✓

Allocate P1:
Work = [3,3,2] + [2,0,0] = [5,3,2]
Finish[1] = true

Check P2: Need[6,0,0] ≤ Work[5,3,2]? NO
Check P3: Need[0,1,1] ≤ Work[5,3,2]? YES ✓

Allocate P3:
Work = [5,3,2] + [2,1,1] = [7,4,3]
Finish[3] = true

Check P0: Need[7,4,3] ≤ Work[7,4,3]? YES ✓

Allocate P0:
Work = [7,4,3] + [0,1,0] = [7,5,3]
Finish[0] = true

Check P2: Need[6,0,0] ≤ Work[7,5,3]? YES ✓

Allocate P2:
Work = [7,5,3] + [3,0,2] = [10,5,5]
Finish[2] = true

Check P4: Need[4,3,1] ≤ Work[10,5,5]? YES ✓

Allocate P4:
Work = [10,5,5] + [0,0,2] = [10,5,7]
Finish[4] = true

All Finish[i] = true

SAFE STATE!
Safe Sequence: <P1, P3, P0, P2, P4>
```

---

### Example 2: Resource Request

**Using same data, P1 requests (1, 0, 2)**

**Solution:**

```
Step 1: Check if Request ≤ Need
Request[1,0,2] ≤ Need[1,2,2]? YES ✓

Step 2: Check if Request ≤ Available
Request[1,0,2] ≤ Available[3,3,2]? YES ✓

Step 3: Pretend allocation
Available = [3,3,2] - [1,0,2] = [2,3,0]
Allocation[P1] = [2,0,0] + [1,0,2] = [3,0,2]
Need[P1] = [1,2,2] - [1,0,2] = [0,2,0]

Step 4: Safety Algorithm with new state

Work = [2,3,0]

Check P0: Need[7,4,3] ≤ Work[2,3,0]? NO
Check P1: Need[0,2,0] ≤ Work[2,3,0]? YES ✓

Work = [2,3,0] + [3,0,2] = [5,3,2]

Check P2: Need[6,0,0] ≤ Work[5,3,2]? NO
Check P3: Need[0,1,1] ≤ Work[5,3,2]? YES ✓

Work = [5,3,2] + [2,1,1] = [7,4,3]

Check P0: Need[7,4,3] ≤ Work[7,4,3]? YES ✓
Work = [7,5,3]

Check P2: Need[6,0,0] ≤ Work[7,5,3]? YES ✓
Work = [10,5,5]

Check P4: Need[4,3,1] ≤ Work[10,5,5]? YES ✓
Work = [10,5,7]

All processes can finish.

REQUEST GRANTED!
New Safe Sequence: <P1, P3, P0, P2, P4>
```

---

### Example 3: Request Denial

**P4 requests (3, 3, 0)**

**Solution:**

```
Step 1: Check if Request ≤ Need
Request[3,3,0] ≤ Need[4,3,1]? YES ✓

Step 2: Check if Request ≤ Available
Request[3,3,0] ≤ Available[3,3,2]? YES ✓

Step 3: Pretend allocation
Available = [3,3,2] - [3,3,0] = [0,0,2]
Allocation[P4] = [0,0,2] + [3,3,0] = [3,3,2]
Need[P4] = [4,3,1] - [3,3,0] = [1,0,1]

Step 4: Safety Algorithm

Work = [0,0,2]

Check all processes:
P0: Need[7,4,3] ≤ [0,0,2]? NO
P1: Need[1,2,2] ≤ [0,0,2]? NO
P2: Need[6,0,0] ≤ [0,0,2]? NO
P3: Need[0,1,1] ≤ [0,0,2]? NO
P4: Need[1,0,1] ≤ [0,0,2]? NO

No process can proceed!

UNSAFE STATE - REQUEST DENIED!
P4 must wait.
```

---

## Deadlock Detection

### When Avoidance is Not Used

If the system doesn't use prevention or avoidance:
1. Allow deadlock to happen
2. Detect it
3. Recover from it

### Detection Algorithm (Single Instance)

Use Wait-For Graph:

```
Resource Allocation Graph:     Wait-For Graph:
                               
    P1 ──► R1 ──► P2           P1 ──────────► P2
                                     │
    P2 ──► R2 ──► P1           P2 ──┘─────────► P1

Cycle in Wait-For Graph = Deadlock
```

### Detection Algorithm (Multiple Instances)

Similar to Banker's safety algorithm:

```
1. Initialize:
   Work = Available
   If Allocation[i] ≠ 0, then Finish[i] = false
   Else Finish[i] = true

2. Find i where:
   Finish[i] = false AND Request[i] ≤ Work
   
   If none found, go to step 4

3. Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 2

4. If Finish[i] = false for some i:
   Process i is deadlocked
```

---

## Deadlock Recovery

### Methods

#### 1. Process Termination

**Option A:** Abort ALL deadlocked processes
- Simple but costly
- Loses all work done

**Option B:** Abort ONE process at a time
- Check if deadlock resolved after each abort
- Choose victim based on:
  - Process priority
  - Computation done so far
  - Resources held
  - Resources needed to complete

#### 2. Resource Preemption

Steps:
1. **Select victim:** Choose process to preempt
2. **Rollback:** Return process to safe state
3. **Starvation prevention:** Limit number of times a process can be victim

```
Preemption example:

Before:                    After:
P1 holds R1, R2            P1 holds R1
P2 holds R3, waits R1      P2 holds R3, R2 (preempted from P1)
                           P1 must rollback and retry
```

---

## Numerical Problems

### Problem 1: Safe State Check

**Given:**
- 5 processes: P0, P1, P2, P3, P4
- 3 resource types: A(10), B(5), C(7) total
- Current state:

| Process | Allocation | Max |
|---------|------------|-----|
| | A B C | A B C |
| P0 | 0 1 0 | 7 5 3 |
| P1 | 2 0 0 | 3 2 2 |
| P2 | 3 0 2 | 9 0 2 |
| P3 | 2 1 1 | 2 2 2 |
| P4 | 0 0 2 | 4 3 3 |

Find if system is in safe state.

**Solution:**

```
Step 1: Calculate Need = Max - Allocation

| Process | Need |
|---------|------|
| P0 | 7 4 3 |
| P1 | 1 2 2 |
| P2 | 6 0 0 |
| P3 | 0 1 1 |
| P4 | 4 3 1 |

Step 2: Calculate Available
Total = [10, 5, 7]
Allocated = [0+2+3+2+0, 1+0+0+1+0, 0+0+2+1+2] = [7, 2, 5]
Available = [10-7, 5-2, 7-5] = [3, 3, 2]

Step 3: Apply Safety Algorithm
Work = [3, 3, 2]

Find P where Need ≤ Work:
P1: [1,2,2] ≤ [3,3,2]? YES
Work = [3,3,2] + [2,0,0] = [5,3,2]

P3: [0,1,1] ≤ [5,3,2]? YES
Work = [5,3,2] + [2,1,1] = [7,4,3]

P4: [4,3,1] ≤ [7,4,3]? YES
Work = [7,4,3] + [0,0,2] = [7,4,5]

P0: [7,4,3] ≤ [7,4,5]? YES
Work = [7,4,5] + [0,1,0] = [7,5,5]

P2: [6,0,0] ≤ [7,5,5]? YES
Work = [7,5,5] + [3,0,2] = [10,5,7]

SAFE STATE
Safe Sequence: <P1, P3, P4, P0, P2>
```

---

### Problem 2: Resource Request

**From Problem 1, P1 requests (1, 0, 2). Should it be granted?**

**Solution:**

```
Step 1: Request[1,0,2] ≤ Need[1,2,2]? 
        [1≤1, 0≤2, 2≤2] YES ✓

Step 2: Request[1,0,2] ≤ Available[3,3,2]?
        [1≤3, 0≤3, 2≤2] YES ✓

Step 3: Pretend allocation
New Available = [3-1, 3-0, 2-2] = [2, 3, 0]
New Allocation[P1] = [2+1, 0+0, 0+2] = [3, 0, 2]
New Need[P1] = [1-1, 2-0, 2-2] = [0, 2, 0]

Step 4: Safety Check with new state
Work = [2, 3, 0]

P1: [0,2,0] ≤ [2,3,0]? YES
Work = [2,3,0] + [3,0,2] = [5,3,2]

Continue... (all processes can complete)

REQUEST GRANTED ✓
```

---

### Problem 3: Finding Minimum Resources

**Given 3 processes each needing maximum 2 resources with single resource type. What is minimum resources to guarantee no deadlock?**

**Solution:**

```
Using formula:
Minimum Resources = (Max - 1) × n + 1

Where n = number of processes, Max = maximum need per process

Minimum = (2 - 1) × 3 + 1
        = 1 × 3 + 1
        = 4 resources

Explanation:
- Worst case: Each process holds (Max - 1) = 1 resource
- All 3 processes hold 1 each = 3 resources, all waiting
- One more resource allows any process to complete
- So minimum = 3 + 1 = 4 resources
```

---

### Problem 4: Deadlock Detection

**Given:**

| Process | Allocation | Request |
|---------|------------|---------|
| | A B C | A B C |
| P0 | 0 1 0 | 0 0 0 |
| P1 | 2 0 0 | 2 0 2 |
| P2 | 3 0 3 | 0 0 0 |
| P3 | 2 1 1 | 1 0 0 |
| P4 | 0 0 2 | 0 0 2 |

**Available:** [0, 0, 0]

**Is the system deadlocked?**

**Solution:**

```
Step 1: Find processes with Allocation = 0 or Request = 0
P0: Request = [0,0,0], mark as finished
P2: Request = [0,0,0], mark as finished

Step 2: Work = Available + Allocation of finished
Work = [0,0,0] + [0,1,0] + [3,0,3] = [3,1,3]

Step 3: Check remaining processes
P1: Request[2,0,2] ≤ Work[3,1,3]? YES
Work = [3,1,3] + [2,0,0] = [5,1,3]

P3: Request[1,0,0] ≤ Work[5,1,3]? YES
Work = [5,1,3] + [2,1,1] = [7,2,4]

P4: Request[0,0,2] ≤ Work[7,2,4]? YES
Work = [7,2,4] + [0,0,2] = [7,2,6]

All processes can finish.
NO DEADLOCK ✓
```

---

## Formula Sheet

```
┌────────────────────────────────────────────────────────────────────────────┐
│                           DEADLOCK FORMULAS                                │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│ BASIC CALCULATIONS                                                         │
│ ──────────────────                                                         │
│                                                                            │
│ Need = Max - Allocation                                                    │
│                                                                            │
│ Available = Total - Σ(Allocation)                                          │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│ DEADLOCK-FREE MINIMUM RESOURCES                                            │
│ ────────────────────────────────                                           │
│                                                                            │
│ For n processes, each needs maximum R resources:                           │
│                                                                            │
│ Minimum = n × (R - 1) + 1                                                  │
│                                                                            │
│ For different maximum needs (R1, R2, ...Rn):                               │
│                                                                            │
│ Minimum = Σ(Ri - 1) + 1 = Σ(Ri) - n + 1                                   │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│ SAFETY CONDITION                                                           │
│ ────────────────                                                           │
│                                                                            │
│ Safe if: ∃ sequence <P1...Pn> where each Pi can be satisfied by:          │
│          Available + Σ(Allocation[Pj]) for all j < i                       │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│ REQUEST GRANT CONDITIONS                                                   │
│ ────────────────────────                                                   │
│                                                                            │
│ 1. Request ≤ Need                                                          │
│ 2. Request ≤ Available                                                     │
│ 3. Resulting state is safe                                                 │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Summary

- Deadlock requires 4 conditions: Mutual Exclusion, Hold & Wait, No Preemption, Circular Wait
- Prevention: Break one of the four conditions
- Avoidance: Never enter unsafe state (Banker's Algorithm)
- Detection: Find cycles (single instance) or use detection algorithm
- Recovery: Terminate processes or preempt resources

---

[← Previous: Virtual Memory](06-virtual-memory.md) | [Back to Home →](../index.md)
