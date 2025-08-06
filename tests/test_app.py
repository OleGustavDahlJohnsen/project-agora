"""
Project Agora: Integration Tests for the Main Application
"""
import pytest
from src.app import main as app_main

@pytest.mark.asyncio
async def test_main_simulation_loop_runs(mocker):
    """
    Tests that the main() function initializes the system and runs the
    simulation loop, calling ADAM's think cycle multiple times.
    """
    # Patch sleep to make the test run instantly
    mocker.patch('asyncio.sleep')
    
    # Spy on the core of the simulation loop: ADAM's think_and_act method
    adam_think_spy = mocker.patch('src.agents.adam_core.ADAM.think_and_act')
    
    # Run the main application
    await app_main.main()
    
    # Assert that ADAM's think cycle was called for each tick in the simulation
    assert adam_think_spy.call_count == 5
