# STATE_MODEL: Six-Dimensional State Ontology

This project uses a six-dimensional state model to represent, simulate, and regulate system behavior as a distributed field.

Instead of optimizing a single scalar score, the system operates in a normalized vector space where each dimension captures a distinct aspect of system dynamics.

These dimensions are not features of the input.  
They are **control variables of the system state**.

---

## Executive Summary

The Geometry-Guided State Navigation Layer (GSL) represents behavior as a field distributed over multiple nodes (currently 19 in a 3D topology).

Each node maintains a normalized state vector:

[V] = [P, F, S, B, L, T]

Where:

- P = Pressure
- F = Flow
- S = Structure
- B = Balance
- L = Law
- T = Transition (Future)

The vector is normalized at each step:

||V||₁ = 1.0

This enforces geometric constraints and creates competition between dimensions.

---

## Why a Multi-Dimensional State Model

Traditional systems optimize:

input → score → choose

This collapses multiple behavioral factors into a single scalar.

In practice, this causes:

- instability loops
- shallow optimization
- loss of structural memory
- inability to separate tension from adaptability

GSL separates these dynamics into independent axes, allowing the system to regulate them explicitly.

---

## The Six State Dimensions

Each dimension represents a **semantic axis of system dynamics**.

Color mapping is used for readability and intuition, but computation is fully vector-based.

---

### 🔴 Red / Pressure (`red_mass`)

**Definition:** unresolved tension, conflict, or system overload.

- High: instability, conflict, accumulated unresolved state
- Low: clear, stable, low residual tension

Represents **what is not yet integrated**.

---

### 🟠 Orange / Flow (`orange_flow`)

**Definition:** adaptability, movement, and transition intensity.

- High: flexible, dynamic, able to change
- Low: rigid, inert, stuck

Represents **ability to move between states**.

---

### 🟡 Yellow / Structure (`yellow_struct`)

**Definition:** structural integrity, organization, and planning form.

- High: well-defined structure, clear organization
- Low: chaotic, unstructured, noisy

Represents **the shape of the system**.

---

### 🟢 Green / Balance (`green_balance`)

**Definition:** internal coherence and alignment between dimensions.

- High: consistent, integrated, harmonious
- Low: conflicting internal signals

Represents **how well the system fits together**.

---

### 🔵 Blue / Rule (`blue_law`)

**Definition:** constraint compliance and formal correctness.

- High: strict adherence to rules and boundaries
- Low: unconstrained, potentially unstable

Represents **respect for constraints**.

---

### 🟣 Violet / Future (`violet_future`)

**Definition:** readiness for transition and latent transformation potential.

- High: system is ready for a state shift
- Low: system is locked in current configuration

Represents **transition readiness**.

---

## Origin of the Model

The model did not begin as a predefined taxonomy.

It emerged during experimentation where:

- scalar scoring failed to stabilize system behavior
- combining variables (e.g., pressure + flow) caused instability
- the system required separation between:
  - tension
  - movement
  - structure
  - coherence
  - constraints
  - transition readiness

This resulted in a minimal stable representation of six dimensions.

---

## Evidence from System Behavior

The model is validated through simulation:

### 1. Stability vs Collapse

Reducing dimensions leads to:

- chaotic oscillation (too few axes)
- rigid collapse (over-constrained systems)

Six dimensions maintain a balance between:

- adaptability
- structure
- stability

---

### 2. Pressure Transformation

The system demonstrates consistent behavior:

pressure → flow + transition

When coherence is high, unresolved pressure is converted into:

- movement (Flow)
- transition potential (Future)

This is not symbolic — it emerges from the update dynamics.

---

### 3. Field-Level Regulation

The system operates on a distributed field:

- nodes influence each other
- local states propagate globally
- coherence emerges from interactions

This allows:

- non-linear stabilization
- distributed memory
- structural regulation instead of local scoring

---

## How to Read the State

System behavior is defined by **combinations**, not individual values.

Examples:

- high red + low green → unstable tension
- high yellow + low orange → rigid structure
- high green + moderate yellow + orange → stable adaptive system
- high violet → readiness for transition

---

## Role Inside GSL

In GSL:

1. Candidate actions are generated
2. Each candidate is encoded into the 6D state
3. The state is injected into the field
4. The system simulates propagation
5. Metrics are evaluated:
   - shadow (residual pressure)
   - coherence (alignment)
   - target_fit (goal proximity)
   - vitality (dynamic energy)
6. The system selects the candidate that produces the best global field state

---

## Important Clarification

- Colors are **semantic labels**, not computational primitives
- All operations are performed in normalized vector space
- The model is a **state control system**, not a feature representation

---

## One-Line Definition

A six-dimensional control state model that separates pressure, flow, structure, balance, constraint, and transition readiness to enable geometric regulation of system behavior.
