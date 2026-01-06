---
layout: default
title: YAML
---

# YAML

[← Back to Home](../index.md)

---

## What is YAML?

> **YAML** (YAML Ain't Markup Language) is a human-readable data serialization format used for configuration files and data exchange.

### History
- Created in 2001 by Clark Evans
- Originally meant "Yet Another Markup Language"
- Renamed to emphasize data over document markup

### Why YAML?
- **Human-Readable**: Easy to read and write
- **Minimal Syntax**: Less verbose than XML/JSON
- **Widely Used**: Docker, Kubernetes, CI/CD, Ansible
- **Data-Focused**: Represents data structures clearly
- **JSON Compatible**: Any JSON is valid YAML

### YAML vs JSON vs XML

| Aspect | YAML | JSON | XML |
|--------|------|------|-----|
| **Readability** | High | Medium | Low |
| **Verbosity** | Low | Medium | High |
| **Comments** | Yes | No | Yes |
| **Data Types** | Rich | Limited | String-based |
| **Use Case** | Config files | APIs, data | Documents |

---

## Basic Syntax

### Key-Value Pairs
```yaml
# Simple key-value
name: John Doe
age: 30
active: true
salary: 75000.50
```

### Indentation Rules
- Use **spaces only** (not tabs)
- Consistent indentation (2 or 4 spaces)
- Indentation defines structure

---

## Data Types

| Type | Example | Notes |
|------|---------|-------|
| **String** | `name: John` or `name: "John"` | Quotes optional |
| **Integer** | `age: 30` | Numeric value |
| **Float** | `price: 19.99` | Decimal value |
| **Boolean** | `active: true` | true, false, yes, no |
| **Null** | `value: null` or `value: ~` | Empty value |
| **Date** | `date: 2024-01-15` | ISO 8601 format |
| **Datetime** | `time: 2024-01-15T14:30:00Z` | With time |

### String Quoting

```yaml
# Plain string (usually works)
message: Hello World

# Single quotes (literal, no escapes)
path: 'C:\Users\name'

# Double quotes (interprets escapes)
greeting: "Hello\nWorld"

# When quotes are needed:
special: "yes"        # Without quotes, parsed as boolean
colon: "key: value"   # Contains colon
number: "12345"       # Keep as string
```

---

## Collections

### Lists (Sequences)

```yaml
# Block style (preferred)
fruits:
  - apple
  - banana
  - cherry

# Inline style
colors: [red, green, blue]

# Nested lists
matrix:
  - [1, 2, 3]
  - [4, 5, 6]
```

### Objects (Mappings)

```yaml
# Block style (preferred)
person:
  name: John
  age: 30
  address:
    city: New York
    zip: "10001"

# Inline style
person: {name: John, age: 30}
```

### Complex Nested Structures

```yaml
company:
  name: TechCorp
  departments:
    - name: Engineering
      employees:
        - name: Alice
          role: Developer
        - name: Bob
          role: DevOps
    - name: Marketing
      employees:
        - name: Carol
          role: Manager
```

---

## Multi-line Strings

### Literal Block (|)
> Preserves newlines exactly

```yaml
description: |
  This is line 1.
  This is line 2.
  
  This is after a blank line.
```
Result: `"This is line 1.\nThis is line 2.\n\nThis is after a blank line.\n"`

### Folded Block (>)
> Converts newlines to spaces

```yaml
summary: >
  This is a long
  sentence that will
  be folded into one line.
```
Result: `"This is a long sentence that will be folded into one line.\n"`

### Block Modifiers

| Modifier | Effect | Example |
|----------|--------|---------|
| `\|` | Keep newlines | `|` |
| `>` | Fold newlines to spaces | `>` |
| `\|-` | No trailing newline | `|-` |
| `>-` | Fold, no trailing newline | `>-` |
| `\|+` | Keep trailing newlines | `|+` |

---

## Anchors and Aliases

> Reuse YAML content to avoid repetition (DRY principle).

```yaml
# Define anchor with &
defaults: &defaults
  adapter: postgres
  host: localhost
  port: 5432

# Use alias with *
development:
  <<: *defaults
  database: dev_db

staging:
  <<: *defaults
  database: staging_db

production:
  <<: *defaults
  host: prod-server
  database: prod_db
```

### Merge Key (<<)
The `<<` key merges the anchored content into the current mapping.

---

## Comments

```yaml
# This is a comment

name: John  # Inline comment

# Multi-line comments
# are written as
# multiple single-line comments
```

---

## Common Gotchas

| Issue | Problem | Solution |
|-------|---------|----------|
| **Tabs** | Invalid indentation | Use spaces only |
| **Colon in string** | Parsed as key-value | Quote the string |
| **Yes/No** | Parsed as boolean | Quote if string needed |
| **Numbers** | Parsed as numeric | Quote to keep as string |
| **Special chars** | May cause errors | Quote the string |

### Examples of Gotchas

```yaml
# WRONG - "yes" becomes true
answer: yes

# RIGHT - keep as string
answer: "yes"

# WRONG - colon creates nested object
message: Note: this is important

# RIGHT - quote the value
message: "Note: this is important"

# WRONG - becomes integer 12345
zipcode: 12345

# RIGHT - keep as string
zipcode: "12345"
```

---

## YAML in DevOps

### Docker Compose
```yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    environment:
      - DEBUG=false
    volumes:
      - ./html:/usr/share/nginx/html
```

### Kubernetes
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  containers:
    - name: nginx
      image: nginx:latest
      ports:
        - containerPort: 80
      resources:
        limits:
          memory: "128Mi"
          cpu: "500m"
```

### GitHub Actions
```yaml
name: CI Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: npm test
```

### Ansible Playbook
```yaml
---
- name: Setup Web Server
  hosts: webservers
  become: true
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
    - name: Start nginx
      service:
        name: nginx
        state: started
```

---

## YAML Validation

### Online Validators
- [yamllint.com](https://yamllint.com)
- [YAML Lint](http://www.yamllint.com/)

### Command Line
```bash
# Install yamllint
pip install yamllint

# Validate file
yamllint config.yaml

# Python validation
python -c "import yaml; yaml.safe_load(open('config.yaml'))"
```

---

## Best Practices

1. **Use consistent indentation** - 2 spaces is common
2. **Quote strings when needed** - Avoid parsing issues
3. **Use anchors for repetition** - DRY principle
4. **Add comments** - Document complex configurations
5. **Validate before use** - Catch syntax errors early
6. **Use explicit data types** - `!!str 123` forces string
7. **Keep files organized** - Logical structure

---

[← Previous: Docker](09-docker.md) | [Next: Kubernetes →](11-kubernetes.md)
