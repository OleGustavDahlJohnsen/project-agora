"""
Project Agora: Integration Tests for the Main Application
"""
import pytest
from src.app import main as app_main

# By patching the __init__ methods, we can check if our main orchestrator
# is actually creating instances of all our classes without running their full logic.
@pytest.mark.asyncio
async def test_main_orchestration_initializes_all_modules(mocker):
    """
    Tests that the main() function correctly instantiates all core modules.
    """
    # Prevent file I/O and plotting during this test
    mocker.patch('builtins.open')
    mocker.patch('matplotlib.pyplot.show')
    mocker.patch('asyncio.sleep')

    # Spy on the constructors of our main classes
    spy_adam = mocker.patch('src.agents.adam_core.ADAM.__init__', return_value=None)
    spy_eliah = mocker.patch('src.ethics.eliah_shield.EliahShield.__init__', return_value=None)
    spy_simulation = mocker.patch('src.simulations.virtual_life.Simulation.__init__', return_value=None)
    spy_dashboard = mocker.patch('src.visualization.dashboard.Dashboard.__init__', return_value=None)
    
    # Spy on the core of the simulation loop: ADAM's think_and_act method
    adam_think_spy = mocker.patch('src.agents.adam_core.ADAM.think_and_act')
    
    # Run the main application
    await app_main.main()
    
    # Assert that the constructor for each core module was called exactly once
    spy_adam.assert_called_once()
    spy_eliah.assert_called_once()
    spy_simulation.assert_called_once()
    spy_dashboard.assert_called_once()
    
    # Assert that ADAM's think cycle was called for each tick in the simulation
    assert adam_think_spy.call_count == 365
