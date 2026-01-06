---
layout: default
title: Docker
---

# Docker

[← Back to Home](../index.md)

---

## Understanding the Problem: Without Virtualization

Before understanding Docker, let's understand the problem it solves.

### Traditional Physical Machines

| Aspect | Description |
|--------|-------------|
| **Single OS** | Each physical machine runs only one operating system |
| **Resource Waste** | Hardware often underutilized |
| **Scalability Issues** | Adding capacity means buying new hardware |
| **Dependency Conflicts** | Different applications may need conflicting libraries |

> **Problem**: What if we want to install Linux, Windows, and Macintosh on the same physical machine?

---

## What is a Hypervisor?

> **Hypervisor** (Virtual Machine Monitor - VMM) is software that enables multiple instances of operating systems to run on the same physical computing resources.

### Types of Hypervisors

| Type | Definition | Examples | Use Case |
|------|------------|----------|----------|
| **Type 1 (Bare Metal)** | Runs directly on hardware without host OS | VMware ESXi, Microsoft Hyper-V, Xen | Enterprise data centers |
| **Type 2 (Hosted)** | Runs on top of host operating system | VirtualBox, VMware Workstation, Parallels | Development/Testing |

### Hypervisor Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Virtual Machines                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │    App A    │  │    App B    │  │    App C    │         │
│  ├─────────────┤  ├─────────────┤  ├─────────────┤         │
│  │  Libraries  │  │  Libraries  │  │  Libraries  │         │
│  ├─────────────┤  ├─────────────┤  ├─────────────┤         │
│  │   Guest OS  │  │   Guest OS  │  │   Guest OS  │         │
│  │   (Linux)   │  │  (Windows)  │  │   (macOS)   │         │
│  └─────────────┘  └─────────────┘  └─────────────┘         │
├─────────────────────────────────────────────────────────────┤
│                      Hypervisor                             │
├─────────────────────────────────────────────────────────────┤
│                   Physical Hardware                         │
└─────────────────────────────────────────────────────────────┘
```

---

## What is Virtualization?

> **Virtualization** is the technology that creates virtual versions of physical computing resources (servers, storage, networks) allowing multiple operating systems to run on a single physical machine.

### How Virtualization Works

1. **Hardware Abstraction**: Hypervisor creates abstraction layer over physical hardware
2. **Resource Allocation**: Physical resources divided among virtual machines
3. **Isolation**: Each VM operates independently with its own OS
4. **Management**: Central management of all virtual resources

### Benefits of Virtualization
- ✅ Run multiple OS on single hardware
- ✅ Better hardware utilization
- ✅ Isolation between VMs
- ✅ Easy backup and recovery (snapshots)
- ✅ Cost savings on hardware

---

## Main Drawbacks of Virtualization

| Drawback | Description |
|----------|-------------|
| **Resource Overhead** | Each VM needs its own full OS copy (heavy resource consumption) |
| **Slow Boot Time** | VMs take minutes to start due to full OS boot |
| **Large Size** | VM images are typically gigabytes in size |
| **Performance Penalty** | Hypervisor layer adds overhead |
| **License Costs** | Each guest OS may require separate licensing |
| **Resource Duplication** | Same libraries/binaries duplicated across VMs |

> **The Problem**: Running 10 applications means 10 complete operating systems, even if they only need a few libraries!

---

## Virtualization vs Containerization

| Aspect | Virtualization (VMs) | Containerization (Docker) |
|--------|---------------------|--------------------------|
| **Guest OS** | Full OS for each VM | Shares host OS kernel |
| **Boot Time** | Minutes | Seconds |
| **Size** | Gigabytes | Megabytes |
| **Performance** | Near-native with overhead | Near-native (minimal overhead) |
| **Isolation** | Complete isolation | Process-level isolation |
| **Resource Usage** | Heavy | Lightweight |
| **Portability** | Hardware dependent | Highly portable |
| **Use Case** | Different OS requirements | Same OS, different apps |

### Visual Comparison

```
┌──────────────────────────────────────────────────────────────────────────────┐
│           VIRTUALIZATION                    CONTAINERIZATION                  │
│  ┌───────────────────────────┐      ┌──────────────────────────────┐        │
│  │    App A    │    App B    │      │  App A  │  App B  │  App C  │         │
│  ├─────────────┼─────────────┤      ├─────────┴─────────┴─────────┤         │
│  │ Guest OS    │ Guest OS    │      │         Container Engine     │         │
│  │ (full Linux)│ (full Win)  │      │           (Docker)           │         │
│  ├─────────────┴─────────────┤      ├────────────────────────────────┤       │
│  │        Hypervisor         │      │         Host OS Kernel         │       │
│  ├───────────────────────────┤      ├────────────────────────────────┤       │
│  │    Physical Hardware      │      │      Physical Hardware         │       │
│  └───────────────────────────┘      └────────────────────────────────┘       │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## What is Docker?

