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

### Understanding Docker Command Structure

```
docker <command> [options] <arguments>
       │          │         │
       │          │         └── What to act on (image name, container ID, etc.)
       │          └── Flags/options that modify behavior (-t, -d, -it, etc.)
       └── The action to perform (run, build, pull, etc.)
```

---

### Image Commands

#### `docker build` - Build Image from Dockerfile

```bash
docker build -t myapp:v1 .
```

| Flag | Full Form | Description | Example |
|------|-----------|-------------|---------|
| `-t` | `--tag` | **Tag the image** with a name and optional version | `-t myapp:v1` |
| `-f` | `--file` | Specify Dockerfile path (if not named "Dockerfile") | `-f Dockerfile.prod` |
| `--no-cache` | | Build without using cached layers | `--no-cache` |
| `--build-arg` | | Pass build-time variables | `--build-arg VERSION=1.0` |
| `.` | | **Build context** - the directory containing Dockerfile | `.` (current dir) |

**Examples:**
```bash
# Build with tag
docker build -t myapp:v1 .

# Build with custom Dockerfile
docker build -f Dockerfile.dev -t myapp:dev .

# Build without cache
docker build --no-cache -t myapp:v1 .

# Build with build arguments
docker build --build-arg NODE_ENV=production -t myapp:prod .
```

---

#### `docker images` / `docker image ls` - List Images

```bash
docker images
docker image ls
```

| Flag | Description | Example |
|------|-------------|---------|
| `-a` | Show all images (including intermediate) | `docker images -a` |
| `-q` | Show only image IDs | `docker images -q` |
| `--filter` | Filter images | `docker images --filter "dangling=true"` |

---

#### `docker pull` - Download Image from Registry

```bash
docker pull nginx:latest
docker pull ubuntu:22.04
```

| Component | Description |
|-----------|-------------|
| `nginx` | Image name |
| `:latest` | Tag/version (defaults to `latest` if omitted) |
| `username/image` | User's image from Docker Hub |

---

#### `docker push` - Upload Image to Registry

```bash
docker push username/myapp:v1
```

> **Note:** You must be logged in (`docker login`) and the image must be tagged with your username.

---

#### `docker rmi` - Remove Image

> **`rmi`** = **R**e**M**ove **I**mage

```bash
docker rmi myapp:v1
docker image rm myapp:v1    # Same command, newer syntax
```

| Flag | Description | Example |
|------|-------------|---------|
| `-f` | **Force** remove (even if container is using it) | `docker rmi -f myapp:v1` |

**Examples:**
```bash
# Remove single image
docker rmi nginx:latest

# Remove multiple images
docker rmi nginx:latest ubuntu:22.04

# Force remove
docker rmi -f myapp:v1

# Remove all unused images
docker image prune

# Remove ALL images (dangerous!)
docker rmi $(docker images -q)
```

---

#### `docker tag` - Tag an Image

```bash
docker tag myapp:v1 myapp:latest
docker tag myapp:v1 username/myapp:v1    # For pushing to Docker Hub
```

---

#### `docker history` - Show Image Layers

```bash
docker history myapp:v1
```

Shows each layer of the image with commands that created them.

---

### Container Commands

#### `docker run` - Create and Start Container

> This is the **most important** Docker command!

```bash
docker run [OPTIONS] IMAGE [COMMAND]
```

##### Common Flags for `docker run`

| Flag | Full Form | Description | Example |
|------|-----------|-------------|---------|
| `-d` | `--detach` | Run in **background** (detached mode) | `-d` |
| `-it` | `-i -t` | **Interactive terminal** (combines -i and -t) | `-it` |
| `-i` | `--interactive` | Keep STDIN open (for input) | `-i` |
| `-t` | `--tty` | Allocate a **pseudo-TTY** (terminal) | `-t` |
| `-p` | `--publish` | **Port mapping** (host:container) | `-p 8080:80` |
| `-P` | `--publish-all` | Publish all exposed ports to random ports | `-P` |
| `--name` | | Assign a **name** to the container | `--name myapp` |
| `-e` | `--env` | Set **environment variable** | `-e NODE_ENV=prod` |
| `-v` | `--volume` | Mount a **volume** (host:container) | `-v /data:/app/data` |
| `--rm` | | **Auto-remove** container when it exits | `--rm` |
| `-w` | `--workdir` | Set **working directory** inside container | `-w /app` |
| `--network` | | Connect to a specific network | `--network mynet` |
| `--restart` | | Restart policy (no, always, on-failure) | `--restart always` |
| `-m` | `--memory` | **Memory limit** | `-m 512m` |
| `--cpus` | | **CPU limit** | `--cpus 0.5` |

##### Understanding `-it` (Interactive Terminal)

> **`-it`** is a combination of **`-i`** (interactive) and **`-t`** (tty/terminal)

| Flag | What it does |
|------|--------------|
| `-i` | Keeps STDIN (standard input) open - you can type commands |
| `-t` | Allocates a pseudo-TTY - gives you a terminal interface |
| `-it` | Together they let you interact with the container like a terminal |

**When to use `-it`:**
```bash
# Open a shell inside a container (need -it for interaction)
docker run -it ubuntu bash

# Access running container's shell
docker exec -it mycontainer /bin/sh

# Run Python interactively
docker run -it python:3.9
```

**When to use `-d` (detached):**
```bash
# Run web server in background
docker run -d -p 80:80 nginx

# Run database in background
docker run -d --name postgres -e POSTGRES_PASSWORD=secret postgres
```

