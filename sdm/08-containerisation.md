---
layout: default
title: Containerisation
---

# Containerisation

[← Back to Home](../index.md)

---

## What is Containerisation?

> **Containerisation** is a lightweight form of virtualization that packages an application with its dependencies into a container that can run consistently across environments.

## Containers vs Virtual Machines

```
     Virtual Machines              Containers
┌─────────────────────┐      ┌─────────────────────┐
│  App A   │  App B   │      │  App A   │  App B   │
├──────────┼──────────┤      ├──────────┴──────────┤
│ Guest OS │ Guest OS │      │   Container Engine  │
├──────────┴──────────┤      │      (Docker)       │
│     Hypervisor      │      ├─────────────────────┤
├─────────────────────┤      │      Host OS        │
│      Host OS        │      ├─────────────────────┤
├─────────────────────┤      │     Hardware        │
│     Hardware        │      └─────────────────────┘
└─────────────────────┘
```

| Aspect | VM | Container |
|--------|-----|-----------|
| Size | Gigabytes | Megabytes |
| Startup | Minutes | Seconds |
| Isolation | Full | Process level |
| Resources | Heavy | Lightweight |
| OS | Each has own OS | Shares host OS |

## Benefits of Containers

| Benefit | Description |
|---------|-------------|
| **Portability** | Run anywhere consistently |
| **Efficiency** | Less overhead than VMs |
| **Scalability** | Easy to scale up/down |
| **Isolation** | Apps don't interfere |
| **DevOps** | Consistent dev to prod |

## Container Concepts

| Term | Description |
|------|-------------|
| **Image** | Read-only template for container |
| **Container** | Running instance of image |
| **Registry** | Storage for images (Docker Hub) |
| **Layer** | Incremental change to image |

---

[← Previous: DevOps](07-devops.md) | [Next: Docker →](09-docker.md)