> **Docker** is an open platform for developing, shipping, and running applications. It is an OS-level virtualization software platform that allows you to **package your project** so that you can carry it from one place to another. The package (called a **container**) contains not only your application but also all its dependencies, including required software versions (e.g., Java 8, Java 11, Java 18, MySQL 5, MySQL 8, etc.).

### When to Use Docker?
- When you want to run **multiple versions of the same software** (e.g., Java 8 and Java 11 simultaneously)
- When you need **consistent environments** across development, testing, and production
- When deploying **microservices architecture**
- When you need **quick scaling** of applications

---

## Docker Engine

> **Docker Engine** is the core software that runs and manages Docker containers on your computer or server. Think of it as the **"brain"** that makes containers work.

### What Docker Engine Does

| Function | Description |
|----------|-------------|
| **Creates and runs containers** | It takes the instructions you give (like a Docker image) and runs it inside a container |
| **Manages containers** | It keeps track of all containers, starting them, stopping them, and handling their resources (CPU, memory, storage) |
| **Builds images** | Converts Dockerfiles into Docker images |
| **Handles networking** | Manages container-to-container and container-to-host communication |

### Docker Engine Components

```
┌─────────────────────────────────────────────────────────────────────┐
│                         USER                                        │
│                          │                                          │
│                    docker run ...                                   │
│                          │                                          │
│                          ▼                                          │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                   Docker CLI                                   │ │
│  │     (Command-Line Interface - the tool you type commands in)  │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                          │                                          │
│                     REST API                                        │
│                          │                                          │
│                          ▼                                          │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                   Docker Daemon (dockerd)                      │ │
│  │   (Background service that actually manages containers)       │ │
│  │   - Listens for commands                                       │ │
│  │   - Does heavy lifting of creating, running containers         │ │
│  │   - Manages images, networks, volumes                          │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│                         DOCKER ENGINE                               │
└─────────────────────────────────────────────────────────────────────┘
```

### Docker Daemon (dockerd)

> **Docker Daemon** is the background service that actually manages containers. It listens for commands and does the heavy lifting of creating, running, and managing containers.

**Key Responsibilities:**
- Listening for Docker API requests
- Managing Docker objects (images, containers, networks, volumes)
- Communicating with other daemons for Docker Swarm services

### Docker CLI (Command-Line Interface)

> **Docker CLI** is the command-line tool you use to give instructions to the Docker Daemon. For example, when you type `docker run` to start a container, you're using the Docker CLI to tell the Docker Daemon to start a container.

**How it works:**
1. You type a command like `docker run nginx`
2. Docker CLI sends this command to Docker Daemon via REST API
3. Docker Daemon executes the command and reports back
4. Docker CLI displays the result to you

### What You Get When You Install Docker

| Component | Description |
|-----------|-------------|
| **Docker Daemon** | Background service (dockerd) |
| **Docker CLI** | Command-line interface |
| **Docker Compose** | Multi-container orchestration (separate install in older versions) |
| **Docker Desktop** | GUI for Windows/Mac (includes everything) |

---

