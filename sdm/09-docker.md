---
layout: default
title: Docker
---

# Docker

[← Back to Home](../index.md)

---

## What is Docker?

> **Docker** is a platform for developing, shipping, and running applications in containers.

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

## Docker Objects

| Object | Description |
|--------|-------------|
| **Image** | Read-only template with instructions |
| **Container** | Runnable instance of an image |
| **Volume** | Persistent data storage |
| **Network** | Container communication |

## Dockerfile

```dockerfile
# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source code
COPY . .

# Expose port
EXPOSE 3000

# Start command
CMD ["npm", "start"]
```

## Docker Commands

```bash
# Images
docker build -t myapp .          # Build image
docker images                     # List images
docker pull nginx                 # Pull from registry
docker push myapp                 # Push to registry
docker rmi image_name             # Remove image

# Containers
docker run -d -p 3000:3000 myapp  # Run container
docker ps                         # List running
docker ps -a                      # List all
docker stop container_id          # Stop container
docker rm container_id            # Remove container
docker logs container_id          # View logs
docker exec -it container bash    # Enter container

# Cleanup
docker system prune               # Remove unused
```

## Docker Compose

```yaml
# docker-compose.yml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgres://db:5432/app
  
  db:
    image: postgres:14
    volumes:
      - db_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=secret

volumes:
  db_data:
```

```bash
docker-compose up -d              # Start services
docker-compose down               # Stop services
docker-compose logs               # View logs
```

## Docker Best Practices

1. Use official base images
2. Minimize layers
3. Use `.dockerignore`
4. Don't run as root
5. Use multi-stage builds
6. Tag images properly

---

[← Previous: Containerisation](08-containerisation.md) | [Next: YAML →](10-yaml.md)
