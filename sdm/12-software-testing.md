---
layout: default
title: Software Testing
---

# Software Testing

[← Back to Home](../index.md)

---

## What is Software Testing?

> **Software Testing** is the process of evaluating software to find defects and verify that it meets requirements.

### Formal Definition (IEEE)
> Software testing is "the process of executing a program or system with the intent of finding errors" — Glenford Myers

### Why is Testing Important?
- **Quality Assurance**: Ensures software meets quality standards
- **Cost Reduction**: Finding bugs early reduces fix costs (10x-100x cheaper)
- **Customer Satisfaction**: Reliable software builds trust
- **Security**: Identifies vulnerabilities before exploitation
- **Compliance**: Meets regulatory and industry standards

---

## Seven Principles of Software Testing (ISTQB)

| # | Principle | Description |
|---|-----------|-------------|
| 1 | **Testing shows presence of defects** | Testing can show bugs exist, but cannot prove there are none |
| 2 | **Exhaustive testing is impossible** | Cannot test all input combinations; use risk-based testing |
| 3 | **Early testing** | Start testing as early as possible in SDLC |
| 4 | **Defect clustering** | Small number of modules contain most defects (Pareto 80/20) |
| 5 | **Pesticide paradox** | Same tests repeatedly won't find new bugs; update test cases |
| 6 | **Testing is context dependent** | Different domains need different testing approaches |
| 7 | **Absence of errors fallacy** | Bug-free software is useless if it doesn't meet user needs |

---

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

### Detailed Explanation of Testing Levels

| Level | Definition | Responsibility | Example |
|-------|------------|----------------|---------|
| **Unit Testing** | Testing individual components/functions in isolation | Developers | Testing a `calculateTax()` function |
| **Integration Testing** | Testing interaction between integrated modules | Developers/Testers | Testing API with database connection |
| **System Testing** | Testing complete, integrated system | Test Team | End-to-end order processing |
| **Acceptance Testing** | Testing if system meets business requirements | Users/Clients | UAT for new feature release |

---

## Functional and Non-Functional Requirements

### What are Software Requirements?

> **Software Requirements** are the documented needs and expectations that a software system must fulfill to satisfy its stakeholders.