## Docker Objects Overview

> When you install and use Docker, you work with **lightweight containers** which contain different applications along with their dependencies including various different software versions.

### History
- Created in 2013 by Solomon Hykes at dotCloud
- Made containerization accessible to developers
- Revolutionized application deployment
- Written in Go programming language

### Why Docker?
- **Consistency**: "Works on my machine" → Works everywhere
- **Isolation**: Applications don't interfere with each other
- **Portability**: Run anywhere Docker is installed (Linux, Windows, Mac)
- **Efficiency**: Lightweight compared to VMs (shares host kernel)
- **Speed**: Start containers in seconds (not minutes like VMs)
- **Microservices**: Perfect for microservices architecture

---

## Docker Architecture

```
┌─────────────────────────────────────────────┐
│              Docker Client                  │
│         (docker build, run, pull)           │
└──────────────────┬──────────────────────────┘
                   │ REST API
                   ▼
┌─────────────────────────────────────────────┐
│              Docker Daemon                  │
│     (manages images, containers, networks)  │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────────┐
│              Docker Registry                │
│           (Docker Hub, private)             │
└─────────────────────────────────────────────┘
```

### Architecture Components

| Component | Definition | Function |
|-----------|------------|----------|
| **Docker Client** | CLI tool (`docker` command) | Sends commands to Docker daemon |
| **Docker Daemon** | Background service (`dockerd`) | Manages images, containers, networks |
| **Docker Registry** | Image storage server | Docker Hub, ECR, GCR, private registries |

### Docker Registry (Docker Hub)

> **Docker Registry** is a storage and content delivery system for holding Docker images.

| Registry Type | Description | Example |
|--------------|-------------|---------|
| **Public Registry** | Open to everyone | Docker Hub (hub.docker.com) |
| **Private Registry** | Restricted access | AWS ECR, Google GCR, Azure ACR |
| **Self-hosted** | Run your own registry | Docker Registry, Harbor |

**Docker Hub Features:**
- 📦 Store and distribute Docker images
- 🔍 Search for official and community images
- 🔐 Private repositories for confidential images
- 🤖 Automated builds from GitHub/Bitbucket
- ⭐ Official images maintained by Docker team

---

## Core Docker Objects

| Object | Definition | Purpose |
|--------|------------|---------|
| **Image** | Read-only template with instructions | Blueprint for containers |
| **Container** | Runnable instance of an image | Isolated application environment |
| **Volume** | Persistent data storage | Data survives container restart |
| **Network** | Container communication | Connect containers together |

### Image vs Container

| Image | Container |
|-------|-----------|
| Blueprint/Template | Running instance |
| Read-only | Read-write layer on top |
| Stored on disk | Runs in memory |
| Can create multiple containers | Ephemeral by default |

---

## Docker Image Layers

> Images are built in layers. Each instruction in Dockerfile creates a new layer.

```
┌─────────────────────────────────┐
│        Application Files        │  Layer 4 (COPY)
├─────────────────────────────────┤
│        npm install packages     │  Layer 3 (RUN)
├─────────────────────────────────┤
│        package.json             │  Layer 2 (COPY)
├─────────────────────────────────┤
│        Node.js 18               │  Layer 1 (Base Image)
└─────────────────────────────────┘
```

### Benefits of Layers
- **Caching**: Unchanged layers are reused
- **Sharing**: Base images shared across images
- **Efficiency**: Only changed layers are rebuilt

---

## Dockerfile

> **Dockerfile** is a text file with a **bunch of instructions** that guide you on how to build a specific Docker image. When these instructions are executed, it creates a Docker container.

### Understanding Dockerfile

| Aspect | Description |
|--------|-------------|
| **What it is** | A text file with build instructions |
| **File name** | Must be named `Dockerfile` (no extension) |
| **Purpose** | To build Docker images, which are then converted into Docker containers |
| **Location** | Usually placed in the root of your project |

### How Dockerfile Works

