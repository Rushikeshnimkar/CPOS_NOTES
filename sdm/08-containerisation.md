---
layout: default
title: Containerisation
---

# Containerisation

[← Back to Home](../index.md)

---

## What is Containerisation?

> **Containerisation** is a lightweight form of virtualization that packages an application with its dependencies into a container that can run consistently across environments.

### Definition
A **container** is a standard unit of software that packages code and all its dependencies so the application runs quickly and reliably across computing environments.

### Why Containers?
- **Consistency**: Same environment from dev to production
- **Isolation**: Applications don't interfere with each other
- **Portability**: Run anywhere containers are supported
- **Efficiency**: Share OS kernel, less overhead than VMs
- **Speed**: Start in seconds, not minutes
- **Scalability**: Easy to scale up/down

---

## How Containers Work

> Containers use OS-level virtualization, sharing the host kernel while maintaining isolation.

### Linux Technologies Behind Containers

| Technology | Definition | Function |
|------------|------------|----------|
| **Namespaces** | Isolate system resources | Separate view of processes, network, files |
| **cgroups** | Control groups | Limit and account resource usage (CPU, memory) |
| **Union File System** | Layered filesystem | Efficient image storage and container creation |
| **Seccomp** | Security computing mode | Restrict system calls |

### Namespace Types

| Namespace | Isolates |
|-----------|----------|
| **PID** | Process IDs |
| **NET** | Network interfaces, ports, routing |
| **MNT** | Mount points, filesystems |
| **UTS** | Hostname and domain name |
| **IPC** | Inter-process communication |
| **USER** | User and group IDs |

---

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

### Detailed Comparison

| Aspect | Virtual Machine | Container |
|--------|-----------------|-----------|
| **Size** | Gigabytes (includes OS) | Megabytes (app + deps) |
| **Startup Time** | Minutes | Seconds |
| **Isolation** | Full (hardware-level) | Process-level |
| **Resources** | Heavy (own OS, kernel) | Lightweight (shared kernel) |
| **OS** | Each has own OS | Shares host OS kernel |
| **Density** | Few VMs per host | Many containers per host |
| **Security** | Stronger isolation | Weaker (shared kernel) |
| **Use Case** | Legacy apps, different OS | Microservices, cloud-native |

---

## Container Concepts

| Term | Definition |
|------|------------|
| **Image** | Read-only template containing application and dependencies |
| **Container** | Running instance of an image (adds writable layer) |
| **Registry** | Storage and distribution system for images (Docker Hub) |
| **Layer** | Incremental change in image (cached for efficiency) |
| **Dockerfile** | Text file with instructions to build an image |
| **Volume** | Persistent storage that outlives containers |

### Image vs Container

```
┌──────────────────────────────────────────┐
│                 IMAGE                     │
│  ┌────────────────────────────────────┐  │
│  │ Layer 3: Application Code          │  │
│  ├────────────────────────────────────┤  │
│  │ Layer 2: Dependencies              │  │
│  ├────────────────────────────────────┤  │
│  │ Layer 1: Base OS                   │  │
│  └────────────────────────────────────┘  │
│           (Read-Only)                     │
└──────────────────────────────────────────┘
                    │
                    │ docker run
                    ▼
┌──────────────────────────────────────────┐
│               CONTAINER                   │
│  ┌────────────────────────────────────┐  │
│  │ Writable Layer (container changes) │  │
│  ├────────────────────────────────────┤  │
│  │ Layer 3: Application Code          │  │
│  ├────────────────────────────────────┤  │
│  │ Layer 2: Dependencies              │  │
│  ├────────────────────────────────────┤  │
│  │ Layer 1: Base OS                   │  │
│  └────────────────────────────────────┘  │
└──────────────────────────────────────────┘
```

---

## Benefits of Containers

| Benefit | Description | Example |
|---------|-------------|---------|
| **Portability** | Run anywhere consistently | Dev laptop → staging → production |
| **Efficiency** | Less overhead than VMs | More containers per server |
| **Scalability** | Easy to scale up/down | Handle traffic spikes |
| **Isolation** | Apps don't interfere | Different Node versions |
| **DevOps** | Consistent dev to prod | No "works on my machine" |
| **Microservices** | Each service in own container | Independent deployment |
| **CI/CD** | Fast, reproducible builds | Automated testing |

---

## Container Runtimes

> Container runtime is software that runs containers.

| Runtime | Description |
|---------|-------------|
| **Docker** | Most popular, full platform |
| **containerd** | Industry-standard core runtime |
| **CRI-O** | Lightweight for Kubernetes |
| **Podman** | Daemonless, rootless containers |
| **runc** | Low-level OCI runtime |

### Container Standards

| Standard | Definition |
|----------|------------|
| **OCI** | Open Container Initiative |
| **Image Spec** | Format for container images |
| **Runtime Spec** | How to run containers |

---

## Container Orchestration

> Managing many containers at scale.

### Why Orchestration?
- **Scheduling**: Where to run containers
- **Scaling**: Add/remove containers based on load
- **Networking**: Container-to-container communication
- **Load Balancing**: Distribute traffic
- **Self-Healing**: Restart failed containers
- **Rolling Updates**: Update without downtime

### Orchestration Tools

| Tool | Description |
|------|-------------|
| **Kubernetes** | Industry standard, most features |
| **Docker Swarm** | Simple, Docker-native |
| **Amazon ECS** | AWS managed service |
| **Azure Container Instances** | Azure serverless containers |
| **Google Cloud Run** | GCP serverless containers |

---

## Container Use Cases

| Use Case | Description |
|----------|-------------|
| **Microservices** | Each service runs in its own container |
| **CI/CD Pipelines** | Consistent build environments |
| **Development** | Match production environment locally |
| **Cloud Migration** | Package legacy apps for cloud |
| **Hybrid Cloud** | Run same containers anywhere |
| **Edge Computing** | Lightweight deployment at edge |

---

## Container Security Considerations

| Concern | Mitigation |
|---------|------------|
| **Shared Kernel** | Keep host kernel updated |
| **Image Vulnerabilities** | Scan images for CVEs |
| **Privilege Escalation** | Run as non-root user |
| **Resource Abuse** | Set CPU/memory limits |
| **Network Exposure** | Limit container networking |
| **Secrets** | Use secret management tools |

---

[← Previous: DevOps](07-devops.md) | [Next: Docker →](09-docker.md)
