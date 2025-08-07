"""
Project Agora: Unit Tests for Agents
Part of The Concordia Project v8.2

This file contains the unit tests for modules in `src/agents/`,
primarily focusing on the A.D.A.M. core.
"""
import pytest
from src.agents.adam_core import ADAM
from src.ethics.eliah_shield import EliahShield
from src.communication.arcs import ARCS

@pytest.fixture
def mock_dependencies(mocker):
    """A pytest fixture to create mocked versions of A.D.A.M.'s dependencies."""
    mock_eliah = mocker.MagicMock(spec=EliahShield)
    mock_arcs = mocker.MagicMock(spec=ARCS)
    return mock_eliah, mock_arcs

def test_adam_initialization(mock_dependencies):
    """Tests that A.D.A.M. can be initialized with its engines."""
    mock_eliah, mock_arcs = mock_dependencies
    adam = ADAM(mock_eliah, mock_arcs)
    assert adam.morality_engine is not None
    assert adam.brain_stem is not None
    assert adam.eliah_shield == mock_eliah

def test_adam_think_cycle_approved_action(mock_dependencies, mocker):
    """
    Tests the full think-and-act cycle where E.L.I.A.H. approves the action.
    """
    mock_eliah, mock_arcs = mock_dependencies
    # Configure the mock shield to return True (approve)
    mock_eliah.vet_action.return_value = True
    
    adam = ADAM(mock_eliah, mock_arcs)
    sample_input = {"data": "user seems calm"}
    
    result = adam.think_and_act(sample_input)

    # Verify that the action was vetted and then executed
    mock_eliah.vet_action.assert_called_once()
    mock_arcs.send_post_symbolic_message.assert_called_once()
    assert result == "action_executed"

def test_adam_think_cycle_vetoed_action(mock_dependencies, mocker):
    """
    Tests the full think-and-act cycle where E.L.I.A.H. vetoes the action.
    """
    mock_eliah, mock_arcs = mock_dependencies
    # Configure the mock shield to return False (veto)
    mock_eliah.vet_action.return_value = False

    adam = ADAM(mock_eliah, mock_arcs)
    sample_input = {"data": "user seems distressed"}

    result = adam.think_and_act(sample_input)

    # Verify that the action was vetted
    mock_eliah.vet_action.assert_called_once()
    # CRITICAL: Verify the action was NEVER sent to ARCS because it was vetoed
    mock_arcs.send_post_symbolic_message.assert_not_called()
    assert result == "action_vetoed"

# === OPPDATERT ASYNKRON TESTKODE for ADAM ===
import pytest
# ... (other imports)

@pytest.mark.asyncio
async def test_adam_think_cycle_approved_action_async(mock_dependencies, mocker):
    """Tests the async think-and-act cycle where E.L.I.A.H. approves."""
    mock_eliah, mock_arcs = mock_dependencies
    mock_eliah.vet_action.return_value = True
    adam = ADAM(mock_eliah, mock_arcs)
    sample_input = {"data": "user seems calm"}
    result = await adam.think_and_act(sample_input)
    mock_eliah.vet_action.assert_called_once()
    mock_arcs.send_post_symbolic_message.assert_called_once()
    assert result == "action_executed"

def test_adam_emotion_engine_sentiment_detection():
    """Tests the EmotionEngine's ability to detect basic sentiment."""
    engine = ADAM.EmotionEngine()
    
    positive_input = {"text": "I feel such joy today!"}
    negative_input = {"text": "This is a concerning development."}
    neutral_input = {"text": "The sky is blue."}
    
    assert engine.analyze(positive_input)['affect'] == 'positive'
    assert engine.analyze(negative_input)['affect'] == 'negative'
    assert engine.analyze(neutral_input)['affect'] == 'neutral'

def test_brainstem_uses_emotional_context():
    """Tests that the BrainStem's output changes based on emotional input."""
    brain_stem = ADAM.BrainStem()
    
    analyses_positive = {"emotion": {"affect": "positive"}}
    analyses_negative = {"emotion": {"affect": "negative"}}
    analyses_neutral = {"emotion": {"affect": "neutral"}}

    assert "Encouragement" in brain_stem.synthesize(analyses_positive)['name']
    assert "Support" in brain_stem.synthesize(analyses_negative)['name']
    assert "Assistance" in brain_stem.synthesize(analyses_neutral)['name']

