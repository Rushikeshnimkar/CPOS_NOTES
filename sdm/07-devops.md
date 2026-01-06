---
layout: default
title: DevOps
---

# DevOps

[← Back to Home](../index.md)

---

## What is DevOps?

> **DevOps** is a set of practices combining software development (Dev) and IT operations (Ops) to shorten the development lifecycle while delivering features, fixes, and updates frequently.

### Origin
- Coined in 2009 by Patrick Debois
- Born from Agile and Lean principles
- Response to siloed Dev and Ops teams

### DevOps is NOT
- A tool or technology
- A job title alone
- Just automation
- A quick fix

### DevOps Formula
```
DevOps = Culture + Automation + Measurement + Sharing (CAMS)
```

---

## DevOps Principles

| Principle | Description |
|-----------|-------------|
| **Collaboration** | Dev and Ops work together, shared responsibility |
| **Automation** | Automate repetitive tasks (build, test, deploy) |
| **Continuous Improvement** | Always improving processes (Kaizen) |
| **Customer Focus** | Quick feedback and delivery |
| **End-to-End Responsibility** | Team owns full lifecycle |
| **Fail Fast, Learn Fast** | Quick experiments, rapid feedback |

---

## DevOps Culture

> Culture is the most important aspect of DevOps transformation.

### Key Cultural Elements

| Element | Traditional | DevOps |
|---------|-------------|--------|
| **Teams** | Siloed Dev and Ops | Cross-functional teams |
| **Communication** | Ticket-based | Direct collaboration |
| **Blame** | Finger-pointing | Blameless post-mortems |
| **Risk** | Risk-averse | Calculated risk-taking |
| **Change** | Big, infrequent releases | Small, frequent changes |
| **Ownership** | "Not my problem" | Shared ownership |

---

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

### Lifecycle Stages

| Stage | Activities | Tools |
|-------|------------|-------|
| **Plan** | Requirements, backlog planning | Jira, Trello, Azure Boards |
| **Code** | Development, version control | Git, GitHub, GitLab |
| **Build** | Compile, package | Maven, Gradle, npm |
| **Test** | Automated testing | Selenium, JUnit, pytest |
| **Release** | Release management | Jenkins, GitHub Actions |
| **Deploy** | Deployment to environments | Kubernetes, Ansible |
| **Operate** | Infrastructure management | Terraform, AWS |
| **Monitor** | Logging, metrics, alerts | Prometheus, Grafana, ELK |

---

## CI/CD (Continuous Integration / Continuous Delivery)

### Continuous Integration (CI)

> **CI** is the practice where developers merge code frequently into a shared repository. Each merge triggers automated build and test.

**Benefits of CI:**
- Early bug detection
- Reduced integration problems
- Faster feedback
- Improved code quality

```
Developer → Commit → Build → Unit Test → Report
     ↑                                      │
     └────────── Feedback ──────────────────┘
```

### Continuous Delivery (CD)

> **CD** ensures code is always in a deployable state. Deployment to production requires manual approval.

**Key Aspects:**
- Automated testing at all levels
- Deployment pipeline
- Environment parity (dev ≈ staging ≈ prod)
- One-click deployment capability

### Continuous Deployment

> Every successful build is **automatically** deployed to production with no manual intervention.

**Requirements:**
- Comprehensive automated testing
- High confidence in test suite
- Feature flags for risk mitigation
- Rollback capability

```
Continuous Integration:  Code → Build → Test → (End)
Continuous Delivery:     Code → Build → Test → Deploy to Staging → [Manual] → Production
Continuous Deployment:   Code → Build → Test → Deploy to Staging → Deploy to Production (Auto)
```

---

## CI/CD Best Practices

1. **Commit frequently** - Small, incremental changes
2. **Build on every commit** - Immediate feedback
3. **Make builds fast** - Target < 10 minutes
4. **Test in production-like environments** - Reduce surprises
5. **Make deployment easy** - One-click or automated
6. **Keep pipelines green** - Fix failures immediately
7. **Version everything** - Code, config, infrastructure

