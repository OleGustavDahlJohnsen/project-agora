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
    # Spy on the constructors of our main classes
    spy_adam = mocker.patch('src.agents.adam_core.ADAM.__init__', return_value=None)
    spy_eliah = mocker.patch('src.ethics.eliah_shield.EliahShield.__init__', return_value=None)
    spy_messiah = mocker.patch('src.ethics.messiah_framework.MessiahFramework.__init__', return_value=None)
    spy_sensor_mesh = mocker.patch('src.sensors.sensor_mesh.SensorMesh.__init__', return_value=None)
    spy_arcs = mocker.patch('src.communication.arcs.ARCS.__init__', return_value=None)
    
    # Run the main application orchestrator
    await app_main.main()
    
    # Assert that the constructor for each core module was called exactly once
    spy_adam.assert_called_once()
    spy_eliah.assert_called_once()
    spy_messiah.assert_called_once()
    spy_sensor_mesh.assert_called_once()
    spy_arcs.assert_called_once()
