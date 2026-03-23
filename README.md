# Geometry-Guided State Navigation Layer (GSL)

GSL is the canonical control layer of the GitCube system.

It defines how candidate actions are interpreted as state transitions,
how field-level metrics are evaluated,
and how stable transitions are selected.

This repository is not the experimental lab and not the runtime OS.

It is the place where system meaning becomes explicit.

---

## ▶️ Quick Start

Start here:

- Multi-agent + Bindu demo → notebooks/gsl_multi_agent_bindu_demo.ipynb
- 3D field simulation → research/simulation_3d_bindu.ipynb
- Text / code encoder → research/gsl_text_encoder_demo.ipynb

---

## What This Repository Is

geometric-state-navigator is the canonical interpretation layer.

It defines:

- state meaning
- threshold meaning
- bindu meaning
- environment meaning
- promotion logic

Full system:

- gitcube-lab → explores
- geometric-state-navigator → explains
- gitcube-os → executes

---

## 🧭 Recommended Flow

1. Run multi-agent demo  
2. Observe field evolution  
3. Run 3D bindu simulation  
4. Run text / code encoder  
5. Read canonical docs  

---

## 🚀 Core Idea

Standard AI:

input → score → choose

GSL:

input → candidates → encode → simulate → evaluate → select → update

Global state > local score

---

## Risk-Level Behavior

LOW RISK  
- planner + explorer  

MEDIUM RISK  
- planner + critic  

HIGH RISK  
- planner + stabilizer  

System reacts to structure, not tokens.

---

## 🧿 6D State

V = [Pressure, Flow, Structure, Balance, Law, Future]

This is a control language, not features.

---

## 🧿 Bindu

Bindu = survival gate

Decides:

- COMMIT
- SOFT_COMMIT
- REJECT
- REROUTE

---

## 🤖 Agents

- planner
- critic
- explorer
- stabilizer

System selects best coalition.

---

## 🔁 Loop

1. generate  
2. encode  
3. simulate  
4. evaluate  
5. select  
6. bindu  
7. memory  

---

## 🧠 Memory

Only stable transitions persist.

---

## 🌊 Phases

- water  
- gas  
- plasma  
- crystal  

Bindu → transition point

---

## 📚 Canon

- docs/STATE_CANON.md  
- docs/THRESHOLD_CANON.md  
- docs/BINDU_CANON.md  
- docs/ENVIRONMENT_CANON.md  
- docs/PROMOTION_RULES.md  
- docs/PROMOTION_CANDIDATES.md  
- docs/REPO_MAP.md  

---

## 🔗 Repositories

Lab → experiments  
Navigator → meaning  
OS → execution  

---

## ⚡ One-line

GSL selects actions by evaluating how they reshape a distributed state field.
