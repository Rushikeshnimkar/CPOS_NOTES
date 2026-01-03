---
layout: default
title: STLC and V-Model
---

# STLC and V-Model

[← Back to Home](../index.md)

---

## Software Testing Life Cycle (STLC)

### Phases

```
┌────────────────────────────────────────────┐
│          STLC PHASES                       │
├────────────────────────────────────────────┤
│ 1. Requirement Analysis                    │
│    └── Understand testable requirements    │
├────────────────────────────────────────────┤
│ 2. Test Planning                           │
│    └── Strategy, resources, schedule       │
├────────────────────────────────────────────┤
│ 3. Test Case Development                   │
│    └── Write test cases and test data      │
├────────────────────────────────────────────┤
│ 4. Environment Setup                       │
│    └── Prepare test environment            │
├────────────────────────────────────────────┤
│ 5. Test Execution                          │
│    └── Run tests, log defects              │
├────────────────────────────────────────────┤
│ 6. Test Cycle Closure                      │
│    └── Reports, metrics, sign-off          │
└────────────────────────────────────────────┘
```

## V-Model

### Diagram

```
Requirements ─────────────────────────────── Acceptance Testing
Analysis          \                      /
                   \                    /
    System ─────────\──────────────────/───── System Testing
    Design           \                /
                      \              /
        High-Level ────\────────────/──── Integration Testing
        Design          \          /
                         \        /
            Low-Level ────\──────/────── Unit Testing
            Design         \    /
                            \  /
                             \/
                          Coding
```

## Verification vs Validation

| Verification | Validation |
|--------------|------------|
| "Are we building it right?" | "Are we building the right product?" |
| Process-oriented | Product-oriented |
| Reviews, inspections | Testing |
| Before coding | After coding |

## Entry and Exit Criteria

| Phase | Entry Criteria | Exit Criteria |
|-------|----------------|---------------|
| Test Planning | Requirements available | Test plan approved |
| Test Design | Test plan approved | Test cases reviewed |
| Test Execution | Environment ready | All tests executed |
| Closure | Testing complete | Reports delivered |

---

[← Previous: Software Testing](12-software-testing.md) | [Next: Manual & Automation Testing →](14-manual-automation-testing.md)
