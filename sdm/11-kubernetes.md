---
layout: default
title: Kubernetes
---

# Kubernetes

[← Back to Home](../index.md)

---

## What is Kubernetes?

> **Kubernetes (K8s)** is an open-source container orchestration platform for automating deployment, scaling, and management of containerized applications.

### Why Kubernetes?
- **Automatic scaling**: Scale applications based on demand
- **Self-healing**: Auto-restart failed containers
- **Load balancing**: Distribute traffic across containers
- **Rollouts & Rollbacks**: Zero-downtime deployments
- **Secret management**: Securely store sensitive data
- **Portability**: Run on any cloud or on-premises

### Kubernetes vs Docker

| Aspect | Docker | Kubernetes |
|--------|--------|------------|
| **Purpose** | Containerization platform | Container orchestration |
| **Scope** | Single container management | Cluster-wide management |
| **Scaling** | Manual | Automatic |
| **Use Case** | Build & run containers | Orchestrate containers at scale |

---

## Kubernetes Architecture

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

---

## Control Plane Components

> The Control Plane makes global decisions about the cluster and detects/responds to cluster events.

| Component | Definition | Function |
|-----------|------------|----------|
| **API Server** | Front-end for Kubernetes control plane | Exposes Kubernetes API, handles all REST operations |
| **etcd** | Distributed key-value store | Stores all cluster data (state, config) |
| **Scheduler** | Watches for newly created Pods | Assigns Pods to Nodes based on resources |
| **Controller Manager** | Runs controller processes | Handles node failures, replication, endpoints |
| **Cloud Controller Manager** | Cloud-specific controllers | Manages load balancers, storage, routes |

---

## Node Components

> Nodes are worker machines that run containerized applications.

| Component | Definition | Function |
|-----------|------------|----------|
| **kubelet** | Agent on each node | Ensures containers run in Pods |
| **kube-proxy** | Network proxy on each node | Maintains network rules, enables communication |
| **Container Runtime** | Software that runs containers | Docker, containerd, CRI-O |

---

## Core Kubernetes Objects

| Object | Definition | Use Case |
|--------|------------|----------|
| **Pod** | Smallest deployable unit, one or more containers | Run application containers |
| **Service** | Stable network endpoint for pods | Expose applications, load balancing |
| **Deployment** | Manages ReplicaSet and pod updates | Declarative updates, rollbacks |
| **ReplicaSet** | Ensures specified number of pod replicas | High availability |
| **ConfigMap** | Configuration data in key-value pairs | Externalize configuration |
| **Secret** | Sensitive data (passwords, tokens) | Secure credential storage |
| **Namespace** | Virtual cluster for isolation | Environment separation (dev, prod) |
| **Ingress** | HTTP/HTTPS route to services | External access, SSL termination |

---

## Pod Definition

> **Pod** is the smallest deployable unit in Kubernetes. It can contain one or more containers that share storage and network.

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
      resources:
        requests:
          memory: "64Mi"
          cpu: "250m"
        limits:
          memory: "128Mi"
          cpu: "500m"
```

### Pod Lifecycle States

| State | Definition |
|-------|------------|
| **Pending** | Pod accepted but containers not yet created |
| **Running** | Pod bound to node, all containers running |
| **Succeeded** | All containers terminated successfully |
| **Failed** | At least one container failed |
| **Unknown** | State cannot be determined |

---

## Deployment

> **Deployment** provides declarative updates for Pods and ReplicaSets.

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
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
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

### Deployment Strategies

| Strategy | Definition | Use Case |
|----------|------------|----------|
| **RollingUpdate** | Gradually replaces old pods with new | Zero-downtime deployments |
| **Recreate** | Kills all old pods before creating new | When downtime is acceptable |
| **Blue/Green** | Run two environments, switch traffic | Quick rollback capability |
| **Canary** | Route small percentage to new version | Test with real traffic |

---

## Service Types

> **Service** is an abstraction that defines a logical set of Pods and a policy to access them.

| Type | Definition | Use Case |
|------|------------|----------|
| **ClusterIP** | Internal cluster IP (default) | Internal communication |
| **NodePort** | Exposes service on each node's IP | Development, debugging |
| **LoadBalancer** | Cloud provider load balancer | Production external access |
| **ExternalName** | Maps service to external DNS | Access external services |

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

---

## Scaling in Kubernetes

### Horizontal Pod Autoscaler (HPA)

> Automatically scales pods based on CPU/memory utilization

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: nginx-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: nginx-deployment
  minReplicas: 2
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Scaling Types

| Type | Definition |
|------|------------|
| **Horizontal Scaling** | Add more pod replicas |
| **Vertical Scaling** | Increase pod resources (CPU, memory) |
| **Cluster Scaling** | Add more nodes to cluster |

---

## kubectl Commands

```bash
# Cluster Info
kubectl cluster-info
kubectl get nodes

# Pods
kubectl get pods
kubectl get pods -o wide
kubectl describe pod nginx-pod
kubectl logs pod-name
kubectl exec -it pod-name -- /bin/bash

# Deployments
kubectl get deployments
kubectl apply -f deployment.yaml
kubectl rollout status deployment/nginx
kubectl rollout undo deployment/nginx
kubectl scale deployment nginx --replicas=5

# Services
kubectl get services
kubectl expose deployment nginx --port=80 --type=LoadBalancer

# Namespaces
kubectl get namespaces
kubectl create namespace dev
kubectl get pods -n dev

# ConfigMaps & Secrets
kubectl create configmap config --from-file=config.txt
kubectl create secret generic secret --from-literal=password=pass123

# Delete
kubectl delete pod pod-name
kubectl delete -f deployment.yaml
```

---

## Key Kubernetes Concepts

| Concept | Definition |
|---------|------------|
| **Desired State** | What you want the cluster to look like |
| **Actual State** | Current state of the cluster |
| **Reconciliation** | Process of matching actual state to desired state |
| **Label** | Key-value pairs attached to objects for identification |
| **Selector** | Query to filter objects based on labels |
| **Annotation** | Non-identifying metadata for objects |

---

## Best Practices

1. **Use namespaces** for environment isolation
2. **Set resource limits** to prevent resource exhaustion
3. **Use liveness and readiness probes** for health checks
4. **Externalize configuration** using ConfigMaps/Secrets
5. **Use Deployments** instead of ReplicaSets directly
6. **Implement RBAC** for access control
7. **Use Ingress** for external HTTP/HTTPS traffic

---

[← Previous: YAML](10-yaml.md) | [Next: Software Testing →](12-software-testing.md)
