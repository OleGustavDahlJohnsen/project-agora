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
