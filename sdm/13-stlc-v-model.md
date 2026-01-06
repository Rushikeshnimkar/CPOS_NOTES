---
layout: default
title: STLC and V-Model
---

# STLC and V-Model

[← Back to Home](../index.md)

---

## Software Testing Life Cycle (STLC)

> **STLC** is a sequence of specific activities conducted during the testing process to ensure software quality goals are met.

### Key Difference: SDLC vs STLC

| SDLC | STLC |
|------|------|
| Focuses on development lifecycle | Focuses on testing lifecycle |
| Includes all project phases | Only testing-specific activities |
| Broader scope | Subset of SDLC |

---

## STLC Phases - Detailed

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

### Phase 1: Requirement Analysis

> **Definition**: Study and analyze requirements to identify testable requirements

| Activity | Deliverable |
|----------|-------------|
| Review SRS (Software Requirements Specification) | Requirement Traceability Matrix (RTM) |
| Identify testable requirements | Automation feasibility report |
| Clarify doubts with stakeholders | - |

**Entry Criteria**: Requirements document available
**Exit Criteria**: RTM signed off, testability identified

---

### Phase 2: Test Planning

> **Definition**: Create strategy and plan for testing activities

| Activity | Deliverable |
|----------|-------------|
| Define scope and objectives | Test Plan document |
| Estimate effort and cost | Effort estimation document |
| Identify resources and tools | Resource plan |
| Define test schedule | Test schedule |

**Key Components of Test Plan**:
- Test ID and version
- Features to be tested / not tested
- Test approach and strategy
- Entry and exit criteria
- Risk analysis and mitigation
- Schedule and resources

---

### Phase 3: Test Case Development

> **Definition**: Create detailed test cases and test data

| Activity | Deliverable |
|----------|-------------|
| Create test cases | Test cases document |
| Create test data | Test data sets |
| Review and baseline test cases | Reviewed test cases |
| Create automation scripts (if applicable) | Automation scripts |

**Good Test Case Characteristics**:
- Clear, concise, and complete
- Traceable to requirements
- Repeatable and independent
- High defect detection capability

---

### Phase 4: Test Environment Setup

> **Definition**: Prepare hardware and software environment for test execution

| Activity | Deliverable |
|----------|-------------|
| Setup hardware and software | Ready test environment |
| Create test data in environment | Test data loaded |
| Perform smoke testing | Smoke test results |

---

### Phase 5: Test Execution

> **Definition**: Execute test cases and report defects

| Activity | Deliverable |
|----------|-------------|
| Execute test cases | Test execution reports |
| Document results (Pass/Fail) | Test results |
| Log defects for failed cases | Defect reports |
| Re-test fixed defects | Updated defect status |
| Run regression tests | Regression test results |

---

### Phase 6: Test Cycle Closure

> **Definition**: Analyze testing efforts and prepare closure reports

| Activity | Deliverable |
|----------|-------------|
| Evaluate completion criteria | Test closure report |
| Document lessons learned | Lessons learned document |
| Prepare test metrics | Test metrics report |
| Archive test artifacts | Archived documents |

**Test Metrics to Report**:
- Total test cases executed
- Pass/Fail ratio
- Defects found and closed
- Defect density
- Test coverage percentage

---

## V-Model (Verification and Validation Model)

> **V-Model** is an SDLC model where development and testing activities are planned in parallel. Each development phase has a corresponding testing phase.

### Why V-Model?
- Early defect detection
- Reduces overall cost (fixing bugs early is cheaper)
- Clear correspondence between development and testing
- Better suited for projects with clear requirements

### V-Model Diagram

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

### V-Model Phase Mapping

| Development Phase | Testing Phase | Description |
|-------------------|---------------|-------------|
| **Requirements Analysis** | **Acceptance Testing** | Verify system meets business requirements |
| **System Design** | **System Testing** | Test complete system functionality |
| **High-Level Design (Architecture)** | **Integration Testing** | Test interface between modules |
| **Low-Level Design (Module)** | **Unit Testing** | Test individual components |

### Left Side (Verification)
- Requirements Analysis
- System Design
- High-Level Design
- Low-Level Design
- Coding

### Right Side (Validation)
- Unit Testing
- Integration Testing
- System Testing
- Acceptance Testing

---

## Verification vs Validation

| Aspect | Verification | Validation |
|--------|--------------|------------|
| **Question** | "Are we building the product right?" | "Are we building the right product?" |
| **Focus** | Process-oriented | Product-oriented |
| **Activities** | Reviews, inspections, walkthroughs | Testing (unit, integration, system) |
| **Timing** | During development (before coding) | After coding |
| **Goal** | Ensure conformance to specifications | Ensure product meets user needs |
| **Methods** | Static testing | Dynamic testing |
| **Examples** | Document review, code review | Functional testing, UAT |

### Static vs Dynamic Testing

| Static Testing | Dynamic Testing |
|----------------|-----------------|
| Testing without executing code | Testing by executing code |
| Reviews, walkthroughs, inspections | Unit testing, system testing |
| Finds defects early | Finds runtime defects |
| Lower cost | Higher cost |

---

## Entry and Exit Criteria

### Definition
> **Entry Criteria**: Conditions that must be met to start a testing phase
> **Exit Criteria**: Conditions that must be met to complete a testing phase

### STLC Entry/Exit Criteria

| Phase | Entry Criteria | Exit Criteria |
|-------|----------------|---------------|
| **Requirement Analysis** | Requirements available, testable | RTM created, requirements signed off |
| **Test Planning** | RTM available, requirements clear | Test plan approved |
| **Test Case Development** | Test plan approved | Test cases reviewed, test data ready |
| **Environment Setup** | Test plan available | Environment ready, smoke test passed |
| **Test Execution** | Environment ready, test cases approved | All tests executed, defects logged |
| **Test Closure** | Testing complete | Test reports delivered, sign-off obtained |

---

## Requirement Traceability Matrix (RTM)

> **RTM** is a document that maps requirements to test cases, ensuring all requirements are tested.

### RTM Example

| Req ID | Requirement | Test Case ID | Test Status | Defect ID |
|--------|-------------|--------------|-------------|-----------|
| REQ-001 | User login | TC-001, TC-002 | Pass | - |
| REQ-002 | Add to cart | TC-003, TC-004 | Fail | DEF-001 |
| REQ-003 | Payment | TC-005 | Pass | - |

### Benefits of RTM
- Ensures 100% test coverage
- Identifies gaps in requirements coverage
- Tracks requirement status throughout testing
- Helps with impact analysis for changes

---

## Test Plan vs Test Strategy

| Test Plan | Test Strategy |
|-----------|---------------|
| Project-specific document | Organization-level document |
| Created by Test Lead/Manager | Created by Project Manager |
| Detailed approach for a project | High-level approach for all projects |
| Includes schedules, resources | Includes general testing standards |

---

[← Previous: Software Testing](12-software-testing.md) | [Next: Manual & Automation Testing →](14-manual-automation-testing.md)