---

## DevOps Tools by Category

| Category | Tools | Purpose |
|----------|-------|---------|
| **Version Control** | Git, GitHub, GitLab, Bitbucket | Code management, collaboration |
| **CI/CD** | Jenkins, GitHub Actions, GitLab CI, CircleCI | Automation pipelines |
| **Containerization** | Docker, Podman | Package applications |
| **Orchestration** | Kubernetes, Docker Swarm | Container management |
| **Config Management** | Ansible, Terraform, Puppet, Chef | Infrastructure automation |
| **Monitoring** | Prometheus, Grafana, Datadog | Metrics and visualization |
| **Logging** | ELK Stack (Elasticsearch, Logstash, Kibana) | Log aggregation |
| **Cloud** | AWS, Azure, GCP | Infrastructure services |
| **Artifact Repository** | Nexus, Artifactory, Docker Hub | Store build artifacts |

---

## Infrastructure as Code (IaC)

> **IaC** is managing and provisioning infrastructure through code rather than manual processes.

### Definition
```
Infrastructure as Code = Version Controlled + Automated + Reproducible Infrastructure
```

### Benefits of IaC
- **Version Controlled**: Track changes, rollback
- **Reproducible**: Same config = same result
- **Testable**: Validate before deployment
- **Documented**: Code IS documentation
- **Scalable**: Easily replicate environments

### IaC Approaches

| Approach | Description | Tools |
|----------|-------------|-------|
| **Declarative** | Define desired state, tool figures out how | Terraform, CloudFormation |
| **Imperative** | Define exact steps to execute | Ansible, scripts |
| **Mutable** | Update existing infrastructure | Traditional approach |
| **Immutable** | Replace infrastructure entirely | Container-based, AMIs |

### IaC Example (Terraform)

```hcl
# Define AWS EC2 instance
resource "aws_instance" "web_server" {
  ami           = "ami-12345678"
  instance_type = "t2.micro"
  
  tags = {
    Name        = "Web Server"
    Environment = "Production"
  }
}
```

---

## DevOps Metrics

> Measuring DevOps success with key metrics.

### DORA Metrics (DevOps Research and Assessment)

| Metric | Definition | Elite Performance |
|--------|------------|-------------------|
| **Deployment Frequency** | How often you deploy to production | Multiple times per day |
| **Lead Time for Changes** | Time from commit to production | Less than 1 hour |
| **Change Failure Rate** | % of deployments causing failures | 0-15% |
| **Time to Restore Service** | Time to recover from incidents | Less than 1 hour |

### Other Important Metrics

| Metric | Description |
|--------|-------------|
| **Mean Time to Recovery (MTTR)** | Average time to recover from failure |
| **Mean Time Between Failures (MTBF)** | Average time between failures |
| **Cycle Time** | Time from work start to delivery |
| **Test Coverage** | Percentage of code covered by tests |

---

## DevOps Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| **DevOps as a title** | Creating a "DevOps team" | Embed DevOps in all teams |
| **Tool obsession** | Focus on tools over culture | Start with culture change |
| **No testing** | Skipping automated tests | Test automation is essential |
| **Manual deployments** | Human-error-prone releases | Automate everything |
| **Environment drift** | Dev ≠ Prod | Use IaC, containers |

---

## DevOps vs Traditional IT

| Aspect | Traditional | DevOps |
|--------|-------------|--------|
| **Deployment** | Monthly/Quarterly | Daily/Hourly |
| **Team Structure** | Siloed | Cross-functional |
| **Change Management** | Heavyweight | Lightweight |
| **Risk Appetite** | Risk-averse | Calculated risk |
| **Feedback** | Slow | Fast |
| **Automation** | Limited | Extensive |

---

[← Previous: Jira](06-jira.md) | [Next: Containerisation →](08-containerisation.md)
