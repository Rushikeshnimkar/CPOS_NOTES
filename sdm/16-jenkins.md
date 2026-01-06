---
layout: default
title: Jenkins
---

# Jenkins

[← Back to Home](../index.md)

---

## What is Jenkins?

> **Jenkins** is an open-source automation server written in Java for building, testing, and deploying software through continuous integration and continuous delivery (CI/CD).

### History
- Originally developed as Hudson in 2004 at Sun Microsystems
- Renamed to Jenkins in 2011 after Oracle acquisition
- Open source under MIT License

### Why Jenkins?
- **Open Source**: Free and community-driven
- **Extensible**: 1800+ plugins available
- **Platform Independent**: Runs on any OS with Java
- **Easy Configuration**: Web-based setup
- **Distributed Builds**: Master-agent architecture

---

## Jenkins Architecture

```
┌───────────────────────────────────────────────────────────────┐
│                     Jenkins Master                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐   │
│  │ Web UI      │  │ Configuration│ │ Plugin Management   │   │
│  └─────────────┘  └─────────────┘  └─────────────────────┘   │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐   │
│  │ Build Queue │  │ Scheduling   │  │ Job Distribution    │   │
│  └─────────────┘  └─────────────┘  └─────────────────────┘   │
└────────────────────────────┬──────────────────────────────────┘
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
       ┌─────────┐     ┌─────────┐     ┌─────────┐
       │ Agent 1 │     │ Agent 2 │     │ Agent 3 │
       │ Linux   │     │ Windows │     │ macOS   │
       └─────────┘     └─────────┘     └─────────┘
```

### Master vs Agent

| Master | Agent |
|--------|-------|
| Central controller | Executes build tasks |
| Manages jobs, plugins, config | Can be specialized (OS, tools) |
| Distributes builds to agents | Connected via SSH, JNLP |
| Provides web interface | Scalable (add more agents) |

---

## Key Concepts

| Concept | Definition |
|---------|------------|
| **Job/Project** | A task configuration (build, test, deploy) |
| **Build** | One execution of a job |
| **Pipeline** | A suite of jobs defined as code |
| **Workspace** | Directory where job executes |
| **Artifact** | Output files from a build |
| **Node** | Machine where builds run (master or agent) |
| **Executor** | Thread that runs builds on a node |
| **Upstream/Downstream** | Job dependencies |

---

## CI/CD with Jenkins

### Continuous Integration (CI)

> Developers merge code frequently into a shared repository. Each merge triggers automated build and test.

```
Developer → Commit → Jenkins Build → Test → Feedback
```

### Continuous Delivery (CD)

> Code is always in deployable state. Deployment to production is manual.

### Continuous Deployment

> Every successful build is automatically deployed to production.

```
Code → Build → Test → Deploy to Staging → Deploy to Production
                                              (automatic)
```

---

## Job Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Freestyle** | Simple, UI-configured jobs | Basic builds |
| **Pipeline** | Scripted as code (Jenkinsfile) | Complex workflows |
| **Multibranch Pipeline** | Auto-creates pipelines per branch | Feature branch workflows |
| **Folder** | Organizes jobs | Project grouping |
| **Multi-configuration** | Runs with multiple configurations | Cross-platform testing |

---

## Jenkins Pipeline

> **Pipeline** is a suite of plugins supporting continuous delivery in Jenkins. Pipelines are defined as code in a `Jenkinsfile`.

### Pipeline Types

| Type | Description |
|------|-------------|
| **Declarative Pipeline** | Structured, simplified syntax (recommended) |
| **Scripted Pipeline** | Full Groovy flexibility (advanced) |

### Declarative Pipeline Example

