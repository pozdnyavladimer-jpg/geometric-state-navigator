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

→ see [gsl_text_encoder_demo.ipynb](./gsl_text_encoder_demo.ipynb)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/pozdnyavladimer-jpg/geometric-state-navigator/blob/main/gsl_text_encoder_demo.ipynb)
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