##### Port Mapping `-p` Explained

```
-p HOST_PORT:CONTAINER_PORT
   │           │
   │           └── Port inside the container
   └── Port on your machine (host)
```

**Examples:**
```bash
# Access container's port 80 via localhost:8080
docker run -p 8080:80 nginx

# Map multiple ports
docker run -p 3000:3000 -p 3001:3001 myapp

# Map to specific host IP
docker run -p 127.0.0.1:8080:80 nginx

# Random host port
docker run -p 80 nginx    # Docker assigns random host port
```

##### Volume Mounting `-v` Explained

```
-v HOST_PATH:CONTAINER_PATH[:OPTIONS]
   │           │              │
   │           │              └── Optional: ro (read-only), rw (read-write)
   │           └── Path inside container
   └── Path on your machine
```

**Examples:**
```bash
# Mount current directory
docker run -v $(pwd):/app myapp

# Mount named volume
docker run -v mydata:/app/data myapp

# Read-only mount
docker run -v /config:/app/config:ro myapp

# Mount specific file
docker run -v /path/to/file.txt:/app/config.txt myapp
```

---

#### `docker ps` - List Containers

```bash
docker ps              # Running containers only
docker ps -a           # ALL containers (including stopped)
```

| Flag | Description | Example |
|------|-------------|---------|
| `-a` | Show **all** containers (running + stopped) | `docker ps -a` |
| `-q` | Show only container **IDs** | `docker ps -q` |
| `-l` | Show **latest** created container | `docker ps -l` |
| `--filter` | Filter output | `docker ps --filter "status=exited"` |

---

#### `docker exec` - Execute Command in Running Container

```bash
docker exec [OPTIONS] CONTAINER COMMAND
```

| Flag | Description | Example |
|------|-------------|---------|
| `-it` | Interactive terminal (see above) | `docker exec -it myapp bash` |
| `-d` | Detached (run in background) | `docker exec -d myapp touch /tmp/file` |
| `-u` | Run as specific **user** | `docker exec -u root myapp bash` |
| `-w` | Set **working directory** | `docker exec -w /app myapp ls` |
| `-e` | Set **environment variable** | `docker exec -e DEBUG=1 myapp ./script.sh` |

**Common Uses:**
```bash
# Open bash shell in container
docker exec -it mycontainer bash

# Open sh shell (if bash not available)
docker exec -it mycontainer /bin/sh

# Run command as root
docker exec -u root -it mycontainer bash

# Run single command
docker exec mycontainer cat /etc/hosts

# Check running processes
docker exec mycontainer ps aux
```

---

#### `docker stop` / `docker start` / `docker restart`

```bash
docker stop myapp      # Gracefully stop (sends SIGTERM, then SIGKILL)
docker start myapp     # Start stopped container
docker restart myapp   # Stop then start
docker kill myapp      # Force stop immediately (SIGKILL)
```

| Command | Signal Sent | Use Case |
|---------|-------------|----------|
| `stop` | SIGTERM → SIGKILL | Graceful shutdown |
| `kill` | SIGKILL | Force stop immediately |
| `restart` | stop + start | Quick restart |

---

#### `docker rm` - Remove Container

```bash
docker rm myapp
docker rm container_id
```

| Flag | Description | Example |
|------|-------------|---------|
| `-f` | **Force** remove running container | `docker rm -f myapp` |
| `-v` | Remove associated **volumes** too | `docker rm -v myapp` |

**Examples:**
```bash
# Remove stopped container
docker rm myapp

# Force remove running container
docker rm -f myapp

# Remove all stopped containers
docker container prune

# Remove all containers (dangerous!)
docker rm -f $(docker ps -aq)
```

---

#### `docker logs` - View Container Logs

```bash
docker logs myapp
```

| Flag | Description | Example |
|------|-------------|---------|
| `-f` | **Follow** logs in real-time | `docker logs -f myapp` |
| `--tail` | Show last N lines | `docker logs --tail 100 myapp` |
| `-t` | Show **timestamps** | `docker logs -t myapp` |
| `--since` | Show logs since timestamp | `docker logs --since 1h myapp` |

---

#### `docker cp` - Copy Files Between Host and Container

```bash
# Container to Host
docker cp mycontainer:/app/file.txt ./local/

# Host to Container
docker cp ./local/file.txt mycontainer:/app/
```

---

### Cleanup Commands

```bash
# Remove all stopped containers
docker container prune

# Remove unused images
docker image prune

# Remove dangling images (untagged)
docker image prune -a

# Remove unused volumes
docker volume prune

# Remove unused networks
docker network prune

# Remove EVERYTHING unused (containers, images, networks, volumes)
docker system prune -a
```

| Command | What it removes |
|---------|-----------------|
| `container prune` | Stopped containers |
| `image prune` | Dangling images |
| `image prune -a` | All unused images |
| `volume prune` | Unused volumes |
| `system prune` | All unused objects |
| `system prune -a` | All unused + all images |

---

### Quick Reference: Most Used Commands

| Task | Command |
|------|---------|
| Build image | `docker build -t name:tag .` |
| Run container | `docker run -d -p 8080:80 --name myapp image` |
| Run interactively | `docker run -it image bash` |
| List containers | `docker ps -a` |
| Stop container | `docker stop container_name` |
| Remove container | `docker rm container_name` |
| Remove image | `docker rmi image_name` |
| View logs | `docker logs -f container_name` |
| Enter container | `docker exec -it container_name bash` |
| Clean up | `docker system prune -a` |

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
