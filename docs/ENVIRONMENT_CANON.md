# ENVIRONMENT CANON

This document defines the canonical meaning of environments in the GitCube system.

An environment is not decoration.

It is a condition field that changes how the system values candidate transitions.

---

## 1. Core Definition

An environment defines which properties are more important for survival under a given condition.

The same candidate state may be acceptable in one environment
and less acceptable in another.

Therefore:

environment does not redefine the state language

it reweights the value of state outcomes

---

## 2. Role in the System

Canonical flow:

candidate state
→ metrics
→ environment weighting
→ bindu gate
→ memory / runtime update

This means environment acts before final runtime commitment.

It shapes preference.
Bindu still protects survival.

---

## 3. What Environment Can Affect

Environment may affect the importance of:

- shadow
- coherence
- target_fit
- vitality

Environment should not directly rewrite canonical state meaning.

It should only change the relative importance of already canonical metrics.

---

## 4. Canonical Philosophy

State language remains stable.

Environment changes pressure.

This means:

- pressure is canonical
- context is environmental

Environment asks:

- under this world condition, what matters more

It does not ask:

- what do these metrics mean now

Meaning remains fixed.
Value shifts.

---

## 5. Minimal Canonical Environments

### balanced

Meaning:
- neutral learning world
- no extreme pressure
- all metrics have near-equal importance

Use when:
- testing baseline system behavior
- comparing agents without strong world bias

Typical effect:
- results stay close to base scoring

---

### harsh

Meaning:
- unstable or dangerous world
- system must protect integrity first

Use when:
- collapse risk is high
- noisy transitions are dangerous
- stability matters more than novelty

Typical effect:
- shadow penalty increases
- coherence importance increases
- vitality may matter less than survival

Expected tendency:
- stabilizer-like behavior becomes more valuable

---

### exploratory

Meaning:
- system is allowed to search
- adaptability and movement matter more

Use when:
- novelty is acceptable
- system is not near collapse
- future potential and dynamic motion are useful

Typical effect:
- vitality becomes more important
- strict pressure suppression matters slightly less

Expected tendency:
- explorer-like behavior becomes more viable

---

## 6. Canonical Rule of Environments

Environment may change preference.

Environment may not change law.

This means:

- environments can shift score
- environments cannot override Bindu canon
- environments cannot redefine COMMIT / REJECT semantics

Bindu remains the final survival gate.

---

## 7. Environment and Runtime

In OS, environment should be implemented as simple weighting logic.

This is preferred:

- small number of named profiles
- explicit metric weights
- deterministic behavior

This is discouraged:

- hidden environment mutation
- unclear world state
- unstable implicit weighting
- environment logic that rewrites thresholds without documentation

---

## 8. Environment and Navigator

Navigator should define:

- the meaning of each environment
- why metric weights differ
- which behaviors each environment encourages
- how environment interacts with canonical metrics

Navigator should not contain raw runtime weighting code.
It should contain canonical interpretation.

---

## 9. Environment and Lab

Lab may invent new environment candidates.

Examples:
- resonance environment
- adversarial environment
- stagnation environment
- compression-heavy environment

But these remain experimental until they can answer:

- what do they optimize for
- which metrics do they reweight
- why is this different from existing environments
- can this be simplified into OS logic

---

## 10. Promotion Rule for Environments

A new environment may be promoted only if:

1. its purpose is clear
2. its weighting effect is explainable
3. it does not duplicate another environment
4. it produces useful runtime variation
5. it remains simple enough to trust

If not, it remains experimental.

---

## 11. Minimal Canonical Mapping

Balanced:
- neutral weighting

Harsh:
- more weight on shadow and coherence

Exploratory:
- more weight on vitality and adaptive movement

This is the current minimal operational canon.

---

## 12. Failure Mode

Environment becomes dangerous when it starts replacing canonical logic.

Examples of bad environment design:

- changing metric meaning
- silently changing thresholds
- hiding unstable heuristics inside score logic
- making runtime interpretation impossible

Environment must shape preference, not destroy interpretability.

---

## 13. One-line Law

Environment changes what is preferred.
Bindu decides what survives.

---

## 14. One-line Summary

Environment is the world-pressure layer of the GitCube system:
it changes how candidate states are valued without changing what the state language means.
