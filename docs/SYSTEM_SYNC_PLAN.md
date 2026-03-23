# SYSTEM SYNC PLAN

This document defines how the three repositories relate to each other and what must stay synchronized between them.

---

## Repositories and Roles

### 1. `gitcube-lab`
Role: experimental sandbox

Purpose:
- test new ideas
- run unstable simulations
- explore mutations
- try new filters, routing rules, or pattern imports

This repository is allowed to diverge.
It is the place where ideas are born.

---

### 2. `geometric-state-navigator`
Role: canonical state engine

Purpose:
- define the state model
- define field metrics
- define resonance / bindu / control logic
- provide the canonical interpretation of system state

This repository is the source of truth for:
- state dimensions
- metric definitions
- threshold philosophy
- field-level behavior

---

### 3. `gitcube-os`
Role: stabilized execution layer

Purpose:
- run the system as an operating layer
- execute loops
- store memory
- promote validated behavior into runtime form

This repository should not invent new theory.
It should implement validated logic from the navigator layer.

---

## Core Principle

Lab invents.  
Navigator formalizes.  
OS executes.

---

## What must stay synchronized

The following parts must remain semantically aligned across repositories.

### 1. State axes

Canonical six-dimensional state:

- pressure
- flow
- structure
- balance
- law
- future

If color aliases are used in research notebooks, they must map consistently:

- red_mass → pressure
- orange_flow → flow
- yellow_struct → structure
- green_balance → balance
- blue_law → law
- violet_future → future

---

### 2. Core metrics

These metrics must mean the same thing everywhere:

- `shadow`
- `coherence`
- `target_fit`
- `vitality`

Even if implementation differs slightly in early experiments, the semantic meaning must stay aligned.

---

### 3. Threshold logic

The following thresholds must be documented and reviewed together:

- commit / soft commit / reject
- bindu open conditions
- warning vs block boundaries
- resonance / coherence gating

Thresholds may evolve, but changes should be intentional and visible.

---

### 4. Promotion path

New logic should move through the system in this order:

1. `gitcube-lab`
2. `geometric-state-navigator`
3. `gitcube-os`

This means:
- experiments happen in Lab
- validated logic is formalized in Navigator
- stable runtime behavior is implemented in OS

---

## What should NOT be synchronized directly

The following should not be copied blindly across all repositories:

- temporary notebooks
- unstable thresholds
- one-off experimental hacks
- debugging code
- research-only metaphors without executable meaning

Only validated logic should move upward.

---

## Source of Truth Map

### `gitcube-lab`
Owns:
- experiments
- adversarial tests
- mutation ideas
- speculative prototypes

### `geometric-state-navigator`
Owns:
- canonical state semantics
- canonical metric definitions
- field logic
- bindu / resonance interpretation
- theoretical system coherence

### `gitcube-os`
Owns:
- runtime execution
- memory loop
- scheduling
- promotion of stable behavior
- operational system flow

---

## Synchronization Workflow

When a new idea appears:

### Step 1 — Experiment
Try it in `gitcube-lab`.

Questions:
- does it work at all?
- does it improve system behavior?
- does it fail under pressure?

### Step 2 — Formalize
If useful, rewrite it in `geometric-state-navigator`.

Questions:
- what does it mean in state language?
- which metric does it affect?
- what threshold or law changes?

### Step 3 — Operationalize
If stable, implement it in `gitcube-os`.

Questions:
- how is it executed?
- when is it committed?
- how is it stored in memory?

---

## Example

A new resonance filter appears in Lab.

- In `gitcube-lab`: test many versions
- In `geometric-state-navigator`: define canonical `coherence_frequency`
- In `gitcube-os`: use it in runtime gate / memory acceptance

This is the correct direction.

---

## Minimal Governance Rule

If two repositories produce different meanings for the same metric,
the Navigator definition wins.

---

## One-line Summary

`gitcube-lab` explores possible logic.  
`geometric-state-navigator` defines correct logic.  
`gitcube-os` runs accepted logic.
