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
