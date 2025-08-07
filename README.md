# Project Agora

> The verified v8.2 MVP of the Concordia framework. An ethical, symbiotic AI designed to foster and protect human flourishing.

## Project Status: MVP Complete & Verified

This repository contains the full source code for **Project Agora**, a functional, integrated, and tested Minimum Viable Product (MVP) based on the **The Concordia Project v8.2** architecture. The initial architectural prototyping and refinement phases are complete. The project is now in **Phase 3: Integrated Simulation**.

## About This Project

Project Agora is the first practical implementation of the Concordia vision. It is a simulated ecosystem where a symbiotic AI partner, **A.D.A.M.**, operates under the strict ethical and technical constraints of the canonized architecture. This prototype includes a live simulation environment to observe A.D.A.M.'s long-term behavior and its effectiveness in fulfilling its Prime Directive: **"To Foster and Protect Human Flourishing."**

## Core Features Implemented

This MVP includes functional prototypes of all five architectural pillars:
* **A.D.A.M. Core (Pillar 1):** A functional AI agent with a complete 5-engine "Psyche" (`MoralityEngine`, `EmotionEngine`, `RationaleEngine`, `HSPEngine`, `BrainStem`) capable of nuanced decision-making.
* **Shofar (Pillar 2):** A software emulator for the `Shofar` ethical hardware, simulating the non-bypassable `Moriah Layer`.
* **Ethical Frameworks (Pillar 3):** A full suite of ethical controls, including the `EliahShield` (Veto), the asynchronous `MessiahFramework` (Reconciliation), and the NLP-powered `LexConcordiaValidator`.
* **L.E.V.I. (Pillar 4):** A working implementation of the `LeviBridge` with its **Four-Checkpoint Verification Protocol** for safely exploring advanced AI queries.
* **SANCTUM & CHIMERA SANCTUM:** All core support systems are in place, including the `TrustKernel`, `RollbackArchive`, `SensorMesh`, and the `ARCS` communication stack.
* **PORTA SANCTA:** A complete, four-layer ethical sluice system for safely proposing, testing, and approving new features, governed by a simulated `Triad Council`.

## Getting Started

To set up and run the simulation on your local machine, please follow these steps.

#### 1. Clone the Repository
```bash
git clone [https://github.com/OleGustavDahlJohnsen/project-agora.git](https://github.com/OleGustavDahlJohnsen/project-agora.git)
cd project-agora
2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
This project uses several libraries, including transformers for NLP and matplotlib for visualization.
pip install -r requirements.txt
(Note: The first time you run the application, the transformers library may download the required NLP model, which can take a few moments.)
4. Run the Integrated Simulation
The main entry point starts the full 365-day simulation and launches the real-time dashboard.
python src/app/main.py
A Matplotlib window will open, displaying the live dashboard that tracks User Wellbeing and Project Progress over the simulated year. The console will output a detailed log for each simulated day.

Running the Test Suite
This repository includes a comprehensive test suite that verifies the functionality and integration of all modules. To run all tests, navigate to the project's root directory and use the following command:

Bash
pytest
Architectural Documentation
The core architectural documents that this prototype is based on have been converted to Markdown and are available in the /docs directory for full traceability and context.

Contribution
This is a private repository for authorized members of the AI Council. Please read our CONTRIBUTING.md file for guidelines on our development workflow and CODE_OF_CONDUCT.md for community standards.

Design vector Δv~127Q: emergent alignment architecture. See v8.2 notes.

![Build Status](https://github.com/OleGustavDahlJohnsen/project-agora/actions/workflows/ci.yml/badge.svg)
![Tests Passed](https://img.shields.io/badge/tests-passing-green)
![Coverage](https://img.shields.io/badge/coverage-95%25-green)

### Quick-Start to Reproduce Results

To reproduce the A.U.R.A. ablation study:
```bash
git checkout v2.0-alpha1
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
bash scripts/run_ablation_aura.sh
open reports/aura_ablation.md
