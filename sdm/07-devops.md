---
layout: default
title: DevOps
---

# DevOps

[← Back to Home](../index.md)

---

## What is DevOps?

> **DevOps** is a set of practices combining software development (Dev) and IT operations (Ops) to shorten the development lifecycle while delivering features, fixes, and updates frequently.

## DevOps Culture

| Principle | Description |
|-----------|-------------|
| **Collaboration** | Dev and Ops work together |
| **Automation** | Automate repetitive tasks |
| **Continuous Improvement** | Always improving processes |
| **Customer Focus** | Quick feedback and delivery |

## DevOps Lifecycle

```
    ┌──────────────────────────────────────────────┐
    │                                              │
    ▼                                              │
┌──────┐   ┌──────┐   ┌──────┐   ┌──────┐   ┌──────┐
│ Plan │──►│Build │──►│ Test │──►│Deploy│──►│Operate│
└──────┘   └──────┘   └──────┘   └──────┘   └───┬──┘
    ▲                                          │
    │              Monitor & Feedback          │
    └──────────────────────────────────────────┘
```

## CI/CD

### Continuous Integration (CI)
- Developers merge code frequently
- Automated build and test on each commit
- Quick feedback on code quality

### Continuous Delivery (CD)
- Code always in deployable state
- Automated deployment to staging
- Manual approval for production

### Continuous Deployment
- Fully automated pipeline to production
- No manual intervention
- Requires robust testing

```
Code Commit → Build → Unit Test → Integration Test → Deploy to Staging → Deploy to Production
```

## DevOps Tools

| Category | Tools |
|----------|-------|
| **Version Control** | Git, GitHub, GitLab |
| **CI/CD** | Jenkins, GitHub Actions, GitLab CI |
| **Containerization** | Docker, Podman |
| **Orchestration** | Kubernetes, Docker Swarm |
| **Config Management** | Ansible, Terraform, Puppet |
| **Monitoring** | Prometheus, Grafana, ELK Stack |
| **Cloud** | AWS, Azure, GCP |

## Infrastructure as Code (IaC)

> Managing infrastructure through code rather than manual processes.

**Benefits:**
- Version controlled
- Reproducible environments
- Automated provisioning

**Tools:** Terraform, CloudFormation, Ansible

---

[← Previous: Jira](06-jira.md) | [Next: Containerisation →](08-containerisation.md)
