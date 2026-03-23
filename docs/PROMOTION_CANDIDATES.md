# PROMOTION CANDIDATES

This document tracks ideas that may move through the GitCube promotion path.

Canonical path:

gitcube-lab
→ geometric-state-navigator
→ gitcube-os

Not every candidate will be promoted.

Some will remain experimental.
Some will be rejected.
Some may be deprecated later.

---

## 1. Purpose

This file exists to answer:

- what ideas are under evaluation
- where they came from
- what they mean in canonical language
- whether they are ready for runtime
- what still blocks promotion

This is the working bridge between Lab and OS.

---

## 2. Status Vocabulary

Use only these statuses:

- experimental
- interpreted
- canonical
- runtime-ready
- promoted
- rejected
- deprecated

---

## 3. Candidate Template

Each candidate should specify:

- name
- source repo
- source file
- status
- canonical interpretation
- affected axes
- affected metrics
- affected thresholds
- runtime value
- known risks
- next action

---

## 4. Active Candidates

### Candidate 1 — coherence_frequency

- source repo: gitcube-lab
- source file: resonance / octave / bindu-related experiments
- status: interpreted
- canonical interpretation:
  derived signal related to coherence quality across the field
- affected axes:
  - balance
  - structure
  - flow
- affected metrics:
  - coherence
- affected thresholds:
  none yet
- runtime value:
  may later refine Bindu selectivity
- known risks:
  can become too abstract or too expensive for runtime
- next action:
  keep in Navigator until a simple operational form exists

---

### Candidate 2 — sieve_score

- source repo: gitcube-lab
- source file: cicada / sieve-style experiments
- status: experimental
- canonical interpretation:
  possible filtering signal for path survivability
- affected axes:
  unclear
- affected metrics:
  possibly coherence or target_fit
- affected thresholds:
  none yet
- runtime value:
  unknown
- known risks:
  may duplicate existing gate logic without adding clarity
- next action:
  remain in Lab until mapped clearly into canonical metrics

---

### Candidate 3 — bindu_opened

- source repo: geometric-state-navigator
- source file: bindu / 3d field simulations
- status: interpreted
- canonical interpretation:
  regime-level state in which the field remains stably aligned,
  not just a one-step gate decision
- affected axes:
  - balance
  - structure
  - future
- affected metrics:
  - coherence
  - shadow
  - vitality
  - target_fit
- affected thresholds:
  may later define a stronger regime threshold
- runtime value:
  useful for reporting and long-horizon episode logic
- known risks:
  can be confused with simple COMMIT gate
- next action:
  keep as Navigator concept; only promote if OS needs regime tracking

---

### Candidate 4 — soft memory persistence

- source repo: gitcube-os
- source file: runtime/memory.py
- status: promoted
- canonical interpretation:
  memory may preserve transitional but acceptable states under flagged status
- affected axes:
  none directly
- affected metrics:
  none directly
- affected thresholds:
  depends on SOFT_COMMIT logic
- runtime value:
  already useful
- known risks:
  memory may become noisy if soft states dominate
- next action:
  monitor and possibly compress or weight soft entries differently

---

### Candidate 5 — environment-weighted selection

- source repo: gitcube-os
- source file:
  - environments/
  - runtime/environment_score.py
  - examples/environment_run.py
- status: promoted
- canonical interpretation:
  the same state may be valued differently depending on environment pressure
- affected axes:
  indirect effect across all axes
- affected metrics:
  - shadow
  - coherence
  - target_fit
  - vitality
- affected thresholds:
  none directly
- runtime value:
  already useful for differentiated runtime behavior
- known risks:
  environment profiles may drift without canon
- next action:
  later define ENVIRONMENT_CANON if complexity grows

---

## 5. Rejected or Frozen Candidates

### Candidate — raw metaphor injection

- source repo: gitcube-lab
- status: rejected
- canonical interpretation:
  unclear
- reason:
  expressive but not operationally stable
- lesson:
  metaphor is useful for invention, but not enough for promotion

---

## 6. Promotion Heuristic

A candidate is strong when:

- it solves a real system problem
- it maps clearly to canonical state language
- it improves runtime decisions
- it fails safely
- it remains simpler than the problem it solves

A candidate is weak when:

- it sounds powerful but changes nothing operationally
- it duplicates existing metrics
- it cannot be explained in canonical language
- it makes runtime harder to trust

---

## 7. Minimal Rule

If a candidate cannot be written here clearly,
it is not ready for promotion.

---

## 8. One-line Summary

Promotion candidates are not ideas we like.
They are ideas we can explain, test, and eventually trust.