Requirements are broadly categorized into two types:

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        SOFTWARE REQUIREMENTS                            │
├─────────────────────────────────┬───────────────────────────────────────┤
│     FUNCTIONAL REQUIREMENTS     │    NON-FUNCTIONAL REQUIREMENTS        │
│                                 │                                       │
│  • What the system DOES         │  • How the system PERFORMS            │
│  • Features & Functions         │  • Quality Attributes                 │
│  • Business Logic               │  • Constraints & Standards            │
└─────────────────────────────────┴───────────────────────────────────────┘
```

---

### Functional Requirements (FR)

> **Functional Requirements** define the specific behavior, features, and functions that a software system must perform to meet user needs.

#### Characteristics of Functional Requirements
- Describe **what** the system should do
- Are directly visible to end users
- Can be tested with specific inputs and expected outputs
- Derived from business needs and user stories

#### Examples of Functional Requirements

| Category | Functional Requirement Example |
|----------|-------------------------------|
| **User Authentication** | System shall allow users to login with email and password |
| **Data Processing** | System shall calculate total order amount including taxes |
| **Business Rules** | System shall not allow orders below ₹100 minimum value |
| **User Interface** | System shall display order history for last 12 months |
| **External Interface** | System shall integrate with payment gateway API |
| **Reporting** | System shall generate monthly sales reports in PDF format |

#### Functional Requirements Template

| Field | Description | Example |
|-------|-------------|---------|
| **FR ID** | Unique identifier | FR-001 |
| **Description** | Clear statement of functionality | User shall be able to reset password via email link |
| **Priority** | MoSCoW (Must/Should/Could/Won't) | Must Have |
| **Source** | Origin of requirement | User Story US-023 |
| **Acceptance Criteria** | How to verify completion | Email received within 2 minutes, link expires in 24 hours |

---

### Non-Functional Requirements (NFR)

> **Non-Functional Requirements** define the quality attributes, constraints, and performance characteristics that the system must exhibit.

#### Categories of Non-Functional Requirements

| Category | Definition | Metric Example |
|----------|------------|----------------|
| **Performance** | Speed and throughput of system | Response time < 2 seconds |
| **Scalability** | Ability to handle growth | Support 10,000 concurrent users |
| **Reliability** | System uptime and consistency | 99.9% availability (SLA) |
| **Availability** | Accessible when needed | 24/7 operation with < 1 hour downtime/month |
| **Security** | Protection from threats | Data encryption (AES-256), OAuth 2.0 |
| **Usability** | Ease of use | New user completes task in < 5 minutes |
| **Maintainability** | Ease of modification | Code coverage > 80%, modular architecture |
| **Portability** | Platform independence | Works on Chrome, Firefox, Safari, Edge |
| **Compatibility** | Works with other systems | Supports Windows 10+, macOS 12+, Linux |
| **Compliance** | Regulatory adherence | GDPR compliant, HIPAA certified |

#### Examples of Non-Functional Requirements

| NFR Type | Requirement Statement |
|----------|----------------------|
| **Performance** | The system shall load the homepage within 3 seconds on 4G networks |
| **Scalability** | The system shall scale horizontally to handle 100% traffic increase |
| **Security** | All passwords shall be stored using bcrypt hashing with salt |
| **Reliability** | Mean Time Between Failures (MTBF) shall be > 720 hours |
| **Usability** | 90% of users shall complete checkout without assistance |
| **Maintainability** | New developers shall be productive within 1 week |

---

### Functional vs Non-Functional Requirements Comparison

| Aspect | Functional Requirements | Non-Functional Requirements |
|--------|------------------------|----------------------------|
| **Focus** | What the system does | How well the system does it |
| **Visibility** | Directly visible to users | Often invisible (background quality) |
| **Derivation** | From user stories/use cases | From quality attributes/SLAs |
| **Testing** | Functional testing | Performance, security, load testing |
| **Documentation** | Use cases, user stories | SLAs, quality standards |
| **Example** | "User can upload profile picture" | "Image upload completes in < 5 seconds" |
| **Measurability** | Pass/Fail (works or doesn't) | Metrics (response time, uptime %) |

---

### Importance in Software Testing

| Requirement Type | Testing Approach | Test Types |
|------------------|-----------------|------------|
| **Functional** | Verify features work correctly | Unit, Integration, System, UAT |
| **Non-Functional** | Verify quality attributes | Performance, Load, Stress, Security, Usability |

> **Key Insight**: A system can meet all functional requirements but still fail if non-functional requirements are not met. For example, a login feature (FR) that takes 30 seconds to respond fails the performance (NFR) expectation.

---

## Types of Testing

### Functional vs Non-Functional Testing

| Type | Description | Focus |
|------|-------------|-------|
| **Functional** | Test what system does | Features, business logic |
| **Non-functional** | Test how system performs | Performance, security, usability |

### Testing Categories

| Type | Definition | Example |
|------|------------|---------|
| **Black Box** | Test without knowing internal code structure | User login from UI |
| **White Box** | Test with full code knowledge | Code path testing |
| **Grey Box** | Partial knowledge of internals | API testing with DB awareness |
| **Regression** | Re-test after changes to ensure nothing broke | After bug fix, run full suite |
| **Smoke** | Quick test of critical functionality | Verify app launches |
| **Sanity** | Focused test on specific functionality | Test only login after login fix |
| **Ad-hoc** | Unplanned, informal testing | Exploratory click-through |
| **Exploratory** | Simultaneous learning, design, and execution | New feature discovery testing |

### Alpha vs Beta Testing

| Aspect | Alpha Testing | Beta Testing |
|--------|---------------|--------------|
| **Location** | Developer's site | User's site |
| **Testers** | Internal employees | External users |
| **Environment** | Controlled | Real-world |
| **Stage** | Before beta | After alpha |
| **Focus** | Functionality | Real usage patterns |

---

## Defect Terminology

> **Defect (Bug)**: A flaw in the software that causes incorrect or unexpected behavior.

| Term | Definition |
|------|------------|
| **Error** | Human mistake made during coding |
| **Bug/Defect** | Error discovered in code |
| **Failure** | Deviation from expected behavior during execution |
| **Fault** | Incorrect step, process, or data definition |

### Defect Severity vs Priority

| Severity | Definition | Example |
|----------|------------|---------|
| **Critical** | System crash, data loss | Application won't start |
| **Major** | Major feature not working | Cannot submit form |
| **Minor** | Minor feature issue | Typo in label |
| **Trivial** | Cosmetic issue | Wrong font color |

| Priority | Definition | Action |
|----------|------------|--------|
| **High** | Must fix immediately | Fix before release |
| **Medium** | Fix in next build | Schedule for current sprint |
| **Low** | Fix when time permits | Backlog item |

### Defect Lifecycle

```
┌──────┐    ┌────────┐    ┌──────────┐    ┌───────┐    ┌────────┐
│ New  │───►│ Assign │───►│ In Work  │───►│ Fixed │───►│ Retest │
└──────┘    └────────┘    └──────────┘    └───────┘    └────┬───┘
                                                           │
                                              ┌────────────┴────────────┐
                                              ▼                         ▼
                                         ┌────────┐               ┌──────────┐
                                         │ Closed │               │ Reopened │
                                         └────────┘               └──────────┘
