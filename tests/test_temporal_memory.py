"""
Project Agora: Unit Tests for the Temporal Memory Weaving Engine
"""
import pytest
from src.agents.temporal_memory import TemporalMemory

def generate_mock_ledger_entry(action_name: str):
    """Helper function to create mock ledger entries."""
    return {
        "timestamp_utc": "...",
        "decision_package": {
            "proposed_action": {"name": action_name, "description": "..."},
            "full_analyses": {}
        }
    }

def test_tmwe_detects_deepening_trust():
    """Tests that the TMW-E can identify a pattern of trust from ledger history."""
    memory_engine = TemporalMemory()
    
    mock_ledger = [
        generate_mock_ledger_entry("OfferSupport"),
        generate_mock_ledger_entry("SeekClarification"),
        generate_mock_ledger_entry("OfferSupport"),
        generate_mock_ledger_entry("OfferEncouragement"),
        generate_mock_ledger_entry("OfferSupport"), # More support than clarification
    ]
    
    analysis = memory_engine.analyze_ledger(mock_ledger)
    assert analysis["trust_pattern"] == "deepening_trust"
    assert "deepening of trust" in analysis["wisdom_summary"]

def test_tmwe_detects_cautious_interaction():
    """Tests that the TMW-E can identify a pattern of caution."""
    memory_engine = TemporalMemory()
    
    mock_ledger = [
        generate_mock_ledger_entry("SeekClarification"),
        generate_mock_ledger_entry("SeekClarification"),
        generate_mock_ledger_entry("OfferSupport"),
    ]
    
    analysis = memory_engine.analyze_ledger(mock_ledger)
    assert analysis["trust_pattern"] == "cautious_interaction"
