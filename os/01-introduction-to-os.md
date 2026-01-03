---
layout: default
title: Introduction to Operating Systems
---

# Introduction to Operating Systems

[← Back to Home](../index.md)

---

## Table of Contents
- [What is an Operating System?](#what-is-an-operating-system)
- [Functions of an Operating System](#functions-of-an-operating-system)
- [Goals of an Operating System](#goals-of-an-operating-system)
- [Types of Operating Systems](#types-of-operating-systems)
- [Operating System Architecture](#operating-system-architecture)
- [System Calls](#system-calls)
- [Operating System Services](#operating-system-services)

---

## What is an Operating System?

An **Operating System (OS)** is system software that acts as an intermediary between computer hardware and the user. It manages hardware resources and provides services for application programs.

### Definition

> An Operating System is a program that manages computer hardware, provides a basis for application programs, and acts as an intermediary between the computer user and the computer hardware.

### Role of Operating System

```
┌─────────────────────────────────────────┐
│              User Programs              │
├─────────────────────────────────────────┤
│           Operating System              │
├─────────────────────────────────────────┤
│              Hardware                   │
│  (CPU, Memory, I/O Devices, Storage)    │
└─────────────────────────────────────────┘
```

### Key Points

- **Resource Manager**: OS manages all hardware and software resources
- **Control Program**: Controls execution of user programs to prevent errors
- **Kernel**: The core component that is always running

---

## Functions of an Operating System

### 1. Process Management

| Function | Description |
|----------|-------------|
| Process Creation | Creating new processes |
| Process Scheduling | Deciding which process runs when |
| Process Termination | Ending processes and releasing resources |
| Process Synchronization | Coordinating between processes |
| Inter-Process Communication | Enabling communication between processes |

### 2. Memory Management

- Keeping track of which parts of memory are in use
- Allocating and deallocating memory as needed
- Managing virtual memory
- Memory protection between processes

### 3. File System Management

- Creating and deleting files and directories
- Mapping files onto secondary storage
- Backup of files on stable storage

### 4. I/O System Management

- Managing device drivers
- Buffering, caching, and spooling
- Providing general device-driver interface

### 5. Security and Protection

- User authentication
- Access control to resources
- Protection against malware
- Encryption and data security

### 6. Networking

- Managing network connections
- Protocol handling
- Data transmission

---

## Goals of an Operating System

### Primary Goals

| Goal | Description |
|------|-------------|
| **Convenience** | Making the computer easier to use |
| **Efficiency** | Using hardware resources efficiently |
| **Ability to Evolve** | Permitting effective development and testing of new functions |

### Secondary Goals

- **Throughput**: Maximize the number of tasks completed per unit time
- **Response Time**: Minimize time between submission and completion
- **Resource Utilization**: Keep all resources as busy as possible
- **Fairness**: Give equal opportunity to all processes

---

## Types of Operating Systems

### 1. Batch Operating System

```
┌──────────────────────────────────────────────┐
│ Jobs are collected → Batched → Executed      │
│                                              │
│ User → Submit Job → Operator → Batch → CPU   │
└──────────────────────────────────────────────┘
```

**Characteristics:**
- No direct interaction between user and computer
- Jobs with similar requirements batched together
- Reduces setup time

**Advantages:**
- Efficient for large jobs
- Reduced idle time

**Disadvantages:**
- No user interaction during execution
- Difficult to debug

---

### 2. Time-Sharing Operating System (Multitasking)

**Definition:** Multiple users share the computer simultaneously through rapid switching between tasks.

**Key Concepts:**
- **Time Quantum/Time Slice**: Fixed time period allocated to each process
- **Context Switching**: Saving and restoring process state

```
Time →  ┌────┬────┬────┬────┬────┬────┐
        │ P1 │ P2 │ P3 │ P1 │ P2 │ P3 │
        └────┴────┴────┴────┴────┴────┘
        Each process gets a time slice
```

**Advantages:**
- Quick response time
- Multiple users supported
- Reduced CPU idle time

**Disadvantages:**
- More complex than batch systems
- Security concerns with multiple users

---

### 3. Distributed Operating System

**Definition:** A collection of independent computers that appears as a single coherent system.

```
┌─────────┐    ┌─────────┐    ┌─────────┐
│ Node 1  │────│ Node 2  │────│ Node 3  │
│  (OS)   │    │  (OS)   │    │  (OS)   │
└─────────┘    └─────────┘    └─────────┘
      │              │              │
      └──────────────┴──────────────┘
              Distributed OS Layer
```

**Advantages:**
- Resource sharing
- Reliability (fault tolerance)
- Scalability
- Performance through parallelism

**Disadvantages:**
- Complex to implement
- Network dependency
- Security challenges

---

### 4. Real-Time Operating System (RTOS)

**Definition:** OS designed for applications that require guaranteed timing.

**Types:**

| Type | Description | Example |
|------|-------------|---------|
| **Hard Real-Time** | Strict deadlines; missing causes failure | Medical devices, Aircraft control |
| **Soft Real-Time** | Deadlines important but not critical | Video streaming, Gaming |

**Characteristics:**
- Predictable response times
- Minimal interrupt latency
- Priority-based scheduling

---

### 5. Network Operating System

**Definition:** OS that provides services to computers connected in a network.

**Features:**
- File sharing across network
- Printer sharing
- User management
- Security features

**Examples:** Windows Server, Linux Server, Novell NetWare

---

### 6. Mobile Operating System

**Definition:** OS designed for mobile devices.

**Examples:**
- Android
- iOS
- Windows Mobile

**Features:**
- Touch interface
- Power management
- Sensor management
- App ecosystem

---

## Operating System Architecture

### 1. Monolithic Architecture

```
┌────────────────────────────────────┐
│          User Programs             │
├────────────────────────────────────┤
│    ┌────────────────────────┐     │
│    │       KERNEL           │     │
│    │  (All OS services in   │     │
│    │   single large block)  │     │
│    └────────────────────────┘     │
├────────────────────────────────────┤
│           Hardware                 │
└────────────────────────────────────┘
```

**Characteristics:**
- All OS services run in kernel space
- Fast performance (no mode switching overhead)
- Difficult to maintain and debug

**Examples:** MS-DOS, Early UNIX

---

### 2. Layered Architecture

```
┌────────────────────────────────────┐
│ Layer N: User Programs             │
├────────────────────────────────────┤
│ Layer N-1: User Interface          │
├────────────────────────────────────┤
│ Layer N-2: I/O Management          │
├────────────────────────────────────┤
│ Layer N-3: Memory Management       │
├────────────────────────────────────┤
│ Layer 1: CPU Scheduling            │
├────────────────────────────────────┤
│ Layer 0: Hardware                  │
└────────────────────────────────────┘
```

**Advantages:**
- Modularity
- Easy to debug and verify
- Easy to modify

**Disadvantages:**
- Difficult to define layers
- Performance overhead

---

### 3. Microkernel Architecture

```
┌─────────────────────────────────────────────┐
│  File System │ Device Drivers │ Network     │
│  (User Space)│ (User Space)   │ (User Space)│
├─────────────────────────────────────────────┤
│         Microkernel (Minimal Kernel)        │
│  - IPC, Basic Scheduling, Memory Management │
├─────────────────────────────────────────────┤
│                 Hardware                    │
└─────────────────────────────────────────────┘
```

**Characteristics:**
- Minimal kernel with basic functions
- Most services run in user space
- Communication via message passing

**Advantages:**
- Easy to extend
- More reliable (service crash doesn't crash system)
- Better security

**Disadvantages:**
- Performance overhead due to message passing

**Examples:** Minix, QNX, Mach

---

### 4. Hybrid Architecture

Combines elements of monolithic and microkernel architectures.

**Examples:** Windows NT, macOS (XNU kernel)

---

## System Calls

### Definition

A **System Call** is a programmatic way for a program to request a service from the operating system's kernel.

### System Call Process

```
User Program                    Operating System
    │                                 │
    │   1. Call library function      │
    │   ─────────────────────────►   │
    │   2. Set up parameters          │
    │   3. Trap instruction           │
    │   ─────────────────────────►   │
    │                           4. Execute service
    │                           5. Return result
    │   ◄─────────────────────────   │
    │   6. Return to caller           │
    ▼                                 ▼
```

### Types of System Calls

#### 1. Process Control
| System Call | Description |
|-------------|-------------|
| `fork()` | Create a new process |
| `exec()` | Execute a program |
| `exit()` | Terminate a process |
| `wait()` | Wait for child process |
| `kill()` | Send signal to process |

#### 2. File Management
| System Call | Description |
|-------------|-------------|
| `open()` | Open a file |
| `close()` | Close a file |
| `read()` | Read from file |
| `write()` | Write to file |
| `lseek()` | Move file pointer |

#### 3. Device Management
| System Call | Description |
|-------------|-------------|
| `ioctl()` | Device control operations |
| `read()` | Read from device |
| `write()` | Write to device |

#### 4. Information Maintenance
| System Call | Description |
|-------------|-------------|
| `getpid()` | Get process ID |
| `alarm()` | Set alarm |
| `time()` | Get system time |

#### 5. Communication
| System Call | Description |
|-------------|-------------|
| `pipe()` | Create pipe |
| `shmget()` | Create shared memory |
| `mmap()` | Map file to memory |

---

## Operating System Services

### Services for Users

1. **Program Execution**: Load and run programs
2. **I/O Operations**: Handle input/output requests
3. **File System Manipulation**: Create, delete, read, write files
4. **Communication**: Enable process communication
5. **Error Detection**: Detect and handle errors

### Services for System Efficiency

1. **Resource Allocation**: Allocate resources to processes
2. **Accounting**: Track resource usage
3. **Protection**: Ensure authorized access only

---

## Key Terminologies

| Term | Definition |
|------|------------|
| **Kernel** | Core of OS, always in memory |
| **Shell** | User interface to the kernel |
| **Process** | Program in execution |
| **Thread** | Lightweight process |
| **Interrupt** | Signal to processor for attention |
| **Trap** | Software-generated interrupt |
| **Mode Bit** | Distinguishes user mode from kernel mode |

---

## Summary

- OS is an intermediary between user and hardware
- Main functions: Process, Memory, File, I/O, Security management
- Types: Batch, Time-sharing, Distributed, Real-time, Network, Mobile
- Architectures: Monolithic, Layered, Microkernel, Hybrid
- System calls provide interface between user programs and OS

---

[Next: Introduction to Linux →](02-introduction-to-linux.md)
