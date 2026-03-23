# STATE CANON

This document defines the canonical state language for the GitCube system.

It is the source of truth for:

- state axes
- naming conventions
- metric meanings
- threshold philosophy
- translation rules between repositories

If any repository diverges from this document, the Navigator definition wins.

---

## 1. Canonical State Model

The system uses a six-dimensional control state.

Canonical axis names:

- `pressure`
- `flow`
- `structure`
- `balance`
- `law`
- `future`

These are not input features.
They are control dimensions of system state.

---

## 2. Color Mapping

In research notebooks and visual simulations, the same axes may appear as color-based aliases.

Canonical mapping:

- `red_mass` → `pressure`
- `orange_flow` → `flow`
- `yellow_struct` → `structure`
- `green_balance` → `balance`
- `blue_law` → `law`
- `violet_future` → `future`

The semantic meaning must stay the same across both naming styles.

---

## 3. Canonical Meaning of Each Axis

### `pressure`
Unresolved tension, instability, accumulated conflict, overload.

Interpretation:
- high pressure = unstable / unresolved system
- low pressure = cleaner, more integrated state

---

### `flow`
Movement, adaptability, transition energy, ability to change.

Interpretation:
- high flow = mobile, exploratory, dynamic
- low flow = rigid, inert, stuck

---

### `structure`
Form, organization, internal planning shape.

Interpretation:
- high structure = ordered, shaped, internally organized
- low structure = noisy, weakly formed

---

### `balance`
Internal coherence and compatibility between dimensions.

Interpretation:
- high balance = integrated and aligned
- low balance = conflicting internal tendencies

---

### `law`
Constraint compliance, rule stability, formal containment.

Interpretation:
- high law = bounded, disciplined, constrained
- low law = weakly governed, unstable boundary behavior

---

### `future`
Transition readiness, latent next-state potential, adaptive direction.

Interpretation:
- high future = transition is possible
- low future = system is locked or inert

---

## 4. Canonical Metrics

These are the primary metrics used across the system.

### `shadow`
Canonical meaning:
residual unresolved pressure

Default interpretation:
- derived primarily from `pressure`
- higher shadow = more unresolved load

Typical form:
- `shadow = pressure`

---

### `coherence`
Canonical meaning:
alignment between major stabilizing dimensions

Default interpretation:
- balance should align with structure
- balance should align with flow

Typical form:
- coherence decreases when these dimensions diverge

Example philosophy:
- high coherence = system acts as one field
- low coherence = internal mismatch

---

### `target_fit`
Canonical meaning:
how close the current state is to the desired attractor

Default interpretation:
- often derived from balance + structure
- in richer field models, may compare full vector to target vector

Example philosophy:
- high target_fit = state approaches intended regime
- low target_fit = state drifts away from desired form

---

### `vitality`
Canonical meaning:
dynamic liveliness of the system

Default interpretation:
- usually tied to flow + future
- may include structure in richer field models

Example philosophy:
- high vitality = adaptive motion still exists
- low vitality = dead or frozen system

---

## 5. Canonical Threshold Philosophy

Thresholds may evolve, but their meaning must stay stable.

### Commit logic philosophy

A state is a good commit candidate when:
- pressure is sufficiently low
- coherence is sufficiently high
- the system is stable enough to preserve

This can be implemented differently in different layers,
but the philosophy is fixed.

---

### Warning logic philosophy

A state is in warning mode when:
- pressure is not catastrophic
- coherence is partial
- system can continue, but should be watched

---

### Block / reject logic philosophy

A state should be blocked or rejected when:
- pressure is too high
- coherence collapses
- the transition would destabilize memory or runtime behavior

---

## 6. Current Canonical Runtime Thresholds

These are the current minimal reference thresholds for OS-like runtime logic.

### Minimal Bindu Commit
Suggested baseline:

- `coherence >= 0.85`
- `shadow <= 0.12`

This is not the final universal law.
It is the current baseline for minimal operational commit.

---

### Soft Acceptance Zone
Suggested interpretation:

- good coherence but slightly elevated shadow
- or good pressure but incomplete coherence

This zone should allow:
- soft commit
- reroute
- conditional memory write

depending on runtime design

---

## 7. Repository Translation Rules

### In `gitcube-lab`
The system may use:
- unstable variable names
- temporary metrics
- speculative thresholds

This is acceptable during experimentation.

But if a concept is promoted,
it must be translated into canonical state language.

---

### In `geometric-state-navigator`
All promoted logic should be rewritten in canonical form.

This repository owns:
- canonical axis semantics
- canonical metric meanings
- canonical threshold philosophy

---

### In `gitcube-os`
Runtime code should use canonical names whenever possible:

Preferred:
- `pressure`
- `flow`
- `structure`
- `balance`
- `law`
- `future`

Research aliases may be referenced in comments,
but operational code should stay clean.

---

## 8. Promotion Rule

If a notebook introduces a useful new quantity, it must answer:

1. Which canonical axis does it affect?
2. Which canonical metric does it modify?
3. Is it a new metric, or a derived signal?
4. Is it experimental, navigator-level, or OS-ready?

Only after this translation can it move upward.

---

## 9. Example Translation

Example:

Notebook variable:
- `coherence_frequency`

Canonical interpretation:
- derived signal related to `coherence`
- may later become a secondary metric in navigator logic
- should not automatically replace canonical coherence

This is how new ideas should enter the system:
not as raw notebook names, but as interpreted additions.

---

## 10. Minimal Canon Law

The system must always be able to answer:

- what state are we in
- why is this state stable or unstable
- what transition is allowed next
- whether this state deserves to persist

If a new variable does not help answer one of these,
it should remain experimental.

---

## 11. One-line Summary

The GitCube system operates in a canonical six-dimensional state language:
pressure, flow, structure, balance, law, and future.
All higher logic must eventually reduce to this language.