```
┌──────────────────────────────────────────────────────────────────────┐
│                        Dockerfile                                     │
│     (Text file with instructions like FROM, RUN, COPY, etc.)         │
└──────────────────────────────┬───────────────────────────────────────┘
                               │
                               │ docker build
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        Docker Image                                   │
│   (Read-only template with your app, dependencies, and config)       │
└──────────────────────────────┬───────────────────────────────────────┘
                               │
                               │ docker run
                               ▼
┌──────────────────────────────────────────────────────────────────────┐
│                        Docker Container                               │
│        (Running instance - your application is now live!)            │
└──────────────────────────────────────────────────────────────────────┘
```

### Docker Container

> **Container** is like a lightweight, isolated environment where you can run an application. Containers share the host OS kernel but have isolated file systems, processes, and networks.

| Container Property | Description |
|-------------------|-------------|
| **Lightweight** | Uses MB instead of GB (unlike VMs) |
| **Fast boot** | Starts in seconds since they don't require an OS to boot |
| **Isolated** | Has own file system, processes, and network |
| **Portable** | Runs the same way everywhere |
| **Ephemeral** | Data is lost when container stops (use volumes for persistence) |

### Dockerfile Instructions

| Instruction | Definition | Example |
|-------------|------------|---------|
| **FROM** | Base image to build on | `FROM node:18-alpine` |
| **WORKDIR** | Set working directory | `WORKDIR /app` |
| **COPY** | Copy files from host | `COPY . .` |
| **RUN** | Execute command during build | `RUN npm install` |
| **ENV** | Set environment variable | `ENV NODE_ENV=production` |
| **EXPOSE** | Document exposed port | `EXPOSE 3000` |
| **CMD** | Default command to run | `CMD ["npm", "start"]` |
| **ENTRYPOINT** | Configure executable | `ENTRYPOINT ["node"]` |
| **ARG** | Build-time variable | `ARG VERSION=1.0` |
| **VOLUME** | Create mount point | `VOLUME /data` |

### Example Dockerfile

```dockerfile
# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files first (for caching)
COPY package*.json ./

# Install dependencies
RUN npm install --production

# Copy source code
COPY . .

# Set environment
ENV NODE_ENV=production

# Document port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:3000/health || exit 1

# Start command
CMD ["npm", "start"]
```

---

## Container Lifecycle

```
┌───────────┐   create   ┌───────────┐   start   ┌───────────┐
│  Image    │──────────►│  Created  │─────────►│  Running  │
└───────────┘            └───────────┘           └─────┬─────┘
                                                      │
                              ┌────────────────────────┤
                              │ pause                  │ stop
                              ▼                        ▼
                         ┌─────────┐             ┌──────────┐
                         │ Paused  │             │ Stopped  │
                         └─────────┘             └────┬─────┘
                                                      │ rm
                                                      ▼
                                                 ┌──────────┐
                                                 │ Removed  │
                                                 └──────────┘
```

---

## Docker Commands

### Image Commands
```bash
# Build image from Dockerfile
docker build -t myapp:v1 .

# List images
docker images
docker image ls

# Pull image from registry
docker pull nginx:latest

# Push image to registry
docker push username/myapp:v1

# Remove image
docker rmi myapp:v1
docker image rm myapp:v1

# Tag image
docker tag myapp:v1 myapp:latest

# Inspect image
docker image inspect myapp:v1

# Image history (show layers)
docker history myapp:v1
```

### Container Commands
```bash
# Create and start container
docker run -d -p 3000:3000 --name myapp myapp:v1

# Run options explained:
# -d         = detached (background)
# -p 3000:3000 = port mapping (host:container)
# --name     = container name
# -e VAR=val = environment variable
# -v /host:/container = volume mount
# --rm       = remove after exit

# List containers
docker ps            # running only
docker ps -a         # all containers

# Stop container
docker stop myapp

# Start stopped container
docker start myapp

# Restart container
docker restart myapp

# Remove container
docker rm myapp
docker rm -f myapp   # force remove running

# View logs
docker logs myapp
docker logs -f myapp  # follow logs

# Execute command in running container
docker exec -it myapp /bin/sh
docker exec -it myapp bash

# Copy files
docker cp myapp:/app/file.txt ./
docker cp ./file.txt myapp:/app/

# Inspect container
docker inspect myapp

# Resource usage
docker stats
```

