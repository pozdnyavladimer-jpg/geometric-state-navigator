# 🧠 Dual Brain Model (GSL / Graph School)

This document defines the dual-system architecture of the agent.

The system operates as a balance between:

- structure (stability)
- exploration (novelty)
- integration (selection)

---

# Core Idea

The agent is not a single decision-maker.

It is a **dual-process system with a central evaluator**:

- Left system → preserves structure
- Right system → generates novelty
- Center → selects and integrates

---

# System Components

| Component | Role | Function |
|----------|------|----------|
| Left Brain | Structure | maintain stability, enforce rules |
| Right Brain | Exploration | generate new possibilities |
| Center | Integration | evaluate and select actions |

---

# Left Brain (Structure System)

### Responsibilities

- enforce constraints
- reduce risk
- maintain graph integrity
- preserve known good structure

---

### Behavior

- prefers ALLOW states
- avoids risk
- resists change

---

### Failure Mode
Overdominance → stagnation
---

# Right Brain (Exploration System)

### Responsibilities

- propose new actions
- explore alternative structures
- introduce variation

---

### Behavior

- generates WARN candidates
- increases diversity
- seeks improvement

---

### Failure Mode
Overdominance → collapse
---

# Center (Evaluator / Integrator)

### Responsibilities

- compare proposals
- enforce survival constraints
- balance risk vs utility
- select next state

---

### Behavior

- filters BLOCK
- allows controlled WARN
- maintains ALLOW baseline

---

### Failure Mode
Bias toward safety → no evolution
---

# Decision Flow
Left proposal (safe) Right proposal (novel) ↓ Center ↓ select next state
---

# Selection Logic

1. Reject all BLOCK states
2. Prefer ALLOW when system is unstable
3. Accept WARN when system is stagnant
4. Balance stability and growth

---

### Simplified Rule
if unstable → choose safe if stagnant → choose novel else → choose balanced
---

# Shadow Mechanism

The right system represents **unintegrated potential (shadow)**.

It must not be suppressed completely.

---

### Rule
No exploration → stagnation Controlled exploration → evolution
---

# Exploration Pressure

The system tracks lack of change.

If no improvement occurs:
increase exploration_probability
---

# Stabilization Response

If instability increases:
increase constraint_strength
---

# Dynamic Balance

The system continuously shifts between:

| State | Strategy |
|------|----------|
| Stable | allow exploration |
| Unstable | enforce structure |
| Balanced | maintain mix |

---

# Interaction with Pattern Engine

The dual brain is the execution layer.

- Pattern Engine → generates candidate ideas
- Dual Brain → selects and applies them

---

# Interaction with Navigation Law

Navigation Law defines *what is correct*.

Dual Brain defines *how decisions are made*.

---

# Key Principle

The system does not aim to eliminate conflict.

It uses conflict between:

- stability
- novelty

to generate evolution.

---

# Final Formula
Evolution = Structure + Controlled Novelty + Integration
---

# Minimal Loop
observe → generate (left/right) → evaluate (center) → apply → repeat
---

# Identity

The agent is not:

- purely rational
- purely exploratory

---

### The agent is:
A dual-system adaptive navigator
---

# End of Document
