# ORGANISM PROTOCOL

This document defines how the GitCube system operates as a single organism
across three repositories.

It removes the separation between repositories at the behavioral level.

---

## 1. Core Principle

The system is not a collection of repositories.

It is a single lifecycle:

Lab → Navigator → OS

Each repository is a phase of the same process.

---

## 2. Roles

### Lab (gitcube-lab)

Function:
- exploration
- mutation
- generation of candidates

Properties:
- unstable
- experimental
- unconstrained

Output:
- candidate ideas
- candidate parameters
- candidate behaviors

---

### Navigator (geometric-state-navigator)

Function:
- interpretation
- canonical definition
- validation of meaning

Properties:
- stable semantics
- explicit rules
- no raw experimentation

Output:
- canonical mapping
- thresholds
- definitions
- promotion eligibility

---

### OS (gitcube-os)

Function:
- execution
- decision enforcement
- memory and reroute

Properties:
- deterministic behavior
- minimal abstraction
- runtime stability

Output:
- accepted transitions
- rejected transitions
- memory updates

---

## 3. Lifecycle

Every idea follows the same path:

1. Generated in Lab
2. Interpreted in Navigator
3. Executed in OS

If an idea skips a stage, it is invalid.

---

## 4. Repo Awareness (Agent Requirement)

Any agent operating in the system must be aware of:

- which repository it is interacting with
- the role of that repository
- the stage of the idea it is processing

Minimal required state:

- repo_type ∈ {lab, navigator, os}
- idea_status ∈ {experimental, interpreted, canonical, runtime}

---

## 5. Promotion State

Each idea must have a clear state:

- experimental → exists only in Lab
- interpreted → mapped in Navigator
- canonical → validated meaning
- runtime → implemented in OS

No idea should exist in multiple ambiguous states.

---

## 6. Canon Alignment

Before an idea moves to OS, it must align with:

- STATE_CANON
- THRESHOLD_CANON
- BINDU_CANON
- ENVIRONMENT_CANON

If alignment is unclear → reject or return to Navigator.

---

## 7. Runtime Integrity

OS must not:

- interpret meaning
- invent new rules
- introduce undefined parameters

OS only executes what is already defined.

---

## 8. Feedback Loop

OS produces signals:

- accepted transitions
- rejected transitions
- dead states
- instability patterns

These signals must flow back:

OS → Navigator → Lab

This enables system learning.

---

## 9. Failure Modes

### Lab → OS direct injection

Invalid:
- skips interpretation
- leads to unstable runtime

---

### Navigator drift

Invalid:
- meaning becomes unclear
- multiple interpretations emerge

---

### OS mutation

Invalid:
- runtime starts redefining rules
- system becomes untraceable

---

## 10. Minimal Law

No behavior enters OS
unless it is first understood in Navigator.

---

## 11. One-line Summary

The system is a closed loop:

Lab explores  
Navigator explains  
OS executes  
and feedback returns to Lab