### Cleanup Commands
```bash
# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove unused volumes
docker volume prune

# Remove everything unused
docker system prune -a
```

---

## Docker Volumes

> **Volumes** provide persistent storage for containers.

### Volume Types

| Type | Description | Example |
|------|-------------|---------|
| **Named Volume** | Docker-managed storage | `-v mydata:/app/data` |
| **Bind Mount** | Map host directory | `-v /host/path:/container/path` |
| **tmpfs Mount** | Memory-only storage | `--tmpfs /tmp` |

### Volume Commands
```bash
# Create volume
docker volume create mydata

# List volumes
docker volume ls

# Inspect volume
docker volume inspect mydata

# Use volume in container
docker run -v mydata:/app/data myapp

# Bind mount (host directory)
docker run -v $(pwd)/data:/app/data myapp

# Remove volume
docker volume rm mydata
```

---

## Docker Networking

### Network Types

| Type | Description | Use Case |
|------|-------------|----------|
| **bridge** | Default isolated network | Container-to-container (single host) |
| **host** | Use host's network directly | Performance-critical apps |
| **none** | No networking | Isolated containers |
| **overlay** | Multi-host networking | Docker Swarm/Kubernetes |

### Network Commands
```bash
# Create network
docker network create mynetwork

# List networks
docker network ls

# Connect container to network
docker network connect mynetwork mycontainer

# Run container on network
docker run --network mynetwork myapp

# Inspect network
docker network inspect mynetwork
```

---

## Docker Compose

> **Docker Compose** is a tool for defining and running multi-container applications.

### docker-compose.yml Example

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://db:5432/app
      - NODE_ENV=production
    depends_on:
      - db
      - redis
    volumes:
      - ./src:/app/src
    networks:
      - app-network
  
  db:
    image: postgres:14
    environment:
      - POSTGRES_USER=app
      - POSTGRES_PASSWORD=secret
      - POSTGRES_DB=app
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - app-network
  
  redis:
    image: redis:alpine
    networks:
      - app-network

volumes:
  db_data:

networks:
  app-network:
    driver: bridge
```

### Docker Compose Commands
```bash
# Start all services
docker-compose up
docker-compose up -d        # detached

# Stop services
docker-compose down
docker-compose down -v      # remove volumes too

# View logs
docker-compose logs
docker-compose logs -f web  # follow specific service

# Rebuild images
docker-compose build
docker-compose up --build

# Scale service
docker-compose up -d --scale web=3

# Execute command in service
docker-compose exec web sh
```

---

## Multi-Stage Builds

> Use multiple FROM statements to create smaller production images.

```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/index.js"]
```

### Benefits
- Smaller final image (no build tools)
- Faster deployments
- Reduced attack surface

---

## Docker Best Practices

### Dockerfile
1. **Use official base images** - Security and maintenance
2. **Use specific tags** - `node:18-alpine` not `node:latest`
3. **Minimize layers** - Combine RUN commands
4. **Use .dockerignore** - Exclude unnecessary files
5. **Don't run as root** - Use `USER` instruction
6. **Use multi-stage builds** - Smaller images
7. **Order commands for caching** - Static files first

### Security
1. **Scan images for vulnerabilities** - `docker scan`
2. **Use non-root user** - `USER node`
3. **Keep images updated** - Rebuild regularly
4. **Limit container resources** - `--memory`, `--cpus`
5. **Use read-only filesystem** - `--read-only`

### .dockerignore Example
```
node_modules
npm-debug.log
.git
.env
Dockerfile
docker-compose.yml
.DS_Store
```

---

[← Previous: Containerisation](08-containerisation.md) | [Next: YAML →](10-yaml.md)
