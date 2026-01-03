---
layout: default
title: Jenkins
---

# Jenkins

[← Back to Home](../index.md)

---

## What is Jenkins?

> **Jenkins** is an open-source automation server for building, testing, and deploying software.

## Key Features

| Feature | Description |
|---------|-------------|
| **CI/CD** | Automate build and deployment |
| **Plugins** | 1800+ plugins available |
| **Pipeline** | Define build as code |
| **Distributed** | Master-agent architecture |

## Jenkins Pipeline

```groovy
pipeline {
    agent any
    
    environment {
        APP_NAME = 'myapp'
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/user/repo.git'
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
        }
        
        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                sh 'npm run deploy'
            }
        }
    }
    
    post {
        success {
            echo 'Build successful!'
        }
        failure {
            echo 'Build failed!'
        }
    }
}
```

## Pipeline Concepts

| Concept | Description |
|---------|-------------|
| **Pipeline** | Complete build definition |
| **Stage** | Major phase (Build, Test, Deploy) |
| **Step** | Single task within stage |
| **Agent** | Where pipeline runs |
| **Post** | Actions after pipeline completes |

## Common Plugins

| Plugin | Purpose |
|--------|---------|
| Git | Source control integration |
| Pipeline | Pipeline as code |
| Docker | Container integration |
| Slack | Notifications |
| JUnit | Test reports |

## Jenkinsfile Location

```
project-root/
├── Jenkinsfile       # Pipeline definition
├── src/
├── tests/
└── package.json
```

---

[← Previous: Selenium](15-selenium.md) | [Back to Home →](../index.md)