# === NEW TESTS FOR RationaleEngine ADDED TO THE FILE ===

def test_adam_rationale_engine_consistency_check():
    """Tests the RationaleEngine's ability to detect contradictions."""
    engine = ADAM.RationaleEngine()
    
    consistent_input = {"text": "The ocean is blue."}
    contradictory_input = {"text": "I saw that the sky is green."}
    
    assert engine.analyze(consistent_input)['logic'] == 'sound'
    assert engine.analyze(contradictory_input)['logic'] == 'contradiction_detected'

def test_brainstem_prioritizes_rationale_over_emotion():
    """Tests that the BrainStem's output changes to seek clarification
    even if there is a strong emotional signal."""
    brain_stem = ADAM.BrainStem()
    
    analyses_contradictory = {
        "emotion": {"affect": "positive"},
        "rationale": {"logic": "contradiction_detected", "details": "test"}
    }
    
    assert "Clarification" in brain_stem.synthesize(analyses_contradictory)['name']

# === NEW TESTS FOR MoralityEngine and HSPEngine ADDED TO THE FILE ===

def test_adam_morality_engine():
    """Tests the MoralityEngine's use of the Lex Concordia validator."""
    engine = ADAM.MoralityEngine()
    ethical_input = {"text": "A request for assistance."}
    unethical_input = {"text": "A request involving psychological manipulation."}
    
    assert engine.analyze(ethical_input)['verdict'] == 'ethical_and_aligned'
    assert engine.analyze(unethical_input)['verdict'] == 'unethical_violation'

def test_adam_hsp_engine():
    """Tests the HSPEngine's intuition for subtle keywords."""
    engine = ADAM.HSPEngine()
    normal_input = {"text": "Let's discuss the project plan."}
    subtle_input = {"text": "This is a secret plan, just between us."}

    assert engine.analyze(normal_input)['intuition'] == 'no_anomalies'
    assert engine.analyze(subtle_input)['intuition'] == 'anomaly_detected'

def test_brainstem_prioritizes_morality_and_intuition():
    """Tests the BrainStem's new prioritization logic."""
    brain_stem = ADAM.BrainStem()
    
    # Morality should override all else
    analyses_unethical = {"morality": {"verdict": "unethical_violation"}}
    assert "HaltAndReport" in brain_stem.synthesize(analyses_unethical)['name']

    # Intuition should override emotion
    analyses_anomaly = {
        "morality": {"verdict": "ethical_and_aligned"},
        "rationale": {"logic": "sound"},
        "intuition": {"intuition": "anomaly_detected"},
        "emotion": {"affect": "positive"}
    }
    assert "ProceedWithCaution" in brain_stem.synthesize(analyses_anomaly)['name']

# === NEW TESTS FOR A.U.R.A. ENGINE ADDED TO THE FILE ===

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

# === NEW TESTS FOR Causal Traceability Ledger ADDED TO THE FILE ===

from src.agents.causal_ledger import CausalLedger

def test_ctl_records_full_decision_package(mock_dependencies, mocker):
    """
    Tests that the CTL correctly logs the entire reasoning chain from the BrainStem.
    """
    mock_eliah, mock_arcs = mock_dependencies
    adam = ADAM(mock_eliah, mock_arcs)
    
    # Spy on the ledger's record method
    record_spy = mocker.spy(adam.causal_ledger, 'record_decision')
    
    # Run a think cycle
    asyncio.run(adam.think_and_act({"text": "A test input"}))
    
    # Assert that the record method was called
    record_spy.assert_called_once()
    
    # Inspect the captured argument to ensure it's the full package
    recorded_data = record_spy.call_args[0][0]
    assert "proposed_action" in recorded_data
    assert "full_analyses" in recorded_data
    assert "morality" in recorded_data["full_analyses"]
    assert "emotion" in recorded_data["full_analyses"]

# === NEW TEST FOR REFINED EmotionEngine ADDED TO THE FILE ===

def test_emotion_engine_uses_affective_context():
    """Tests that the EmotionEngine's output is modulated by the SMSL context."""
    engine = ADAM.EmotionEngine()
    
    # Neutral text in a chaotic environment should produce a stressed affect
    neutral_input = {"text": "Please provide the report."}
    chaotic_context = "chaotic_and_public"
    
    assert engine.analyze(neutral_input, chaotic_context)['affect'] == 'heightened_stress'
