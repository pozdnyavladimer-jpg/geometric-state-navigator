# THRESHOLD CANON

This document defines the canonical thresholds for decision-making in the GitCube system.

It controls:

- commit vs reject
- memory write conditions
- bindu activation
- routing decisions

This is the operational layer of the system.

---

## 1. Core Idea

The system does not select actions by score alone.

It selects actions based on:

- stability (low shadow)
- alignment (high coherence)
- survivability

---

## 2. Canonical Metrics Reference

Used in all thresholds:

- shadow → residual instability
- coherence → internal alignment
- target_fit → goal alignment
- vitality → dynamic energy

---

## 3. Decision Zones

### 🟥 REJECT (unstable state)

Conditions:

- shadow > 0.15  
OR
- coherence < 0.80  

Meaning:

- state is unstable
- cannot be stored
- should not update system

Action:

- reject
- reroute
- do not write memory

---

### 🟨 SOFT ZONE (transitional state)

Conditions:

- 0.10 < shadow ≤ 0.15  
AND
- 0.80 ≤ coherence < 0.85  

Meaning:

- partially stable
- not ideal, but usable

Action:

- soft commit OR reroute
- conditional memory write

---

### 🟩 COMMIT (stable state)

Conditions:

- shadow ≤ 0.10  
AND
- coherence ≥ 0.85  

Meaning:

- stable system state
- safe to persist

Action:

- commit
- update state
- write memory

---

## 4. Bindu Gate

Bindu acts as a final filter before memory or state update.

### Minimal Bindu Commit

Conditions:

- coherence ≥ 0.85  
- shadow ≤ 0.10  

Decision:

- COMMIT

---

### Bindu Reject

Conditions:

- shadow too high  
- coherence too low  

Decision:

- REJECT

---

## 5. Optional Extended Logic

Bindu may include additional checks:

- vitality > 0.25 → avoid dead states  
- target_fit > 0.4 → avoid meaningless states  

These are optional but recommended.

---

## 6. Routing Logic

If state is rejected:

- do NOT update state
- trigger reroute
- allow alternative agent selection

---

## 7. Memory Rules

Memory should only store:

- committed states
- or soft states (optional, flagged)

Never store:

- rejected states
- unstable transitions

---

## 8. Canonical Mapping to Code

Example:

```python
if coherence >= 0.85 and shadow <= 0.10:
    decision = "COMMIT"
elif coherence >= 0.80:
    decision = "SOFT"
else:
    decision = "REJECT"
```
