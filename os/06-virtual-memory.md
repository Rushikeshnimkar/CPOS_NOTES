---
layout: default
title: Virtual Memory
---

# Virtual Memory

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to Virtual Memory](#introduction-to-virtual-memory)
- [Demand Paging](#demand-paging)
- [Page Fault Handling](#page-fault-handling)
- [Page Replacement Algorithms](#page-replacement-algorithms)
- [Thrashing](#thrashing)
- [Working Set Model](#working-set-model)
- [Memory-Mapped Files](#memory-mapped-files)
- [Numerical Problems](#numerical-problems)

---

## Introduction to Virtual Memory

### What is Virtual Memory?

> **Virtual Memory** is a memory management technique that provides an "idealized abstraction of the storage resources that are actually available on a given machine" which creates the illusion of a very large memory to users.

### Benefits of Virtual Memory

| Benefit | Description |
|---------|-------------|
| **Larger Address Space** | Programs can be larger than physical memory |
| **More Processes** | More programs can run simultaneously |
| **Simple Programming** | Programmers don't worry about physical limits |
| **Memory Sharing** | Efficient sharing of code pages |
| **Protection** | Isolation between processes |

### Virtual Address Space

```
Virtual Memory                Physical Memory           Disk
┌──────────────┐             ┌──────────────┐      ┌──────────────┐
│   Page 0     │────────────►│   Frame 2    │      │              │
├──────────────┤             ├──────────────┤      │              │
│   Page 1     │──────────┐  │   Frame 1    │      │              │
├──────────────┤          │  ├──────────────┤      ├──────────────┤
│   Page 2     │────────┐ └─►│   Frame 5    │      │   Page 3     │◄─┐
├──────────────┤        │    ├──────────────┤      ├──────────────┤  │
│   Page 3     │────────┼───►│              │──────│              │  │
├──────────────┤        │    ├──────────────┤      └──────────────┘  │
│   Page 4     │────────┼───►│   Frame 3    │                        │
└──────────────┘        │    ├──────────────┤                        │
                        └───►│   Frame 0    │     (Swapped out) ─────┘
                             └──────────────┘
```

---

## Demand Paging

### Concept

> **Demand Paging** is a technique where pages are loaded into memory only when they are needed (on demand), not in advance.

### How It Works

1. Process starts with no pages in memory
2. When a page is referenced, check if it's in memory
3. If present (valid) → access normally
4. If not present (invalid) → page fault → load from disk

### Valid-Invalid Bit

```
Page Table:
┌────────┬───────┬────────────────┐
│  Page  │ Frame │ Valid/Invalid  │
├────────┼───────┼────────────────┤
│   0    │   5   │       V        │  ← In memory
│   1    │   3   │       V        │  ← In memory
│   2    │   -   │       I        │  ← Not in memory
│   3    │   7   │       V        │  ← In memory
│   4    │   -   │       I        │  ← Not in memory
└────────┴───────┴────────────────┘
```

### Advantages

- Faster program startup
- Less memory usage
- More programs can run

### Disadvantages

- Page faults cause delays
- Disk I/O overhead
- Complex implementation

---

## Page Fault Handling

### Page Fault

> A **Page Fault** occurs when a program accesses a page that is not currently in physical memory.

### Page Fault Handling Steps

```
1. CPU generates page reference
            │
            ▼
2. Check page table (Valid/Invalid bit)
            │
    ┌───────┴───────┐
    │               │
    ▼               ▼
  Valid           Invalid
    │               │
    ▼               ▼
3. Access        4. PAGE FAULT
   Memory            │
                     ▼
            5. Trap to OS
                     │
                     ▼
            6. Find page on disk
                     │
                     ▼
            7. Find free frame
               (or page replacement)
                     │
                     ▼
            8. Load page into frame
                     │
                     ▼
            9. Update page table
               (set valid bit)
                     │
                     ▼
            10. Restart instruction
```

### Effective Access Time with Page Faults

```
EAT = (1 - p) × memory_access_time + p × page_fault_time

Where:
- p = probability of page fault
- page_fault_time includes:
  - Service interrupt
  - Read page from disk
  - Restart process
```

### Example Calculation

```
Given:
- Memory access time = 200 ns
- Page fault service time = 8 ms = 8,000,000 ns
- Page fault rate = 1 in 1000 references (p = 0.001)

EAT = (1 - 0.001) × 200 + 0.001 × 8,000,000
    = 0.999 × 200 + 0.001 × 8,000,000
    = 199.8 + 8,000
    = 8,199.8 ns

Slowdown = 8,199.8 / 200 ≈ 41 times slower
```

---

## Page Replacement Algorithms

When memory is full and a new page is needed:
1. Select a victim page to remove
2. Write victim to disk if modified (dirty)
3. Load new page into freed frame
4. Update page tables

### 1. FIFO (First-In, First-Out)

**Concept:** Replace the page that has been in memory the longest.

**Example:**
```
Reference String: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1
Frames: 3

Step-by-step:
┌─────┬─────────────┬────────┐
│ Ref │   Frames    │ Fault? │
├─────┼─────────────┼────────┤
│  7  │ [7, -, -]   │   F    │
│  0  │ [7, 0, -]   │   F    │
│  1  │ [7, 0, 1]   │   F    │
│  2  │ [2, 0, 1]   │   F    │ ← 7 out (oldest)
│  0  │ [2, 0, 1]   │        │ ← Hit
│  3  │ [2, 3, 1]   │   F    │ ← 0 out
│  0  │ [2, 3, 0]   │   F    │ ← 1 out
│  4  │ [4, 3, 0]   │   F    │ ← 2 out
│  2  │ [4, 2, 0]   │   F    │ ← 3 out
│  3  │ [4, 2, 3]   │   F    │ ← 0 out
│  0  │ [0, 2, 3]   │   F    │ ← 4 out
│  3  │ [0, 2, 3]   │        │ ← Hit
│  2  │ [0, 2, 3]   │        │ ← Hit
│  1  │ [0, 1, 3]   │   F    │ ← 2 out
│  2  │ [0, 1, 2]   │   F    │ ← 3 out
│  0  │ [0, 1, 2]   │        │ ← Hit
│  1  │ [0, 1, 2]   │        │ ← Hit
│  7  │ [7, 1, 2]   │   F    │ ← 0 out
│  0  │ [7, 0, 2]   │   F    │ ← 1 out
│  1  │ [7, 0, 1]   │   F    │ ← 2 out
└─────┴─────────────┴────────┘

Total Page Faults: 15
```

**Belady's Anomaly:** FIFO can have MORE page faults with MORE frames!

---

### 2. Optimal (OPT)

**Concept:** Replace the page that will not be used for the longest time in the future.

**Example (Same reference string, 3 frames):**
```
Reference String: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

Step-by-step:
┌─────┬─────────────┬────────┬─────────────────────────────────┐
│ Ref │   Frames    │ Fault? │ Decision                        │
├─────┼─────────────┼────────┼─────────────────────────────────┤
│  7  │ [7, -, -]   │   F    │                                 │
│  0  │ [7, 0, -]   │   F    │                                 │
│  1  │ [7, 0, 1]   │   F    │                                 │
│  2  │ [2, 0, 1]   │   F    │ 7 not needed again for longest  │
│  0  │ [2, 0, 1]   │        │                                 │
│  3  │ [2, 0, 3]   │   F    │ 1 needed farthest at pos 13     │
│  0  │ [2, 0, 3]   │        │                                 │
│  4  │ [2, 0, 4]   │   F    │ 3 needed at 9, replace          │
│  2  │ [2, 0, 4]   │        │                                 │
│  3  │ [2, 3, 4]   │   F    │ 0 at pos 10, replace            │
│  0  │ [2, 3, 0]   │   F    │ 4 not needed again              │
│  3  │ [2, 3, 0]   │        │                                 │
│  2  │ [2, 3, 0]   │        │                                 │
│  1  │ [1, 3, 0]   │   F    │ 2 at 14, farthest               │
│  2  │ [1, 2, 0]   │   F    │ 3 not needed again              │
│  0  │ [1, 2, 0]   │        │                                 │
│  1  │ [1, 2, 0]   │        │                                 │
│  7  │ [1, 7, 0]   │   F    │ 2 not needed again              │
│  0  │ [1, 7, 0]   │        │                                 │
│  1  │ [1, 7, 0]   │        │                                 │
└─────┴─────────────┴────────┴─────────────────────────────────┘

Total Page Faults: 9 (Minimum possible)
```

**Note:** Optimal is theoretical (requires future knowledge), used as benchmark.

---

### 3. LRU (Least Recently Used)

**Concept:** Replace the page that has not been used for the longest time.

**Example (Same reference string, 3 frames):**
```
Reference String: 7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1

Step-by-step:
┌─────┬─────────────┬────────┬─────────────────────────────────┐
│ Ref │   Frames    │ Fault? │ LRU Order (most→least recent)   │
├─────┼─────────────┼────────┼─────────────────────────────────┤
│  7  │ [7, -, -]   │   F    │ 7                               │
│  0  │ [7, 0, -]   │   F    │ 0, 7                            │
│  1  │ [7, 0, 1]   │   F    │ 1, 0, 7                         │
│  2  │ [2, 0, 1]   │   F    │ 2, 1, 0 (7 LRU, replaced)       │
│  0  │ [2, 0, 1]   │        │ 0, 2, 1                         │
│  3  │ [2, 0, 3]   │   F    │ 3, 0, 2 (1 LRU, replaced)       │
│  0  │ [2, 0, 3]   │        │ 0, 3, 2                         │
│  4  │ [4, 0, 3]   │   F    │ 4, 0, 3 (2 LRU, replaced)       │
│  2  │ [4, 0, 2]   │   F    │ 2, 4, 0 (3 LRU, replaced)       │
│  3  │ [4, 3, 2]   │   F    │ 3, 2, 4 (0 LRU, replaced)       │
│  0  │ [0, 3, 2]   │   F    │ 0, 3, 2 (4 LRU, replaced)       │
│  3  │ [0, 3, 2]   │        │ 3, 0, 2                         │
│  2  │ [0, 3, 2]   │        │ 2, 3, 0                         │
│  1  │ [1, 3, 2]   │   F    │ 1, 2, 3 (0 LRU, replaced)       │
│  2  │ [1, 3, 2]   │        │ 2, 1, 3                         │
│  0  │ [1, 0, 2]   │   F    │ 0, 2, 1 (3 LRU, replaced)       │
│  1  │ [1, 0, 2]   │        │ 1, 0, 2                         │
│  7  │ [1, 0, 7]   │   F    │ 7, 1, 0 (2 LRU, replaced)       │
│  0  │ [1, 0, 7]   │        │ 0, 7, 1                         │
│  1  │ [1, 0, 7]   │        │ 1, 0, 7                         │
└─────┴─────────────┴────────┴─────────────────────────────────┘

Total Page Faults: 12
```

### LRU Implementation Methods

#### Counter Implementation
- Each page entry has a counter
- Updated on every access with clock value
- Replace page with smallest counter

#### Stack Implementation
- Keep a stack of page numbers
- On access, move page to top
- Bottom of stack = LRU

---

### 4. LRU Approximation Algorithms

#### Second Chance (Clock Algorithm)

```
Circular queue with reference bit:

Initial state:          After victim selection:
  ↓ (clock hand)            ↓ (advanced)
┌───┬───┐              ┌───┬───┐
│ A │ 1 │              │ A │ 0 │ ← bit cleared
├───┼───┤              ├───┼───┤
│ B │ 1 │              │ B │ 0 │ ← bit cleared
├───┼───┤              ├───┼───┤
│ C │ 0 │ ← Victim     │ X │ 1 │ ← new page
├───┼───┤              ├───┼───┤
│ D │ 1 │              │ D │ 1 │
└───┴───┘              └───┴───┘

Algorithm:
1. Check reference bit at clock hand
2. If bit = 1: clear bit, advance hand
3. If bit = 0: select as victim
```

#### Enhanced Second Chance

Uses both reference bit (R) and modify bit (M):

| Class | (R, M) | Priority |
|-------|--------|----------|
| 0 | (0, 0) | Best victim (not used, not modified) |
| 1 | (0, 1) | Not used, but modified |
| 2 | (1, 0) | Recently used, clean |
| 3 | (1, 1) | Worst victim (used and modified) |

---

### Algorithm Comparison

| Algorithm | Page Faults (Example) | Time Complexity | Space | Notes |
|-----------|----------------------|-----------------|-------|-------|
| FIFO | 15 | O(1) | O(n) | Belady's anomaly |
| Optimal | 9 | - | - | Theoretical only |
| LRU | 12 | O(n) or O(log n) | O(n) | Good approximation |
| Clock | ~LRU | O(1) amortized | O(n) | Practical |

---

## Thrashing

### What is Thrashing?

> **Thrashing** occurs when a system spends more time swapping pages than executing processes, causing severe performance degradation.

### Thrashing Scenario

```
CPU Utilization vs Degree of Multiprogramming:

CPU
Util.
  │
  │         ╭────╮
  │       ╱      ╲
  │     ╱          ╲ ← Thrashing begins
  │   ╱              ╲
  │ ╱                  ╲
  │╱                     ╲_____
  └─────────────────────────────► Degree of
                                  Multiprogramming
```

### Causes of Thrashing

1. **Too many processes** competing for limited frames
2. **Insufficient physical memory** for working sets
3. **Poor page replacement** decisions

### Prevention Methods

| Method | Description |
|--------|-------------|
| **Working Set Model** | Keep only active pages in memory |
| **Page Fault Frequency** | Adjust allocation based on fault rate |
| **Local Replacement** | Replace only within process's frames |
| **Process Suspension** | Swap out entire processes |

---

## Working Set Model

### Concept

> The **Working Set** of a process is the set of pages that the process is actively using at a given time.

### Working Set Window (Δ)

```
Reference String with Δ = 10:
... 2, 6, 1, 5, 7, 7, 7, 7, 5, 1, ...
    └───────────────────────────┘
           Working Set Window

Working Set = {1, 2, 5, 6, 7}
Working Set Size (WSS) = 5
```

### Working Set Model Properties

- **Δ too small:** Won't encompass entire locality
- **Δ too large:** May include multiple localities
- **Δ = ∞:** Working set = all pages ever referenced

### Implementation

```
Total Demand (D) = Σ WSS_i for all processes

If D > Total Frames available:
    Thrashing will occur
    Suspend one or more processes

If D < Total Frames:
    System running efficiently
    Can add more processes
```

---

## Memory-Mapped Files

### Concept

Map a file directly into virtual address space, allowing file access through memory operations.

```
Virtual Address Space          File on Disk
┌──────────────────┐          ┌──────────────────┐
│                  │          │                  │
│   Mapped Region  │◄────────►│   File Data      │
│                  │  mmap()  │                  │
└──────────────────┘          └──────────────────┘
```

### Benefits

- Simplified file I/O
- Shared memory between processes
- Lazy loading of file contents

---

## Numerical Problems

### Problem 1: Page Fault Calculation

**Given:**
Reference String: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5
Frames: 3

Compare page faults for FIFO, LRU, and Optimal.

**Solution:**

```
FIFO:
┌─────┬─────────────┬────────┐
│ Ref │   Frames    │ Fault  │
├─────┼─────────────┼────────┤
│  1  │ [1, -, -]   │   F    │
│  2  │ [1, 2, -]   │   F    │
│  3  │ [1, 2, 3]   │   F    │
│  4  │ [4, 2, 3]   │   F    │
│  1  │ [4, 1, 3]   │   F    │
│  2  │ [4, 1, 2]   │   F    │
│  5  │ [5, 1, 2]   │   F    │
│  1  │ [5, 1, 2]   │        │
│  2  │ [5, 1, 2]   │        │
│  3  │ [3, 1, 2]   │   F    │
│  4  │ [3, 4, 2]   │   F    │
│  5  │ [3, 4, 5]   │   F    │
└─────┴─────────────┴────────┘
FIFO Page Faults: 10

LRU:
┌─────┬─────────────┬────────┐
│ Ref │   Frames    │ Fault  │
├─────┼─────────────┼────────┤
│  1  │ [1, -, -]   │   F    │
│  2  │ [1, 2, -]   │   F    │
│  3  │ [1, 2, 3]   │   F    │
│  4  │ [4, 2, 3]   │   F    │
│  1  │ [4, 1, 3]   │   F    │
│  2  │ [4, 1, 2]   │   F    │
│  5  │ [5, 1, 2]   │   F    │
│  1  │ [5, 1, 2]   │        │
│  2  │ [5, 1, 2]   │        │
│  3  │ [3, 1, 2]   │   F    │
│  4  │ [3, 4, 2]   │   F    │
│  5  │ [3, 4, 5]   │   F    │
└─────┴─────────────┴────────┘
LRU Page Faults: 10

Optimal:
┌─────┬─────────────┬────────┐
│ Ref │   Frames    │ Fault  │
├─────┼─────────────┼────────┤
│  1  │ [1, -, -]   │   F    │
│  2  │ [1, 2, -]   │   F    │
│  3  │ [1, 2, 3]   │   F    │
│  4  │ [1, 2, 4]   │   F    │ (3 used farthest)
│  1  │ [1, 2, 4]   │        │
│  2  │ [1, 2, 4]   │        │
│  5  │ [1, 2, 5]   │   F    │ (4 not used again)
│  1  │ [1, 2, 5]   │        │
│  2  │ [1, 2, 5]   │        │
│  3  │ [1, 2, 3]   │   F    │ (5 used later)
│  4  │ [4, 2, 3]   │   F    │ (1 not used again)
│  5  │ [4, 5, 3]   │   F    │ (2 not used again)
└─────┴─────────────┴────────┘
Optimal Page Faults: 8

Summary:
- FIFO: 10 faults
- LRU: 10 faults
- Optimal: 8 faults
```

---

### Problem 2: Effective Access Time

**Given:**
- Memory access time = 100 ns
- Page fault service time = 25 ms
- Desired EAT ≤ 110 ns

Find maximum acceptable page fault rate.

**Solution:**

```
EAT = (1 - p) × 100 + p × 25,000,000

For EAT ≤ 110:
    (1 - p) × 100 + p × 25,000,000 ≤ 110
    100 - 100p + 25,000,000p ≤ 110
    24,999,900p ≤ 10
    p ≤ 10 / 24,999,900
    p ≤ 0.0000004 (approximately)
    p ≤ 4 × 10^-7

Maximum page fault rate: 1 fault per 2.5 million references
```

---

### Problem 3: Working Set Size

**Given:**
Reference String (last 10 references): 1, 2, 3, 2, 7, 1, 0, 1, 2, 3
Window size Δ = 5

Find working set at different time points.

**Solution:**

```
At t=5 (references 1-5): 1, 2, 3, 2, 7
Working Set = {1, 2, 3, 7}
WSS = 4

At t=6 (references 2-6): 2, 3, 2, 7, 1
Working Set = {1, 2, 3, 7}
WSS = 4

At t=7 (references 3-7): 3, 2, 7, 1, 0
Working Set = {0, 1, 2, 3, 7}
WSS = 5

At t=8 (references 4-8): 2, 7, 1, 0, 1
Working Set = {0, 1, 2, 7}
WSS = 4

At t=9 (references 5-9): 7, 1, 0, 1, 2
Working Set = {0, 1, 2, 7}
WSS = 4

At t=10 (references 6-10): 1, 0, 1, 2, 3
Working Set = {0, 1, 2, 3}
WSS = 4
```

---

### Problem 4: Belady's Anomaly

**Show Belady's Anomaly with reference string: 1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5**

**Solution:**

```
With 3 Frames (FIFO):
Page Faults = 9

With 4 Frames (FIFO):
┌─────┬───────────────┬────────┐
│ Ref │    Frames     │ Fault  │
├─────┼───────────────┼────────┤
│  1  │ [1, -, -, -]  │   F    │
│  2  │ [1, 2, -, -]  │   F    │
│  3  │ [1, 2, 3, -]  │   F    │
│  4  │ [1, 2, 3, 4]  │   F    │
│  1  │ [1, 2, 3, 4]  │        │
│  2  │ [1, 2, 3, 4]  │        │
│  5  │ [5, 2, 3, 4]  │   F    │
│  1  │ [5, 1, 3, 4]  │   F    │
│  2  │ [5, 1, 2, 4]  │   F    │
│  3  │ [5, 1, 2, 3]  │   F    │
│  4  │ [4, 1, 2, 3]  │   F    │
│  5  │ [4, 5, 2, 3]  │   F    │
└─────┴───────────────┴────────┘
Page Faults = 10

Conclusion: 4 frames → 10 faults > 3 frames → 9 faults
This is Belady's Anomaly!
```

---

## Formula Sheet

```
┌────────────────────────────────────────────────────────────────────────────┐
│                        VIRTUAL MEMORY FORMULAS                             │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│ EFFECTIVE ACCESS TIME (EAT)                                                │
│ ───────────────────────────                                                │
│                                                                            │
│ EAT = (1 - p) × memory_time + p × page_fault_time                         │
│                                                                            │
│ Where:                                                                     │
│   p = page fault rate (probability)                                        │
│   memory_time = main memory access time                                    │
│   page_fault_time = time to handle page fault                             │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│ PAGE FAULT RATE                                                            │
│ ───────────────                                                            │
│                                                                            │
│ Page Fault Rate = Number of Page Faults / Total References                 │
│                                                                            │
│ Hit Ratio = 1 - Page Fault Rate                                            │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│ WORKING SET                                                                │
│ ───────────                                                                │
│                                                                            │
│ WSS(t, Δ) = pages referenced in interval (t - Δ, t)                        │
│                                                                            │
│ Total Demand D = Σ WSS_i                                                   │
│                                                                            │
│ If D > m (available frames): thrashing                                     │
│                                                                            │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│ PAGE FAULT FREQUENCY                                                       │
│ ────────────────────                                                       │
│                                                                            │
│ If fault rate > upper bound: allocate more frames                         │
│ If fault rate < lower bound: deallocate frames                            │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Summary

- Virtual memory allows programs larger than physical memory
- Demand paging loads pages only when needed
- Page faults trigger loading from disk
- Page replacement algorithms: FIFO, Optimal, LRU
- Thrashing occurs when too many processes compete for memory
- Working set model prevents thrashing
- Belady's anomaly: more frames can cause more faults (FIFO)

---

[← Previous: Memory Management](05-memory-management.md) | [Next: Deadlock →](07-deadlock.md)