```groovy
pipeline {
    agent any
    
    environment {
        APP_NAME = 'myapp'
        VERSION = '1.0.0'
    }
    
    options {
        timeout(time: 30, unit: 'MINUTES')
        retry(2)
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/user/repo.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'npm install'
                sh 'npm run build'
            }
        }
        
        stage('Test') {
            steps {
                sh 'npm test'
            }
            post {
                always {
                    junit 'test-results/*.xml'
                }
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                sh 'npm run deploy:staging'
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            input {
                message "Deploy to production?"
                ok "Deploy"
            }
            steps {
                sh 'npm run deploy:production'
            }
        }
    }
    
    post {
        success {
            slackSend message: "Build ${BUILD_NUMBER} succeeded!"
        }
        failure {
            slackSend message: "Build ${BUILD_NUMBER} failed!"
        }
        always {
            cleanWs()
        }
    }
}
```

---

## Pipeline Syntax

| Directive | Description | Example |
|-----------|-------------|---------|
| **pipeline** | Root of Declarative Pipeline | `pipeline { }` |
| **agent** | Where pipeline runs | `agent any`, `agent { label 'linux' }` |
| **stages** | Container for stages | `stages { stage('Build') { } }` |
| **stage** | Named phase of pipeline | `stage('Test') { steps { } }` |
| **steps** | Actions to perform | `sh 'npm test'` |
| **environment** | Environment variables | `environment { KEY = 'value' }` |
| **when** | Conditional execution | `when { branch 'main' }` |
| **post** | Actions after pipeline | `post { success { } failure { } }` |
| **input** | Wait for user input | `input { message 'Continue?' }` |
| **parallel** | Run stages in parallel | `parallel { stage('A') { } stage('B') { } }` |

---

## Build Triggers

| Trigger | Description | Configuration |
|---------|-------------|---------------|
| **Manual** | Triggered by user | Click "Build Now" |
| **Poll SCM** | Check repo for changes periodically | `H/15 * * * *` |
| **Webhook** | Repository sends notification | GitHub/GitLab webhook |
| **Upstream** | Triggered by another job | "Build after other projects" |
| **Scheduled** | Run at specified times | Cron syntax |

### Cron Syntax

```
MINUTE HOUR DOM MONTH DOW
  │      │    │    │    └── Day of Week (0-7)
  │      │    │    └────── Month (1-12)
  │      │    └─────────── Day of Month (1-31)
  │      └──────────────── Hour (0-23)
  └─────────────────────── Minute (0-59)

Examples:
H/15 * * * *    # Every 15 minutes
0 2 * * *       # Daily at 2 AM
0 0 * * 0       # Weekly on Sunday
H H(9-16) * * 1-5  # Weekdays during work hours
```

---

## Common Plugins

| Plugin | Purpose |
|--------|---------|
| **Git** | Source control integration |
| **Pipeline** | Pipeline as code |
| **Blue Ocean** | Modern UI for pipelines |
| **Docker** | Docker integration |
| **Slack/Email** | Notifications |
| **JUnit** | Test result reporting |
| **Credentials** | Secure credential storage |
| **NodeJS** | Node.js support |
| **SonarQube** | Code quality analysis |

---

## Best Practices

1. **Use Pipeline as Code** - Store Jenkinsfile in repository
2. **Keep builds fast** - Parallelize when possible
3. **Fail fast** - Run quick tests first
4. **Use agents wisely** - Offload builds from master
5. **Secure credentials** - Use credentials plugin
6. **Clean workspaces** - Prevent disk space issues
7. **Archive artifacts** - Keep important build outputs
8. **Use shared libraries** - Reuse pipeline code
9. **Monitor builds** - Set up notifications

---

## Jenkinsfile Location

```
project-root/
├── Jenkinsfile       # Pipeline definition
├── src/
├── tests/
├── Dockerfile
└── package.json
```

---

## Jenkins vs Other CI/CD

| Feature | Jenkins | GitHub Actions | GitLab CI |
|---------|---------|----------------|-----------|
| **Hosting** | Self-hosted | Cloud | Both |
| **Setup** | Complex | Easy | Easy |
| **Flexibility** | Highest | Moderate | Moderate |
| **Plugins** | 1800+ | Marketplace | Built-in |
| **Pricing** | Free | Free tier | Free tier |

---

[← Previous: Selenium](15-selenium.md) | [Back to Home →](../index.md)
