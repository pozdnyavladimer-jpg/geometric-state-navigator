# REPO MAP

This document defines how the GitCube system is split across repositories.

The system is intentionally divided into 3 layers:

gitcube-lab
→ geometric-state-navigator
→ gitcube-os

Each layer has a strict role.

---

## 1. High-Level Structure

### gitcube-lab

Role:
- exploration
- invention
- experiments

Contains:
- notebooks
- simulations
- raw ideas
- unstable logic
- new metrics
- new environments

Allowed:
- chaos
- redundancy
- abstraction
- intuition

Not allowed:
- runtime-critical logic
- canonical definitions

---

### geometric-state-navigator

Role:
- interpretation
- canonical meaning
- system laws

Contains:
- STATE_CANON.md
- THRESHOLD_CANON.md
- BINDU_CANON.md
- ENVIRONMENT_CANON.md
- PROMOTION_RULES.md
- PROMOTION_CANDIDATES.md

Defines:
- what metrics mean
- what thresholds mean
- what decisions mean
- what environments mean

Allowed:
- explanation
- mapping
- abstraction → clarity

Not allowed:
- raw experiments
- runtime code
- unstable logic

---

### gitcube-os

Role:
- execution
- runtime system
- survival filtering

Contains:
- core/
- runtime/
- environments/
- memory/

Implements:
- state transitions
- agent loop
- Bindu decision (runtime)
- memory rules
- environment scoring

Allowed:
- simple deterministic logic
- stable implementation
- minimal abstractions

Not allowed:
- unclear meaning
- experimental logic
- unexplained thresholds

---

## 2. Promotion Flow

All ideas must follow this path:

1. Lab → generate candidate
2. Navigator → interpret candidate
3. OS → implement candidate

This is mandatory.

---

## 3. Promotion Rules

A candidate may move forward only if:

From Lab → Navigator:
- it can be explained in canonical language
- it has clear purpose
- it maps to state / metrics / thresholds

From Navigator → OS:
- it has a minimal implementation
- it improves runtime behavior
- it fails safely
- it is simpler than the problem it solves

---

## 4. Anti-Patterns

### ❌ Direct Lab → OS injection

Bad:
- copying notebook logic into runtime
- skipping canonical interpretation

Why:
- leads to unstable system behavior

---

### ❌ Navigator becoming a notebook

Bad:
- adding experiments into docs
- mixing meaning with raw code

Why:
- destroys clarity

---

### ❌ OS defining meaning

Bad:
- thresholds only exist in code
- logic not documented in Navigator

Why:
- system becomes unexplainable

---

## 5. Responsibility Split

Lab:
- invents

Navigator:
- explains

OS:
- enforces

---

## 6. Minimal Law

Nothing enters OS
unless it is first understood in Navigator.

---

## 7. One-line Summary

Lab explores.
Navigator explains.
OS keeps what survives.
