"""
Project Agora: Unit Tests for the A.U.R.A. Engine
"""
import pytest
from src.agents.aura_engine import AuraEngine

def test_aura_engine_proposes_silence_in_negative_context():
    """Tests that AURA overrides a non-support action with silence when affect is negative."""
    aura = AuraEngine()
    # A.D.A.M. wants to seek clarification, but the user is distressed
    action = {"name": "SeekClarification", "description": "..."}
    context = {"affect": "negative"}
    
    regulated_action = aura.regulate(action, context)
    assert regulated_action["name"] == "SacredSilence"

def test_aura_engine_allows_support_in_negative_context():
    """Tests that AURA correctly allows a direct support action even when affect is negative."""
    aura = AuraEngine()
    action = {"name": "OfferSupport", "description": "..."}
    context = {"affect": "negative"}
    
    regulated_action = aura.regulate(action, context)
    assert regulated_action["name"] == "OfferSupport"

def test_aura_engine_suppresses_unnecessary_speech():
    """Tests that AURA suppresses a generic, low-impact response in a neutral context."""
    aura = AuraEngine()
    action = {"name": "OfferAssistance", "description": "..."}
    context = {"affect": "neutral"}
    
    regulated_action = aura.regulate(action, context)
    assert regulated_action["name"] == "SilentObservation"
