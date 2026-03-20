# BENCHMARK: GSL vs Baseline Selection

This document demonstrates how the Geometry-Guided State Navigation Layer (GSL) differs from standard selection strategies.

The goal is to show that GSL selects actions based on **global field stabilization**, not local preference.

---

## What is being tested

We compare two selection strategies:

### Baseline
Selects the best candidate using a local scoring function.

### GSL
Selects the candidate that produces the best **global field state** after simulation.

---

## Evaluation Metrics

Each candidate is evaluated using:

- **Shadow** → unresolved pressure (lower is better)
- **Coherence** → internal alignment (higher is better)
- **Target Fit** → alignment with desired state
- **Vitality** → ability to continue evolving

---

## Key Result

In multiple scenarios, GSL selects a **different action** than baseline.

This indicates:

> GSL is not following local preference.  
> It is optimizing global system behavior.

---

## Example Case

### Scenario

"We have an unstable system with conflicting signals. What should we do?"

---

### Baseline Decision

Selected: **force_control**

Reason (implicit):
- high structure
- strong constraint enforcement

Resulting state:

- shadow = 0.232
- coherence = 0.901
- target_fit = 0.684
- vitality = 0.575

---

### GSL Decision

Selected: **integrative_adaptive**

Reason:
- reduces pressure more effectively
- increases coherence
- maintains adaptability

Resulting state:

- shadow = 0.223
- coherence = 0.938
- target_fit = 0.706
- vitality = 0.594

---

## Interpretation

Baseline prioritizes:

→ immediate control  
→ constraint enforcement  

GSL prioritizes:

→ pressure reduction  
→ system balance  
→ long-term stability  

This results in:

- lower residual tension
- higher alignment
- more adaptive behavior

---

## Summary Across Cases
cases_total = 5 selection_differences = 4/5 avg_coherence_gain = +0.030
### Meaning

- In **80% of cases**, GSL selects a different action
- GSL consistently improves **coherence**
- Small trade-offs in vitality or target_fit may occur
- Overall system stability improves

---

## Important Observation

In some cases:

Baseline and GSL select the same action.

This means:

> The local scoring already aligned with global field stability.

GSL does not override correct decisions.  
It only intervenes when local optimization leads to suboptimal global states.

---

## Failure Modes Addressed

### 1. Over-Control

Baseline selects rigid control strategies  
→ reduces flexibility  
→ increases long-term instability

GSL selects adaptive strategies  
→ preserves balance and movement

---

### 2. Exploration Bias

Baseline may over-prefer novelty or probability  
→ unstable transitions

GSL ensures:
→ exploration does not break coherence

---

### 3. Loop Behavior

Baseline may reinforce repeated patterns

GSL detects:
→ lack of field improvement  
→ selects alternative trajectory

---

## What This Proves

GSL introduces a new selection principle:

→ not "best answer"  
→ but "best resulting state"

This is a shift from:

**output optimization → system regulation**

---

## One-Line Conclusion

GSL improves decision-making by selecting actions that stabilize the system globally, even when those actions are not locally optimal.
