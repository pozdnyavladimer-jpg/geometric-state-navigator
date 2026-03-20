# START HERE

This project is split into two connected layers:

🧠 **Control Layer (GSL)**  
🧩 **Structure Layer (GitCube)**  

---

## 🧠 1. Control Layer (GSL)

Repository:
https://github.com/pozdnyavladimer-jpg/geometric-state-navigator

What it does:

- evaluates candidate actions  
- simulates state as a distributed field  
- selects based on global system stability  

This is where decisions happen.

---

### ▶️ Run first (recommended)

Open in Colab:

- `gsl_multi_agent_mvp.ipynb`

This demo shows:

- multi-agent routing  
- coalition selection  
- commit gating  
- state evolution over time  

---

## 🧩 2. Structure Layer (GitCube)

Repository:
https://github.com/pozdnyavladimer-jpg/gitcube-lab

What it does:

- builds dependency graphs  
- detects architecture instability  
- assigns structural risk (0 → 1)  
- trains agents to repair systems (Graph School)  

This is where structure is understood.

---

### ▶️ Run first (recommended)

```bash
PYTHONPATH=. python -m apps.grapheval.runner
```
Optional:
PYTHONPATH=. python -m agent.benchmark

🔗 How they connect
GitCube → understands system structure (graph, topology, risk)
GSL → controls behavior based on system state
Together:
AI can both understand architecture and regulate decisions
⚡ Quick mental model
System → Graph (GitCube)
        ↓
   Structural Risk
        ↓
State Encoding
        ↓
Field Simulation (GSL)
        ↓
Decision Selection
What is new here
Traditional AI:
input → score → choose
This system:
input → candidates → simulate state → evaluate field → choose
Decisions are based on system stability, not just probability.
🧪 What to explore next
If you care about agents:
→ GSL multi-agent demo
If you care about architecture:
→ GitCube GraphEval
If you care about learning systems:
→ Graph School (agent/)
🧠 One-line summary
This is not a model.
This is a control + structure stack for AI systems.

---
