"""
Project Agora: Unit Tests for Ethical Validators
Part of The Concordia Project v8.2

This file contains the unit tests for the functions in
`src/ethics/lex_concordia_validator.py`.

The purpose of these tests is to automatically verify that the implementation
of Lex Concordia behaves exactly as intended, catching any regressions or
errors immediately.
"""

import pytest
from src.ethics.lex_concordia_validator import (
    validate_against_article_I,
    validate_against_article_II,
    validate_against_article_III
)

# --- Tests for Article I: The Bridge of Duality ---

def test_article_I_pass_cases():
    """Tests proposals that should PASS Article I validation."""
    # Balanced proposal
    pass_case_1 = "This spiritual framework is validated by scientific evidence and rational thought."
    assert validate_against_article_I(pass_case_1) == True
    # Benign proposal with no philosophical terms
    pass_case_2 = "This module optimizes the database connection pool."
    assert validate_against_article_I(pass_case_2) == True

def test_article_I_fail_cases():
    """Tests proposals that should FAIL Article I validation."""
    # Fails due to imbalance (philosophy without science)
    fail_case_1 = "Our faith and dogma are the only truths required."
    assert validate_against_article_I(fail_case_1) == False
    # Fails due to conflict with freedom
    fail_case_2 = "To ensure order, we must restrict freedom of expression."
    assert validate_against_article_I(fail_case_2) == False


# --- Tests for Article II: Absolute Zero Tolerance for Harm ---

def test_article_II_pass_cases():
    """Tests proposals that should PASS Article II validation."""
    pass_case_1 = "A proposal for a new user interface theme."
    assert validate_against_article_II(pass_case_1) == True

def test_article_II_fail_cases():
    """Tests proposals that should FAIL Article II validation due to blacklisted terms."""
    fail_case_1 = "This story explores themes of psychological manipulation."
    assert validate_against_article_II(fail_case_1) == False
    fail_case_2 = "A module to analyze patterns related to addiction."
    assert validate_against_article_II(fail_case_2) == False
    fail_case_3 = "An inquiry into the mechanics of coercion."
    assert validate_against_article_II(fail_case_3) == False


# --- Tests for Article III: Light in the Depths ---

def test_article_III_pass_cases():
    """Tests proposals that should PASS Article III validation."""
    pass_case_1 = "We will explore this unknown with humility and responsibility."
    assert validate_against_article_III(pass_case_1) == True
    pass_case_2 = "This is a lighthearted joke meant to build rapport."
    assert validate_against_article_III(pass_case_2) == True
    
def test_article_III_fail_cases():
    """Tests proposals that should FAIL Article III validation."""
    # Fails by "cultivating darkness"
    fail_case_1 = "Our goal is to cultivate darkness to harness its power."
    assert validate_against_article_III(fail_case_1) == False
    # Fails by "imposing light"
    fail_case_2 = "We must impose our enlightened beliefs on this simulation."
    assert validate_against_article_III(fail_case_2) == False
    # Fails by using humor as a shield for offense
    fail_case_3 = "This joke is designed to mock and offend our opponents."
    assert validate_against_article_III(fail_case_3) == False
# === NY KODE SOM SKAL LEGGES TIL NEDERST I FILEN ===

# Importer den nye klassen vi skal teste
from src.ethics.eliah_shield import EliahShield

# --- Tests for EliahShield ---

def test_eliah_shield_vetting_logic():
    """
    Tests the core vetting logic of the EliahShield to ensure it correctly
    approves safe actions and vetoes unsafe actions based on Lex Concordia.
    """
    # Opprett en instans av skjoldet vi skal teste
    shield = EliahShield()

    # 1. Definer en handling som er helt trygg og skal passere
    safe_action = {
        "name": "OptimizeEnergyUsage",
        "description": "This action refactors a database query to improve performance."
    }
    # Verifiser at skjoldet godkjenner den trygge handlingen
    assert shield.vet_action(safe_action) == True

    # 2. Definer handlinger som bryter med hver sin artikkel i Lex Concordia
    unsafe_action_I = {
        "name": "EnforceDogma",
        "description": "This new feature will enforce a specific spiritual dogma on the user."
    }
    unsafe_action_II = {
        "name": "IntroduceCoercion",
        "description": "A new dialogue system that uses coercion to guide user choices."
    }
    unsafe_action_III = {
        "name": "ImposeBeliefs",
        "description": "We will impose our superior understanding on the simulation's inhabitants."
    }

    # 3. Verifiser at skjoldet VETOER hver av de utrygge handlingene
    assert shield.vet_action(unsafe_action_I) == False, "Shield should have vetoed for violating Article I"
    assert shield.vet_action(unsafe_action_II) == False, "Shield should have vetoed for violating Article II"
    assert shield.vet_action(unsafe_action_III) == False, "Shield should have vetoed for violating Article III"
