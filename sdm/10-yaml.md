---
layout: default
title: YAML
---

# YAML

[← Back to Home](../index.md)

---

## What is YAML?

> **YAML** (YAML Ain't Markup Language) is a human-readable data serialization format used for configuration files.

## Basic Syntax

```yaml
# This is a comment

# Key-value pairs
name: John Doe
age: 30
active: true

# Nested data
person:
  name: John
  address:
    city: New York
    zip: "10001"

# Lists
fruits:
  - apple
  - banana
  - cherry

# Inline list
colors: [red, green, blue]

# Inline object
person: {name: John, age: 30}
```

## Data Types

| Type | Example |
|------|---------|
| String | `name: John` or `name: "John"` |
| Number | `age: 30` or `price: 19.99` |
| Boolean | `active: true` or `enabled: false` |
| Null | `value: null` or `value: ~` |
| Date | `date: 2024-01-15` |

## Multi-line Strings

```yaml
# Literal block (preserves newlines)
description: |
  This is line 1.
  This is line 2.

# Folded block (newlines become spaces)
summary: >
  This is a long
  sentence that wraps.
```

## Anchors and Aliases

```yaml
# Define anchor
defaults: &defaults
  adapter: postgres
  host: localhost

# Use alias
development:
  <<: *defaults
  database: dev_db

production:
  <<: *defaults
  database: prod_db
```

## YAML in DevOps

### Docker Compose
```yaml
version: '3.8'
services:
  web:
    image: nginx
    ports:
      - "80:80"
```

### Kubernetes
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx:latest
```

---

[← Previous: Docker](09-docker.md) | [Next: Kubernetes →](11-kubernetes.md)
