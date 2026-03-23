# BINDU CANON

This document defines the canonical meaning of Bindu in the GitCube system.

Bindu is not just a threshold.

It is the final decision point that determines whether a state transition is allowed to become part of the living system.

---

## 1. What Bindu Is

Bindu is the convergence point of a transition.

It answers:

- is the candidate state stable enough
- is the system coherent enough
- can this transition survive without damaging memory or runtime behavior

Bindu is therefore the acceptance gate between:
- candidate state
- committed state

---

## 2. Role of Bindu in the System

Bindu sits between evaluation and persistence.

Canonical flow:

candidate state
→ evaluation
→ bindu decision
→ commit or reject
→ memory update

This means Bindu is the last filter before:
- state update
- memory write
- runtime continuation

---

## 3. What Bindu Checks

At minimum, Bindu checks:

- shadow
- coherence

Optional extended checks may include:

- target_fit
- vitality
- resonance-derived signals

But the canonical minimum remains:

- low enough shadow
- high enough coherence

---

## 4. Canonical Bindu Philosophy

Bindu does not ask:
- is this state interesting
- is this state high-scoring
- is this state novel

Bindu asks:
- does this transition preserve system integrity

A state may be useful but still fail Bindu.
A state may be exciting but still fail Bindu.
A state must be survivable to pass.

---

## 5. Canonical Decision Set

Bindu may return one of the following decisions.

### COMMIT

Meaning:
- state is stable
- transition is allowed
- memory may be updated
- runtime may advance

### SOFT_COMMIT

Meaning:
- state is not ideal
- but transition is acceptable under controlled conditions
- memory write may be optional or flagged
- runtime may continue with caution

### REJECT

Meaning:
- state is too unstable
- transition must not be applied
- memory must not store it
- system should remain in previous valid state

### REROUTE

Meaning:
- current candidate should not be committed
- but search may continue through another agent, coalition, or path

---

## 6. Canonical Minimal Thresholds

These are the current baseline thresholds for minimal operational Bindu logic.

### Minimal COMMIT

Suggested baseline:

- coherence >= 0.85
- shadow <= 0.10

Meaning:
- state is coherent enough
- residual instability is low enough
- transition is safe to preserve

---

### Minimal SOFT_COMMIT

Suggested baseline:

- coherence >= 0.80
- shadow <= 0.15

Meaning:
- state is partially stable
- transition may be useful
- persistence is conditional

---

### Minimal REJECT

Suggested baseline:

- coherence < 0.80
OR
- shadow > 0.15

Meaning:
- state is too unstable to enter memory or runtime

---

## 7. Optional Extended Bindu Checks

These checks are not mandatory for the minimal OS layer,
but may be used in Navigator or advanced runtime designs.

### target_fit

Use when:
- the system has a defined attractor
- not every stable state is meaningful

Typical interpretation:
- a transition may be stable but still irrelevant

---

### vitality

Use when:
- the system should avoid dead stable states
- mere stability is not enough

Typical interpretation:
- stable but inert states may be allowed
- but not always preferred

---

### resonance or coherence_frequency

Use when:
- the system uses higher-order alignment logic
- field-level phase consistency matters

Typical interpretation:
- not all coherent states are equally resonant
- Bindu may become more selective in advanced layers

---

## 8. Bindu and Memory

Canonical rule:

Memory should only store what has passed Bindu.

This means:

- COMMIT → write memory
- SOFT_COMMIT → optional or flagged memory write
- REJECT → no memory write
- REROUTE → no memory write unless a new path passes

This protects memory from becoming a storage dump of unstable transitions.

---

## 9. Bindu and Runtime

Canonical rule:

Runtime must never overwrite a valid state with a rejected state.

This means:
- rejected transitions are observed
- but not applied

If a candidate fails Bindu:
- either reroute
- or keep the previous valid state

This is the minimum condition for runtime integrity.

---

## 10. Bindu and Lab vs OS

### In Lab

Bindu may be:
- weak
- exploratory
- partially disabled
- intentionally violated for experimentation

This is acceptable.

### In Navigator

Bindu should be:
- interpreted clearly
- linked to canonical metrics
- documented as system law

### In OS

Bindu should be:
- simple
- stable
- enforceable
- executable

The OS layer should use a minimal robust form of Bindu,
not an overcomplicated research version.

---

## 11. Bindu Open

In advanced field simulations, Bindu may also represent a regime,
not just a one-step gate.

This means Bindu can be interpreted in two ways:

### Bindu as gate
A single transition filter.

### Bindu as regime
A sustained region of:
- low shadow
- high coherence
- stable internal alignment

The OS layer usually uses Bindu as gate.
The Navigator layer may use Bindu as both gate and regime.

---

## 12. Promotion Rule

If a new Bindu-related signal is proposed in Lab, it must answer:

1. Does it replace shadow, coherence, or neither?
2. Is it a primary metric or a derived signal?
3. Is it needed in OS or only in Navigator?
4. Does it improve survival filtering without making runtime fragile?

If these answers are not clear,
the signal remains experimental.

---

## 13. Minimal Canon Law

A transition may only become memory if it survives Bindu.

This is the minimal law.

---

## 14. One-line Summary

Bindu is the canonical survival gate of the GitCube system:
it decides whether a candidate transition deserves to become real.
