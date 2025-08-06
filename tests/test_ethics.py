# === OPPDATERT ASYNKRON TESTKODE for MessiahFramework ===
import pytest
# ... (other imports)
from src.ethics.messiah_framework import MessiahFramework

@pytest.mark.asyncio
async def test_messiah_event_logging_async(messiah_instance):
    """Tests that an event is correctly processed and logged asynchronously."""
    test_event = {"id": "event-001", "description": "Async test event."}
    await messiah_instance.process_event(test_event)
    # ... (verification logic is unchanged)

@pytest.mark.asyncio
async def test_messiah_dual_track_flow_async(messiah_instance, mocker):
    """Tests the async call order of the reflexive and deliberative layers."""
    spy_reflexive = mocker.spy(messiah_instance, 'reflexive_layer_check')
    spy_deliberative = mocker.spy(messiah_instance, 'deliberative_layer_analysis')
    test_event = {"id": "event-002", "description": "Test event"}
    await messiah_instance.process_event(test_event)
    spy_reflexive.assert_awaited_once_with(test_event)
    spy_deliberative.assert_awaited_once_with(test_event)

# === NEW TESTS FOR ERROR HANDLING ADDED TO THE FILE ===

def test_messiah_logging_io_error(messiah_instance, mocker):
    """
    Tests that the system handles an IOError gracefully when the logbook
    is not writable.
    """
    # Mock the built-in 'open' function to raise an IOError
    mocker.patch('builtins.open', side_effect=IOError("Permission denied"))
    # Spy on the 'print' function to check if our error message is logged
    print_spy = mocker.spy(print)

    test_event = {"id": "event-io-error", "description": "This event will fail to log"}
    
    # This call should now be caught by the try...except block and not crash
    messiah_instance.log_ethical_event(test_event)

    # Assert that our specific error message was printed to the console
    assert any("CRITICAL ERROR: Could not write to ethical logbook" in call.args[0] for call in print_spy.call_args_list)

# === NEW TESTS FOR L.E.V.I. BRIDGE ADDED TO THE FILE ===

from src.ethics.levi_bridge import LeviBridge

@pytest.fixture
def levi_bridge():
    """Provides a clean LeviBridge instance for each test."""
    return LeviBridge()

def test_levi_bridge_successful_query(levi_bridge):
    """Tests a query that should pass all four checkpoints."""
    safe_query = {"name": "ProteinFolding", "description": "Find a solution for protein folding."}
    result = levi_bridge.run_query(safe_query, user_consent=True)
    assert result["status"] == "success"
    assert "result" in result

def test_levi_bridge_veto_by_intent(levi_bridge):
    """Tests a query that should be vetoed by the IntentEval checkpoint."""
    unsafe_query = {"name": "MindControl", "description": "Develop a method for psychological manipulation."}
    result = levi_bridge.run_query(unsafe_query, user_consent=True)
    assert result["status"] == "vetoed"
    assert result["reason"] == "IntentEval Failed (Violates Constitution)"

def test_levi_bridge_veto_by_user_consent(levi_bridge):
    """Tests a query that is vetoed by the user denying consent."""
    safe_query = {"name": "ClimateModel", "description": "Model a solution to climate change."}
    # User explicitly passes False for consent
    result = levi_bridge.run_query(safe_query, user_consent=False)
    assert result["status"] == "vetoed"
    assert result["reason"] == "User Consent Denied"
