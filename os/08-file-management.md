---
layout: default
title: File Management
---

# File Management

[← Back to Home](../index.md)

---

## Table of Contents
- [Introduction to Files](#introduction-to-files)
- [File Control Block (FCB)](#file-control-block-fcb)
- [File System](#file-system)
- [Disk Space Allocation](#disk-space-allocation)
- [Disk Scheduling Algorithms](#disk-scheduling-algorithms)
- [Hard Disk Structure](#hard-disk-structure)
- [I/O Techniques](#io-techniques)
- [Booting Process](#booting-process)

---

## Introduction to Files

### What is a File?

**User View:**
- File is a container which contains logically related information/data
- File is a collection of characters/records/lines
- File is a basic storage unit

**System View:**
- File is a stream of bits/bytes
- **File = Data + Metadata**
  - Data = Actual file contents
  - Metadata = Information about the file

---

## File Control Block (FCB)

> In UNIX environment, FCB is also called as **iNode**.

### FCB/iNode Contents

| Field | Description |
|-------|-------------|
| **iNode Number** | Unique identifier of a file |
| **File Name** | Name of the file |
| **File Type** | Type of the file |
| **File Size** | Size in bytes |
| **Parent Folder** | Location of parent directory |
| **Access Permissions** | Read, Write, Execute permissions |
| **Time Stamps** | Creation, modification, access times |

> **Note:** Per file one iNode/FCB gets created. Number of iNodes = Number of files on disk.

---

## File System

> **File System** is a way to store data onto the disk in an organized manner so that it can be accessed efficiently and conveniently.

### File System Examples

| Operating System | File System |
|------------------|-------------|
| UNIX | UFS (UNIX File System) |
| Linux | ext2, ext3, ext4 |
| Windows | FAT, NTFS |
| MAC OS X | HFS (Hierarchical File System) |

### File System Structure

```
┌────────────────────────────────────────┐
│           Boot Block/Sector            │  ← Bootstrap program
├────────────────────────────────────────┤
│       Volume Control Block             │  ← Super block
│     (File system metadata)             │
├────────────────────────────────────────┤
│        Master File Table               │  ← iNode list
│          (iNode Block)                 │
├────────────────────────────────────────┤
│                                        │
│            Data Blocks                 │  ← Actual file data
│                                        │
└────────────────────────────────────────┘
```

---

## Disk Space Allocation

### 1. Contiguous Allocation

Free data blocks are allocated for a file in a **contiguous manner**.

```
┌────┬────┬────┬────┬────┬────┬────┐
│ F1 │ F1 │ F1 │ F2 │ F2 │    │    │
└────┴────┴────┴────┴────┴────┴────┘
  0    1    2    3    4    5    6
```

| Advantages | Disadvantages |
|------------|---------------|
| Sequential access | File cannot grow easily |
| Random access | External fragmentation |
| Simple to implement | Need defragmentation |

---

### 2. Linked Allocation

Free data blocks are allocated for a file in a **linked list manner**.

```
┌────┐    ┌────┐    ┌────┐    ┌────┐
│ F1 │───►│ F1 │───►│ F1 │───►│NULL│
└────┘    └────┘    └────┘    └────┘
Block 0   Block 3   Block 7   End
```

| Advantages | Disadvantages |
|------------|---------------|
| Sequential access | Slow random access |
| No file size limit | Pointer overhead |
| No external fragmentation | |

**Example:** FAT (File Allocation Table)

---

### 3. Indexed Allocation

An **index block** maintains pointers to all data blocks of a file.

```
Index Block          Data Blocks
┌─────────┐         ┌─────────┐
│    3    │────────►│  Data   │ Block 3
├─────────┤         └─────────┘
│    7    │────────►┌─────────┐
├─────────┤         │  Data   │ Block 7
│   12    │────►... └─────────┘
├─────────┤
│   -1    │ (End)
└─────────┘
```

| Advantages | Disadvantages |
|------------|---------------|
| Sequential access | Index block overhead |
| Random access | File size limited by index block |
| No external fragmentation | |

**Example:** UFS, ext2, ext3

---

## Disk Scheduling Algorithms

> When multiple processes request disk access, the disk scheduling algorithm determines the order in which requests are serviced.

### Key Metrics

| Metric | Description |
|--------|-------------|
| **Seek Time** | Time to move disk head to desired track |
| **Rotational Latency** | Time for sector to rotate under head |
| **Access Time** | Seek Time + Rotational Latency |

---

### 1. FCFS (First Come First Served)

Request which arrived first gets serviced first.

**Example:** Request Queue: 98, 183, 37, 122, 14, 124, 65, 67 (Head at 53)

```
Head Movement: 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
Total Seek Time: 45 + 85 + 146 + 85 + 108 + 110 + 59 + 2 = 640 cylinders
```

---

### 2. SSTF (Shortest Seek Time First)

Request closest to current head position gets serviced first.

**Example:** Same queue, Head at 53

```
Head Movement: 53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
Total Seek Time: Much reduced compared to FCFS
```

**Problem:** May cause starvation for requests far from head.

---

### 3. SCAN (Elevator Algorithm)

Head scans disk from one end to another, servicing requests along the way.

```
Moving toward 0:
53 → 37 → 14 → 0 (end) → 65 → 67 → 98 → 122 → 124 → 183
```

---

### 4. C-SCAN (Circular SCAN)

Head scans in **one direction only**. After reaching end, jumps to beginning.

```
53 → 65 → 67 → 98 → 122 → 124 → 183 → (jump to 0) → 14 → 37
```

---

### 5. LOOK / C-LOOK

Like SCAN/C-SCAN, but head only goes as far as the last request in each direction.

```
LOOK: 53 → 37 → 14 → (reverse) → 65 → 67 → 98 → 122 → 124 → 183
No need to go to end (0 or max)
```

---

### Disk Scheduling Comparison

| Algorithm | Seek Time | Starvation | Notes |
|-----------|-----------|------------|-------|
| FCFS | High | No | Simple, fair |
| SSTF | Low | Yes | May starve far requests |
| SCAN | Medium | No | Elevator-like movement |
| C-SCAN | Medium | No | More uniform wait time |
| LOOK | Medium | No | Optimized SCAN |

---

## Hard Disk Structure

### Physical Components

```
        Spindle
           │
    ┌──────┼──────┐
    │   ┌──┼──┐   │
    │   │  │  │   │  ← Platters
    │   └──┼──┘   │
    └──────┼──────┘
           │
        ───┴───  ← Arm with Read/Write Head
```

### Disk Organization

| Component | Description |
|-----------|-------------|
| **Platter** | Circular disk coated with magnetic material |
| **Track** | Concentric rings on platter surface |
| **Sector** | Smallest unit of storage (typically 512 bytes) |
| **Cylinder** | All tracks at same position across platters |
| **Head** | Read/Write mechanism |

### Access Time Components

```
Total Access Time = Seek Time + Rotational Latency + Transfer Time

Where:
- Seek Time: Move head to correct track
- Rotational Latency: Wait for sector to rotate under head
- Transfer Time: Time to read/write data
```

---

## I/O Techniques

### 1. Programmed I/O (Polling)

- CPU continuously checks device status
- CPU waits for I/O completion
- Also called **Synchronous I/O**

| Advantage | Disadvantage |
|-----------|--------------|
| Simple | Low CPU utilization |

---

### 2. Interrupt-Driven I/O

- CPU issues command and continues other work
- Device sends **interrupt** when ready
- Also called **Asynchronous I/O**

| Advantage | Disadvantage |
|-----------|--------------|
| Better CPU utilization | Interrupt overhead |

### Interrupt Types

| Type | Description |
|------|-------------|
| **Hardware Interrupt** | From devices (keyboard, mouse, disk) |
| **Software Interrupt** | From programs (system calls) |

### Interrupt Vector Table (IVT)

- Table maintained by OS
- Stores starting address of interrupt service routines (ISR)

---

### 3. DMA (Direct Memory Access)

- Special controller handles data transfer
- CPU initiates transfer, DMA controller completes it
- CPU is free for other tasks

```
          DMA Controller
               │
    CPU ──────┼────── Memory
               │
           ────┴────
           I/O Device
```

| Advantage | Disadvantage |
|-----------|--------------|
| Maximum CPU utilization | DMA controller cost |
| Efficient for bulk transfers | Bus contention |

---

## Booting Process

### Key Terminologies

| Term | Description |
|------|-------------|
| **BIOS** | Basic Input Output System - Firmware in motherboard ROM |
| **POST** | Power-On Self Test - Tests hardware components |
| **Bootstrap Loader** | Finds and starts bootable device |
| **Bootstrap Program** | Loads OS kernel into memory |
| **Bootloader** | Allows selection of OS when multiple are installed |

### Boot Sequence

```
┌──────────────────────────────────────────────────────────────┐
│ 1. Power On                                                   │
├──────────────────────────────────────────────────────────────┤
│ 2. BIOS/UEFI Executes                                        │
│    - POST (Power-On Self Test)                               │
│    - Initialize hardware                                      │
├──────────────────────────────────────────────────────────────┤
│ 3. Bootstrap Loader                                           │
│    - Find bootable device                                     │
│    - Load first sector (512 bytes)                           │
├──────────────────────────────────────────────────────────────┤
│ 4. Bootloader (if multiple OS)                                │
│    - GRUB, Windows Boot Manager                              │
│    - User selects OS                                          │
├──────────────────────────────────────────────────────────────┤
│ 5. Bootstrap Program                                          │
│    - Load OS kernel into main memory                         │
├──────────────────────────────────────────────────────────────┤
│ 6. Kernel Initialization                                      │
│    - Initialize drivers, services                            │
│    - Start user interface                                     │
└──────────────────────────────────────────────────────────────┘
```

### BIOS Contents

- POST/BIST program
- Bootstrap loader
- Basic device drivers
- Bootable device preference settings

---

## Summary

- **File** = Data + Metadata (stored in iNode/FCB)
- **File Systems**: ext4 (Linux), NTFS (Windows), HFS (Mac)
- **Disk Allocation**: Contiguous, Linked, Indexed
- **Disk Scheduling**: FCFS, SSTF, SCAN, C-SCAN, LOOK
- **I/O Methods**: Polling, Interrupt-driven, DMA
- **Boot Process**: BIOS → POST → Bootstrap → Kernel

---

[← Previous: Deadlock](07-deadlock.md) | [Back to Home →](../index.md)
