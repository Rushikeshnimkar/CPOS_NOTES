---
layout: default
title: Kubernetes
---

# Kubernetes

[← Back to Home](../index.md)

---

## What is Kubernetes?

> **Kubernetes (K8s)** is an open-source container orchestration platform for automating deployment, scaling, and management of containerized applications.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Control Plane                        │
│  ┌──────────────┐ ┌──────────────┐ ┌───────────────┐   │
│  │ API Server   │ │ Scheduler    │ │ Controller   │   │
│  └──────────────┘ └──────────────┘ │ Manager      │   │
│  ┌──────────────┐                   └───────────────┘   │
│  │    etcd      │                                       │
│  └──────────────┘                                       │
└─────────────────────────────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
     ┌─────────┐    ┌─────────┐    ┌─────────┐
     │  Node   │    │  Node   │    │  Node   │
     │ ┌─────┐ │    │ ┌─────┐ │    │ ┌─────┐ │
     │ │ Pod │ │    │ │ Pod │ │    │ │ Pod │ │
     │ └─────┘ │    │ └─────┘ │    │ └─────┘ │
     │ kubelet │    │ kubelet │    │ kubelet │
     └─────────┘    └─────────┘    └─────────┘
```

## Core Components

| Component | Description |
|-----------|-------------|
| **Pod** | Smallest deployable unit, one or more containers |
| **Service** | Stable network endpoint for pods |
| **Deployment** | Manages ReplicaSet and pod updates |
| **ConfigMap** | Configuration data |
| **Secret** | Sensitive data (passwords, tokens) |
| **Namespace** | Virtual cluster for isolation |

## Pod Definition

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
```

## Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:latest
          ports:
            - containerPort: 80
```

## Service

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 80
  type: LoadBalancer
```

## kubectl Commands

```bash
# Get resources
kubectl get pods
kubectl get services
kubectl get deployments

# Create/Apply
kubectl apply -f deployment.yaml
kubectl create namespace dev

# Describe
kubectl describe pod nginx-pod

# Logs
kubectl logs pod-name

# Exec into pod
kubectl exec -it pod-name -- /bin/bash

# Delete
kubectl delete pod pod-name
kubectl delete -f deployment.yaml
```

---

[← Previous: YAML](10-yaml.md) | [Next: Software Testing →](12-software-testing.md)