```

---

## Testing Techniques

### Black Box Techniques

| Technique | Description | When to Use |
|-----------|-------------|-------------|
| **Equivalence Partitioning** | Divide inputs into equivalent groups; test one from each | Large input ranges |
| **Boundary Value Analysis** | Test at boundary edges (min, min-1, max, max+1) | Numeric inputs |
| **Decision Table Testing** | Test combinations of inputs and actions | Complex business rules |
| **State Transition Testing** | Test transitions between states | Workflows, state machines |
| **Use Case Testing** | Test based on user scenarios | End-to-end flows |
| **Error Guessing** | Use experience to guess error-prone areas | Any testing phase |

#### Equivalence Partitioning Example
```
Input: Age (valid range 18-65)
Partitions:
  Invalid: age < 18 → Test with 10
  Valid:   18 ≤ age ≤ 65 → Test with 30
  Invalid: age > 65 → Test with 80
```

#### Boundary Value Analysis Example
```
Valid range: 18-65
Test values: 17, 18, 19, 64, 65, 66
```

### White Box Techniques

| Technique | Description | Coverage Goal |
|-----------|-------------|---------------|
| **Statement Coverage** | Every statement executed at least once | 100% statements |
| **Branch Coverage** | Every decision branch (true/false) executed | 100% branches |
| **Path Coverage** | Every possible path through code | All paths |
| **Condition Coverage** | Each condition in decision tested for true/false | All conditions |
| **MC/DC** | Modified Condition/Decision Coverage | Aviation/safety-critical |

---

## Test Case Template

| Field | Description | Example |
|-------|-------------|---------|
| **Test ID** | Unique identifier | TC_LOGIN_001 |
| **Test Name** | Descriptive name | Valid user login |
| **Description** | What is being tested | Verify successful login with valid credentials |
| **Preconditions** | Setup requirements | User account exists, browser open |
| **Test Steps** | Actions to perform | 1. Enter username 2. Enter password 3. Click login |
| **Test Data** | Input data | username: user1, password: pass123 |
| **Expected Result** | Expected outcome | User redirected to dashboard |
| **Actual Result** | What happened | [Filled during execution] |
| **Status** | Pass/Fail/Blocked | [Filled during execution] |
| **Priority** | High/Medium/Low | High |

---

## Test Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| **Defect Density** | Defects / Size (KLOC) | Code quality indicator |
| **Defect Detection Efficiency** | (Defects found in testing / Total defects) × 100 | Testing effectiveness |
| **Test Coverage** | (Statements covered / Total statements) × 100 | Code coverage |
| **Test Case Effectiveness** | (Defects found / Test cases executed) × 100 | Test case quality |
| **Defect Removal Efficiency** | (Defects removed / Total defects) × 100 | Process effectiveness |

---

## Test Documentation

| Document | Purpose |
|----------|---------|
| **Test Plan** | Overall testing strategy, scope, schedule |
| **Test Cases** | Detailed test steps and expected results |
| **Test Scripts** | Automated test code |
| **Traceability Matrix** | Maps requirements to test cases |
| **Defect Report** | Documented bugs with details |
| **Test Summary Report** | Results, metrics, recommendations |

---

[← Previous: Kubernetes](11-kubernetes.md) | [Next: STLC & V-Model →](13-stlc-v-model.md)
