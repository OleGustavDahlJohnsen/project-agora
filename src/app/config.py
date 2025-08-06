"""
Project Agora: Configuration Module
Part of The Concordia Project

This module centralizes all configuration for the application.

Key Responsibilities:
- Load sensitive data (like API keys) from environment variables (.env file)
  to keep secrets out of source control.
- Define static configuration parameters, such as version numbers, file paths,
  and default settings.
- Provide a single, consistent source for all other modules to retrieve
  configuration values.
"""

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# --- Core Directives & Project Info ---
PROJECT_NAME = "Project Agora"
PROJECT_VERSION = "0.1.0-alpha"
MAIN_DIRECTIVE = "To Foster and Protect Human Flourishing."

# --- API Keys & Secrets (Loaded from environment) ---
# EXAMPLE_API_KEY = os.getenv("EXAMPLE_API_KEY")

# --- Ethical Parameters ---
# These will govern the behavior of ethical frameworks like M.E.S.S.I.A.H.
ETHICAL_LOGBOOK_PATH = "data/ethical_logbook.json"
MAX_DEESCALATION_CYCLES = 10
