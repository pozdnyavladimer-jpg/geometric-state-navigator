# Geometry-Guided State Navigation Layer (GSL)

GSL is a control layer for nonlinear state regulation on top of existing AI systems.

Instead of selecting outputs by probability or score, GSL evaluates how candidate states reshape a distributed field and selects the one that improves global system stability.

---
## Text / Code Encoder Demo
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
