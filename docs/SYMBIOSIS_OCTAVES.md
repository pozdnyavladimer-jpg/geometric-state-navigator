# SYMBIOSIS OCTAVES SPEC
## V-CORE Generation Control Protocol

---

## 0. PURPOSE

This document defines a control layer between:
- Human Intent
- Neuro State
- Generation Parameters (Image / Video)

Goal:
Transform generation from prompt-based control to state-driven orchestration.

---

## 1. CORE MODEL

Generation = f(Shadow, Structure, Semantics, Coherence, Constraints, Exploration)

Mapped as:

| Layer | Meaning |
|---|---|
| Shadow | Latent space noise |
| Structure | Geometry / layout |
| Semantics | Prompt alignment |
| Coherence | Stability / quality |
| Constraints | Negative filters |
| Exploration | Novelty / drift |

---

## 2. GITCUBE 6-FACE CONTROL

| Face | Param | Real Mapping |
|---|---|---|
| PRESSURE | Noise Density | seed / sigma |
| FLOW | Prompt Force | CFG scale |
| STRUCTURE | Spatial Control | ControlNet / Depth / Pose |
| BALANCE | Sampling Quality | steps / sampler |
| LAW | Constraints | negative prompt |
| FUTURE | Exploration | temperature / variation strength |

---

## 3. NORMALIZED PARAM RANGES

All params are normalized to [0,1].

PRESSURE ∈ [0,1]  
FLOW ∈ [0,1]  
STRUCTURE ∈ [0,1]  
BALANCE ∈ [0,1]  
LAW ∈ [0,1]  
FUTURE ∈ [0,1]

---

## 4. NEURO STATE MODEL

NeuroState:
- adrenaline ∈ [0,1]   → exploration drive
- dopamine ∈ [0,1]     → reward fixation
- cortisol ∈ [0,1]     → penalty / fear
- serotonin ∈ [0,1]    → stability / balance

---

## 5. NEURO → PARAM MAPPING

Core rules:

- FUTURE += adrenaline * 0.6
- PRESSURE += adrenaline * 0.4

- BALANCE += dopamine * 0.5
- FLOW += dopamine * 0.3

- LAW += cortisol * 0.7
- FUTURE -= cortisol * 0.5

- STRUCTURE += serotonin * 0.6
- BALANCE += serotonin * 0.4

Clamp all values to [0,1].

---

## 6. STATE MODES

### EXPLORATION MODE

Condition:
- adrenaline > 0.7

Effect:
- FUTURE high
- LAW low
- PRESSURE high

Result:
- chaotic generation
- style drift
- high diversity

---

### STABILITY MODE

Condition:
- serotonin > 0.7

Effect:
- STRUCTURE high
- BALANCE high
- FUTURE low

Result:
- clean composition
- minimal artifacts

---

### LOCK MODE (CRYSTAL)

Condition:
- dopamine > 0.7

Effect:
- BALANCE high
- FLOW high
- FUTURE low

Result:
- consistent identity
- style persistence

---

### STRICT MODE

Condition:
- cortisol > 0.7

Effect:
- LAW maximal
- FUTURE minimal

Result:
- rigid output
- low hallucination
- low drift

---

## 7. VIDEO EXTENSION (TEMPORAL OCTAVE)

Additional parameters:

- temporal_coherence ∈ [0,1]
- frame_drift ∈ [0,1]

Rules:

- if temporal_coherence < 0.7:
  - increase BALANCE
  - increase STRUCTURE

- if frame_drift > 0.3:
  - decrease FUTURE

Interpretation:

| Problem | Cause | Fix |
|---|---|---|
| Flicker | low coherence | increase BALANCE |
| Morphing | high FUTURE | reduce FUTURE |
| Jitter | low STRUCTURE | increase STRUCTURE |

---

## 8. GENERATION PIPELINE

Shadow → Structure → Semantics → Balance → Law → Output

Each stage reduces ambiguity and increases alignment.

---

## 9. IMPLEMENTATION HOOK

Minimal controller logic:

- read neuro state
- map neuro state to control params
- clamp params
- send params into generation system

Pseudo-flow:

1. read user intent
2. estimate neuro state
3. apply symbiosis mapping
4. update generation params
5. render image / video
6. evaluate coherence
7. feed result back into state

---

## 10. CORE IDEA

User does not control pixels directly.

User controls:
- phase-space navigation
- stability
- drift
- structure
- coherence

---

## 11. FINAL DEFINITION

GitCube is an interface for navigating latent space through:
- state
- constraints
- coherence
- exploration

---

## STATUS

CRYSTAL
