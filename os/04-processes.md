---
layout: default
title: Processes
---

# Processes

[← Back to Home](../index.md)

---

## Table of Contents
- [Process Concept](#process-concept)
- [Process States](#process-states)
- [Process Control Block (PCB)](#process-control-block-pcb)
- [Process Operations](#process-operations)
- [Process Scheduling](#process-scheduling)
- [Scheduling Algorithms](#scheduling-algorithms)
- [Inter-Process Communication (IPC)](#inter-process-communication-ipc)
- [Context Switching](#context-switching)
- [Threads](#threads)

---

## Process Concept

### What is a Process?

> A **Process** is a program in execution. It is an active entity that includes the program code, current activity, and resources allocated to it.

### Program vs Process

| Aspect | Program | Process |
|--------|---------|---------|
| Nature | Passive (stored on disk) | Active (running in memory) |
| Resources | None | CPU, memory, I/O, files |
| State | Static | Dynamic (running, waiting, etc.) |
| Existence | Permanent until deleted | Temporary (lifetime of execution) |

### Process Memory Layout

```
High Address ┌─────────────────────┐
             │       Stack         │ ← Local variables, function calls
             │         ↓           │
             ├─────────────────────┤
             │         ↑           │
             │        Heap         │ ← Dynamic memory allocation
             ├─────────────────────┤
             │        BSS          │ ← Uninitialized global data
             ├─────────────────────┤
             │        Data         │ ← Initialized global data
             ├─────────────────────┤
             │        Text         │ ← Program code (read-only)
Low Address  └─────────────────────┘
```

### Memory Sections

| Section | Description | Example |
|---------|-------------|---------|
| **Text** | Executable code | Functions, instructions |
| **Data** | Initialized global/static variables | `int x = 10;` |
| **BSS** | Uninitialized global/static variables | `int y;` |
| **Heap** | Dynamically allocated memory | `malloc()`, `new` |
| **Stack** | Local variables, function calls | Parameters, return addresses |

---

## Process States

### Five-State Model

```
                    ┌──────────────┐
          Admit     │     New      │
           │        └──────┬───────┘
           │               │
           ▼               ▼
    ┌──────────────┐   Dispatch   ┌──────────────┐
    │    Ready     │─────────────►│   Running    │
    │    Queue     │◄─────────────│              │
    └──────┬───────┘  Preempt/    └──────┬───────┘
           │          Timeout            │
           │                             │ I/O Wait
           │    ┌──────────────┐         │
           │    │   Waiting    │◄────────┘
           │    │   (Blocked)  │
           │    └──────┬───────┘
           │           │ I/O Complete
           │◄──────────┘
           │
           │        ┌──────────────┐
           └───────►│  Terminated  │
                    └──────────────┘
```

### State Descriptions

| State | Description |
|-------|-------------|
| **New** | Process is being created |
| **Ready** | Process waiting to be assigned to CPU |
| **Running** | Instructions are being executed |
| **Waiting/Blocked** | Process waiting for I/O or event |
| **Terminated** | Process has finished execution |

### State Transitions

| Transition | Description |
|------------|-------------|
| New → Ready | Process admitted to ready queue |
| Ready → Running | Scheduler dispatches process |
| Running → Ready | Preemption or time quantum expired |
| Running → Waiting | Process requests I/O |
| Waiting → Ready | I/O completed |
| Running → Terminated | Process completes or exits |

---

## Process Control Block (PCB)

### Definition

> The **Process Control Block (PCB)** is a data structure maintained by the OS for every process. It contains all information needed to manage the process.

### PCB Structure

```
┌─────────────────────────────────┐
│    Process Control Block (PCB)  │
├─────────────────────────────────┤
│  Process ID (PID)               │
├─────────────────────────────────┤
│  Process State                  │
├─────────────────────────────────┤
│  Program Counter                │
├─────────────────────────────────┤
│  CPU Registers                  │
├─────────────────────────────────┤
│  CPU Scheduling Information     │
│  (Priority, pointers, etc.)     │
├─────────────────────────────────┤
│  Memory Management Information  │
│  (Page tables, segment tables)  │
├─────────────────────────────────┤
│  I/O Status Information         │
│  (Open files, devices)          │
├─────────────────────────────────┤
│  Accounting Information         │
│  (CPU time, time limits)        │
└─────────────────────────────────┘
```

### PCB Components

| Component | Description |
|-----------|-------------|
| **Process ID** | Unique identifier |
| **Process State** | Current state (Ready, Running, etc.) |
| **Program Counter** | Address of next instruction |
| **CPU Registers** | Register contents |
| **Scheduling Info** | Priority, queue pointers |
| **Memory Info** | Base/limit registers, page tables |
| **I/O Status** | List of open files, I/O devices |
| **Accounting** | CPU time used, time limits |

---

## Process Operations

### Process Creation

**Reasons for process creation:**
- System initialization
- User request
- Process spawning another process

**fork() System Call**

```c
#include <unistd.h>
#include <stdio.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        // Error occurred
        printf("Fork failed\n");
    } else if (pid == 0) {
        // Child process
        printf("Child: PID = %d, Parent PID = %d\n", getpid(), getppid());
    } else {
        // Parent process
        printf("Parent: PID = %d, Child PID = %d\n", getpid(), pid);
    }
    
    return 0;
}
```

### Parent-Child Relationship

```
                Parent Process
                    (fork)
                      │
         ┌────────────┴────────────┐
         │                         │
    Parent continues          Child Process
    (fork returns child_pid)  (fork returns 0)
```

### Process Termination

**Reasons for termination:**
- Normal exit (voluntary)
- Error exit (voluntary)
- Fatal error (involuntary)
- Killed by another process (involuntary)

```c
// Normal termination
exit(0);    // Success
exit(1);    // Error

// Kill a process
kill(pid, SIGTERM);  // Graceful termination
kill(pid, SIGKILL);  // Force kill
```

### Zombie and Orphan Processes

| Type | Description | Solution |
|------|-------------|----------|
| **Zombie** | Child terminated but parent hasn't called wait() | Parent calls wait() |
| **Orphan** | Parent terminated before child | init/systemd adopts child |

---

## Process Scheduling

### Types of Schedulers

| Scheduler | Description | Frequency |
|-----------|-------------|-----------|
| **Long-term** | Selects processes for ready queue | Minutes |
| **Short-term** | Selects ready process for CPU | Milliseconds |
| **Medium-term** | Swapping (suspending/resuming) | Seconds |

### Scheduling Queues

```
┌─────────────────────────────────────────────────────────┐
│                         Job Queue                       │
│      (All processes in the system)                     │
└────────────────────────────┬────────────────────────────┘
                             │ Long-term scheduler
                             ▼
┌─────────────────────────────────────────────────────────┐
│                       Ready Queue                       │
│      (Processes waiting for CPU)                       │
└────────────────────────────┬────────────────────────────┘
                             │ Short-term scheduler
                             ▼
                     ┌───────────────┐
                     │      CPU      │
                     └───────┬───────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
     ┌───────────┐    ┌───────────┐    ┌───────────┐
     │ I/O Queue │    │Time Expire│    │Terminated │
     └─────┬─────┘    └─────┬─────┘    └───────────┘
           │                │
           └────────────────┴──► Back to Ready Queue
```

### Scheduling Criteria

| Criteria | Goal | Description |
|----------|------|-------------|
| **CPU Utilization** | Maximize | Keep CPU busy |
| **Throughput** | Maximize | Processes completed per time |
| **Turnaround Time** | Minimize | Total time from submission to completion |
| **Waiting Time** | Minimize | Time spent in ready queue |
| **Response Time** | Minimize | Time from request to first response |

### Key Formulas

| Metric | Formula |
|--------|---------|
| **Turnaround Time (TAT)** | Completion Time - Arrival Time |
| **Waiting Time (WT)** | Turnaround Time - Burst Time |
| **Response Time (RT)** | First Response - Arrival Time |
| **Throughput** | Number of Processes / Total Time |

---

## Scheduling Algorithms

### 1. First-Come, First-Served (FCFS)

**Characteristics:**
- Non-preemptive
- Simple to implement
- Convoy effect possible

**Example:**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 24 |
| P2 | 0 | 3 |
| P3 | 0 | 3 |

**Gantt Chart:**
```
┌────────────────────────┬─────┬─────┐
│          P1            │ P2  │ P3  │
└────────────────────────┴─────┴─────┘
0                       24    27    30
```

**Calculations:**
- TAT(P1) = 24 - 0 = 24
- TAT(P2) = 27 - 0 = 27
- TAT(P3) = 30 - 0 = 30
- Average TAT = (24 + 27 + 30) / 3 = **27**
- WT(P1) = 24 - 24 = 0
- WT(P2) = 27 - 3 = 24
- WT(P3) = 30 - 3 = 27
- Average WT = (0 + 24 + 27) / 3 = **17**

---

### 2. Shortest Job First (SJF)

**Non-Preemptive SJF**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 7 |
| P2 | 2 | 4 |
| P3 | 4 | 1 |
| P4 | 5 | 4 |

**Execution Order:** P1 → P3 → P2 → P4

**Gantt Chart:**
```
┌───────┬───┬───────┬───────┐
│  P1   │P3 │  P2   │  P4   │
└───────┴───┴───────┴───────┘
0       7   8      12      16
```

**Calculations:**
- TAT(P1) = 7 - 0 = 7
- TAT(P2) = 12 - 2 = 10
- TAT(P3) = 8 - 4 = 4
- TAT(P4) = 16 - 5 = 11
- Average TAT = (7 + 10 + 4 + 11) / 4 = **8**
- Average WT = (0 + 6 + 3 + 7) / 4 = **4**

---

### 3. Shortest Remaining Time First (SRTF)

**Preemptive version of SJF**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 8 |
| P2 | 1 | 4 |
| P3 | 2 | 9 |
| P4 | 3 | 5 |

**Gantt Chart:**
```
┌───┬───────┬───────┬───────────┬─────────────────┐
│P1 │  P2   │  P4   │    P1     │       P3        │
└───┴───────┴───────┴───────────┴─────────────────┘
0   1       5      10          17                26
```

**Calculations:**
- TAT(P1) = 17 - 0 = 17, WT = 17 - 8 = 9
- TAT(P2) = 5 - 1 = 4, WT = 0
- TAT(P3) = 26 - 2 = 24, WT = 15
- TAT(P4) = 10 - 3 = 7, WT = 2
- Average TAT = 13, Average WT = 6.5

---

### 4. Priority Scheduling

**Characteristics:**
- Each process assigned a priority
- Higher priority = executed first
- Can be preemptive or non-preemptive

**Example (Non-Preemptive):**

| Process | Arrival | Burst | Priority |
|---------|---------|-------|----------|
| P1 | 0 | 10 | 3 |
| P2 | 0 | 1 | 1 |
| P3 | 0 | 2 | 4 |
| P4 | 0 | 1 | 5 |
| P5 | 0 | 5 | 2 |

*(Lower number = Higher priority)*

**Gantt Chart:**
```
┌───┬───────┬────────────┬────┬───┐
│P2 │  P5   │    P1      │ P3 │P4 │
└───┴───────┴────────────┴────┴───┘
0   1       6           16   18  19
```

**Problem:** Starvation (low priority may never execute)

**Solution:** Aging (increase priority over time)

---

### 5. Round Robin (RR)

**Characteristics:**
- Preemptive
- Time quantum (time slice)
- Fair allocation

**Example (Time Quantum = 4):**

| Process | Arrival Time | Burst Time |
|---------|--------------|------------|
| P1 | 0 | 24 |
| P2 | 0 | 3 |
| P3 | 0 | 3 |

**Gantt Chart:**
```
┌────┬────┬────┬────┬────┬────┬────┬────┐
│ P1 │ P2 │ P3 │ P1 │ P1 │ P1 │ P1 │ P1 │
└────┴────┴────┴────┴────┴────┴────┴────┘
0    4    7   10   14   18   22   26   30
```

**Calculations:**
- TAT(P1) = 30 - 0 = 30
- TAT(P2) = 7 - 0 = 7
- TAT(P3) = 10 - 0 = 10
- Average TAT = (30 + 7 + 10) / 3 = **15.67**
- Average WT = (6 + 4 + 7) / 3 = **5.67**

**Time Quantum Selection:**
- Too large → Becomes FCFS
- Too small → Too many context switches
- Typical: 10-100 ms

---

### 6. Multilevel Queue Scheduling

```
                    ┌────────────────────────────┐
                    │   System Processes         │ ← Highest Priority
                    ├────────────────────────────┤
                    │   Interactive Processes    │
                    ├────────────────────────────┤
                    │   Interactive Editing      │
                    ├────────────────────────────┤
                    │   Batch Processes          │
                    ├────────────────────────────┤
                    │   Student Processes        │ ← Lowest Priority
                    └────────────────────────────┘
```

---

### Algorithm Comparison

| Algorithm | Preemption | Starvation | Complexity |
|-----------|------------|------------|------------|
| FCFS | No | No | Simple |
| SJF | No | Yes | Medium |
| SRTF | Yes | Yes | Medium |
| Priority | Both | Yes | Medium |
| Round Robin | Yes | No | Simple |
| Multilevel | Both | Possible | Complex |

---

## Inter-Process Communication (IPC)

### Why IPC?

- Data sharing between processes
- Computation speedup
- Modularity
- Convenience

### IPC Methods

#### 1. Pipes

```
┌───────────┐          ┌───────────┐
│  Process  │──────────│  Process  │
│     A     │   Pipe   │     B     │
│  (Writer) │──────────│  (Reader) │
└───────────┘          └───────────┘
```

```c
int fd[2];
pipe(fd);
// fd[0] - read end
// fd[1] - write end
```

#### 2. Named Pipes (FIFOs)

```bash
mkfifo mypipe
echo "Hello" > mypipe &
cat < mypipe
```

#### 3. Message Queues

```c
// Create/access message queue
int msgid = msgget(key, 0666 | IPC_CREAT);

// Send message
msgsnd(msgid, &message, size, 0);

// Receive message
msgrcv(msgid, &message, size, type, 0);
```

#### 4. Shared Memory

```c
// Create shared memory
int shmid = shmget(key, size, 0666 | IPC_CREAT);

// Attach to address space
char *data = shmat(shmid, NULL, 0);

// Use shared memory
strcpy(data, "Hello");

// Detach
shmdt(data);
```

#### 5. Semaphores

```c
// Create semaphore
int semid = semget(key, 1, 0666 | IPC_CREAT);

// Wait (P operation)
semop(semid, &decrement, 1);

// Signal (V operation)
semop(semid, &increment, 1);
```

#### 6. Sockets

```c
// Create socket
int sockfd = socket(AF_INET, SOCK_STREAM, 0);

// Connect, send, receive...
```

### IPC Comparison

| Method | Speed | Capacity | Scope |
|--------|-------|----------|-------|
| Pipes | Fast | Limited | Related processes |
| Named Pipes | Fast | Limited | Any process |
| Message Queues | Medium | Medium | System-wide |
| Shared Memory | Fastest | Large | System-wide |
| Sockets | Medium | Variable | Network-wide |

---

## Context Switching

### What is Context Switching?

> **Context Switching** is the process of saving the state of a currently running process and loading the state of the next process to be executed.

### Context Switch Steps

```
Process A Running              Process B Running
      │                              ▲
      │ 1. Interrupt/System Call     │
      ▼                              │
┌─────────────────┐                  │
│ Save state of A │                  │
│ (Registers, PC, │                  │
│  Stack pointer) │                  │
└────────┬────────┘                  │
         │ 2. Update PCB of A        │
         ▼                           │
┌─────────────────┐                  │
│ Load state of B │                  │
│ from its PCB    │                  │
└────────┬────────┘                  │
         │ 3. Resume B               │
         └───────────────────────────┘
```

### Context Switch Overhead

- Context switch time is pure overhead
- Depends on hardware support
- Typically 1-1000 microseconds

---

## Threads

### What is a Thread?

> A **Thread** is the smallest unit of execution within a process. Multiple threads can exist within a process, sharing resources.

### Process vs Thread

| Aspect | Process | Thread |
|--------|---------|--------|
| Memory | Separate address space | Shared address space |
| Creation | Heavy (forking) | Lightweight |
| Communication | IPC needed | Direct memory access |
| Context Switch | Expensive | Cheap |
| Crash Impact | Isolated | Affects entire process |

### Thread Types

#### User-Level Threads
- Managed by user library
- Kernel unaware
- Fast context switch
- One blocks → all block

#### Kernel-Level Threads
- Managed by kernel
- Better scheduling
- More overhead
- One blocks → others continue

### Multithreading Models

**1. Many-to-One**
```
User Threads: T1  T2  T3  T4
                 \  |  /
                  \ | /
Kernel Thread:     K1
```

**2. One-to-One**
```
User Threads:   T1   T2   T3   T4
                |    |    |    |
Kernel Threads: K1   K2   K3   K4
```

**3. Many-to-Many**
```
User Threads:   T1   T2   T3   T4
                 \  / \  / \  /
Kernel Threads:  K1    K2    K3
```

---

## Summary

- Process is a program in execution with resources
- Process states: New, Ready, Running, Waiting, Terminated
- PCB contains all process information
- Schedulers: Long-term, Short-term, Medium-term
- Scheduling algorithms: FCFS, SJF, Priority, Round Robin
- IPC methods: Pipes, Message Queues, Shared Memory
- Threads are lightweight processes sharing memory

---

[← Previous: Shell Programming](03-shell-programming.md) | [Next: Memory Management →](05-memory-management.md)
