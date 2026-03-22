# Geometry-Guided State Navigation Layer (GSL)
## ▶️ Quick Start

Start here:

- Multi-agent demo → notebooks/gsl_multi_agent_bindu_demo.ipynb
- 3D field simulation → research/simulation_3d_bindu.ipynb
- Text encoder → research/gsl_text_encoder_demo.ipynb
## Risk-Level Behavior Demo

The system adapts behavior based on structural risk:

### LOW RISK
- risk: 0.233
- decision: planner+explorer
- interpretation: safe to explore

### MEDIUM RISK
- risk: 0.51
- decision: planner+critic
- interpretation: controlled execution

### HIGH RISK
- risk: 1.0
- decision: planner+stabilizer
- interpretation: stabilization required

The system does not react to tokens —  
it reacts to structural instability.
GSL is a control layer for nonlinear state regulation on top of existing AI systems.

Instead of selecting outputs by probability or score, GSL evaluates how candidate states reshape a distributed field and selects the one that improves global system stability.

---
## Canonical Integrated Demo

GitCube computes structural risk from a dependency graph.  
GSL converts that risk into a state vector and selects a control coalition.

This demonstrates a shift from code-level reasoning to system-level decision making.

Example:

- risk = 0.51  
- verdict = WARN  
- decision = planner+critic  
- status = SOFT_COMMIT  

The system reacts not to tokens, but to structural instability.
## Text / Code Encoder Demo

The project includes a demo that maps both natural language and code into the same 6D behavioral state space.

This allows the system to read:

- unstable text  
- balanced instructions  
- structured code  
- pathological code patterns  

→ see [gsl_text_encoder_demo.ipynb](./research/gsl_text_encoder_demo.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pozdnyavladimer-jpg/geometric-state-navigator/blob/main/research/gsl_text_encoder_demo.ipynb)
## 🧭 Recommended Flow

1. Run multi-agent demo  
2. Observe state evolution  
3. Run 3D bindu simulation  
4. Try text encoder  

This demonstrates:
- state control
- field simulation
- structure → behavior mapping
## 🚀 Core Idea

Standard AI:
input → score → choose

GSL:
input → candidates → encode → simulate field → evaluate → select → update memory

This shifts decision-making from local optimization to global state regulation.

---

## 🧠 What it does

GSL improves:

- stability under conflicting signals
- loop avoidance
- structural memory
- long-horizon behavior
- adaptive decision-making

---
---

## 🧪 Research & Graph Architecture Lab

GSL is the control layer.

The underlying graph-based architecture reasoning environment is developed in:

👉 https://github.com/pozdnyavladimer-jpg/gitcube-lab

GitCube Lab is a research platform that focuses on:

- dependency graph analysis  
- architecture stability and risk detection  
- topology-based reasoning  
- agent-based architecture repair (Graph School)  
- adaptive memory over structural states  

---

### How they connect

- **GSL** → evaluates and selects actions based on global state  
- **GitCube** → provides structural understanding of systems (graph topology)

Together they form:

> a system that can both **understand architecture** and **control behavior**

---

### Conceptual mapping

- GitCube → graph / topology / structural risk  
- GSL → state space / field simulation / decision control  

---

This separation allows:

- GitCube to model **structure**
- GSL to regulate **behavior**

---

👉 In short:

GSL decides *what to do*  
GitCube understands *what the system is*
## 🧩 Architecture

- [State Model](./STATE_MODEL.md)
- [Control Layer](./CONTROL_LAYER.md)
- [Benchmark](./BENCHMARK.md)
- [Use Cases](./USE_CASES.md)
- [Multi-Agent Architecture](./MULTI_AGENT_ARCHITECTURE.md)

---

## ▶️ Run

[Open in Colab](https://colab.research.google.com/drive/1XO_GhnqEMdhTLLXklhvlI5kulIqBl60w)

---

## ⚡ Key Result

In adversarial scenarios, GSL selects different actions than baseline:

- reduces residual pressure
- increases coherence
- improves global state stability

This shows that GSL selects based on system dynamics, not local preference.

---

## 🤖 Multi-Agent Demo

- dynamic routing (stabilize / plan / explore)
- coalition selection between agents
- commit / reroute decisions
- multi-step state regulation

---

## 📌 One-line definition

Geometry-Guided State Navigation Layer selects actions by simulating how candidate states reshape a distributed field and preferring those that improve coherence, reduce pressure, and enable stable transitions.
## Canonical Kernel Demo

Minimal kernel pipeline:

```bash
python -m kernel.pipeline
```
Example output:
Decision: {'coalition': 'planner+stabilizer', 'status': 'COMMIT'}
Metrics: {'shadow': 0.05, 'coherence': 0.9, 'target_fit': 0.6, 'vitality': 0.4}
## 🧿 6D State + Bindu + Multi-Agent

This system operates on a six-dimensional state space distributed across a field of nodes.

Each node contains a normalized vector:

V = [Pressure, Flow, Structure, Balance, Law, Future]

Instead of making decisions directly, the system simulates how candidate actions reshape the entire field.

---

### 🔷 1. Six-Dimensional State (6D)

Each dimension represents a fundamental control axis:

- Pressure → unresolved tension (red)
- Flow → adaptability (orange)
- Structure → organization (yellow)
- Balance → internal coherence (green)
- Law → constraints (blue)
- Future → transition readiness (violet)

The system does not optimize a score.

It regulates **geometry of state**.

---

### 🧿 2. Bindu (Critical Transition Point)

Bindu is the moment where the system becomes:

- low pressure  
- highly coherent  
- aligned with target  
- dynamically stable  

At this point:

- the field stops oscillating  
- decisions stabilize  
- transitions become possible  

Bindu is not a threshold —  
it is a **phase transition in system behavior**.

---

### 🤖 3. Multi-Agent Dynamics

The system uses multiple agents:

- planner → builds structure  
- critic → enforces constraints  
- explorer → increases adaptability  
- stabilizer → reduces pressure  

Each agent modifies the state vector differently.

---

### ⚖️ 4. Coalition Selection

Instead of picking a single agent:

→ the system evaluates **combinations of agents**

Example:

- planner + explorer → exploration mode  
- planner + critic → controlled execution  
- planner + stabilizer → stabilization  

The system selects the coalition that:

- reduces pressure  
- increases coherence  
- improves global state  

---

### 🔁 5. Field Simulation Loop

At each step:

1. generate candidate actions  
2. encode into 6D state  
3. apply to field  
4. simulate propagation  
5. evaluate metrics  
6. select best coalition  
7. update memory  

This creates a **closed feedback loop**.

---

### 🧠 6. Memory Fold-In

The system does not reset.

Each accepted step:

→ is stored and affects future decisions

This enables:

- long-horizon behavior  
- structural learning  
- trajectory stabilization  

---

### 🌊 7. Phase Dynamics

The system moves through phases:

- water → high pressure (unstable)  
- gas → transitional  
- plasma → high energy alignment  
- crystal → stable coherent state  

Bindu emerges between plasma → crystal.

---

### ⚡ Key Insight

This system does not choose outputs.

It selects actions based on how they reshape a distributed field.

---

### 🧩 One-line Summary

Multi-agent coalitions regulate a six-dimensional state field and drive it toward a stable transition point (Bindu) through iterative simulation.
