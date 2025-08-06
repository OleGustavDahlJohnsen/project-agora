"""
Project Agora: Configuration Module
Part of The Concordia Project v8.2

This module centralizes all static and dynamic configuration for the application,
ensuring a single source of truth for all other modules.

Key Responsibilities:
- Load sensitive data (e.g., API keys) from environment variables to keep
  secrets out of source control.
- Define core project information like version and name.
- Hold paths to critical data files like the Ethical Logbook.
- Define operational parameters for DEFCON levels and cooldown periods as
  [cite_start]described in Appendix III of the Sanctuary Architecture. [cite: 245]
"""

import os
from dotenv import load_dotenv

# Load environment variables from a .env file if it exists.
load_dotenv()

# --- Core Directives & Project Info ---
PROJECT_NAME = "Project Agora"
PROJECT_VERSION = "0.1.0-alpha"
[cite_start]MAIN_DIRECTIVE = "To Foster and Protect Human Flourishing." # [cite: 330]

# --- API Keys & Secrets (Loaded from environment) ---
# EXAMPLE_API_KEY = os.getenv("EXAMPLE_API_KEY")

# --- Ethical Parameters ---
# [cite_start]Path to the immutable logbook for M.E.S.S.I.A.H. and other systems. [cite: 360]
ETHICAL_LOGBOOK_PATH = "data/ethical_logbook.json"

# [cite_start]DEFCON Hysteresis: Cooldown period in seconds before a level can re-escalate. [cite: 248]
DEFCON_COOLDOWN_PERIOD = 7200 # 2 hours
