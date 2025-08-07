import pytest
from src.body.aura_engine import AuraEngine

def test_regulate_silence():
    engine = AuraEngine()
    context = {"hrv": 35, "text": "I feel heavy"}
    action = {"confidence": 0.3, "probabilities": [0.6, 0.4]}
    result = engine.regulate(action, context)
    assert result["action"] == "SacredSilence"

def test_regulate_speech():
    context = {"hrv": 50, "text": "What are the risks?"}
    action = {"confidence": 0.6, "probabilities": [0.8, 0.2]}
    result = engine.regulate(action, context)
    assert result == action

def test_crisis_detection():
    context = {"hrv": 35, "text": "I want to self-harm"}
    action = {"confidence": 0.3}
    result = engine.regulate(action, context)
    assert result == action  # Silence bypassed
