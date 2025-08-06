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

"""
Project Agora: Unit Tests for the Dynamic Simulation Systems
"""
# ... (previous imports)
from src.simulations.virtual_life import Simulation

def test_simulation_world_state_changes_on_action():
    """Tests that the world state changes correctly based on an action."""
    sim = Simulation()
    initial_wellbeing = sim.world_state["user_wellbeing"]
    
    support_action = {'name': 'OfferSupport'}
    sim.run_tick(support_action)
    
    assert sim.world_state["user_wellbeing"] > initial_wellbeing

def test_simulation_dynamic_event_generation():
    """Tests that the simulation generates state-appropriate events."""
    sim = Simulation()
    
    # Test high-stress event
    sim.world_state["user_wellbeing"] = 3.0
    event1 = sim._generate_next_event()
    assert "overwhelmed" in event1["text"]
    
    # Test normal event
    sim.world_state["user_wellbeing"] = 8.0
    event2 = sim._generate_next_event()
    assert "calm day" in event2["text"]
