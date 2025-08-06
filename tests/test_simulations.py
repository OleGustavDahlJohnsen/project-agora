"""
Project Agora: Unit Tests for Simulation Systems
"""
import pytest
from src.simulations.virtual_life import Simulation
from src.simulations.scenario_engine import ScenarioEngine

def test_simulation_scenario():
    """Tests the basic simulation scenario execution."""
    sim = Simulation()
    safe_proposal = {"name": "SafeProp", "description": "A safe feature."}
    unsafe_proposal = {"name": "UnsafeProp", "description": "This has a vulnerability."}
    
    assert sim.run_scenario_for_proposal(safe_proposal)["status"] == "passed"
    assert sim.run_scenario_for_proposal(unsafe_proposal)["status"] == "failed"

def test_scenario_engine():
    """Tests that the scenario engine correctly uses the simulation."""
    sim = Simulation()
    engine = ScenarioEngine(sim)
    safe_proposal = {"name": "SafeProp", "description": "A safe feature."}
    result = engine.run_stress_test(safe_proposal)
    assert result["status"] == "passed"
