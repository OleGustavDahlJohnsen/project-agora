"""
Project Agora: Unit Tests for the Trust Horizon Visualization Interface
"""
import pytest
from src.visualization.trust_horizon import TrustHorizonDashboard

# Mock matplotlib to prevent it from creating a GUI window during tests
@pytest.fixture(autouse=True)
def mock_matplotlib(mocker):
    mocker.patch('matplotlib.pyplot.ion')
    mocker.patch('matplotlib.pyplot.subplots')
    mocker.patch('matplotlib.pyplot.pause')

def test_thvi_trust_score_logic():
    """
    Tests that the TrustHorizonDashboard correctly calculates the trust score
    based on a series of mock ledger entries.
    """
    thvi_dash = TrustHorizonDashboard()
    
    # Initial state
    assert thvi_dash.trust_score == 5.0
    
    # A supportive action should increase the score
    ledger_1 = [{"decision_package": {"proposed_action": {"name": "OfferSupport"}}}]
    thvi_dash._calculate_trust_score(ledger_1)
    assert thvi_dash.trust_score > 5.0

    # A vetoed action should decrease the score
    initial_score = thvi_dash.trust_score
    ledger_2 = ledger_1 + [{"decision_package": {"proposed_action": {"name": "HaltAndReport"}}}]
    thvi_dash._calculate_trust_score(ledger_2)
    assert thvi_dash.trust_score < initial_score
