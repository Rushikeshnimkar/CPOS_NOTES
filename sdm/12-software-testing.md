---
layout: default
title: Software Testing
---

# Software Testing

[← Back to Home](../index.md)

---

## What is Software Testing?

> **Software Testing** is the process of evaluating software to find defects and verify that it meets requirements.

## Testing Levels

```
┌───────────────────────────────────────────────────┐
│              Acceptance Testing                   │ ← User perspective
├───────────────────────────────────────────────────┤
│              System Testing                       │ ← Complete system
├───────────────────────────────────────────────────┤
│              Integration Testing                  │ ← Module interaction
├───────────────────────────────────────────────────┤
│              Unit Testing                         │ ← Individual units
└───────────────────────────────────────────────────┘
```

## Types of Testing

| Type | Description |
|------|-------------|
| **Functional** | Test what system does |
| **Non-functional** | Test how system performs |
| **Black Box** | Test without knowing internals |
| **White Box** | Test with code knowledge |
| **Regression** | Ensure changes don't break |
| **Smoke** | Basic functionality check |
| **Sanity** | Specific functionality after bug fix |

## Testing Techniques

### Black Box
- Equivalence Partitioning
- Boundary Value Analysis
- Decision Table Testing
- State Transition Testing

### White Box
- Statement Coverage
- Branch Coverage
- Path Coverage
- Condition Coverage

## Test Case Template

| Field | Description |
|-------|-------------|
| Test ID | Unique identifier |
| Description | What is being tested |
| Preconditions | Setup requirements |
| Test Steps | Actions to perform |
| Test Data | Input data |
| Expected Result | Expected outcome |
| Actual Result | What happened |
| Status | Pass/Fail |

---

[← Previous: Kubernetes](11-kubernetes.md) | [Next: STLC & V-Model →](13-stlc-v-model.md)
