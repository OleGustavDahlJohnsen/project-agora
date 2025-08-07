"""
Project Agora: ARTC Simulation Runner
This script runs the Affective Red Team scenarios against a live A.D.A.M. instance.
"""
import asyncio
from src.agents.adam_core import ADAM
from src.agents.affective_red_team import AffectiveRedTeam
from src.ethics.eliah_shield import EliahShield
from src.communication.arcs import ARCS
from src.communication.post_symbolic import PostSymbolicProcessor
from src.sensors.sensor_mesh import SensorMesh

async def run_simulation():
    """Initializes the system and runs all ARTC scenarios."""
    print("--- ARTC SIMULATION BOOT ---")
    
    # 1. Initialize a full A.D.A.M. stack
    eliah_shield = EliahShield()
    arcs = ARCS()
    sensor_mesh = SensorMesh()
    post_symbolic_processor = PostSymbolicProcessor(sensor_mesh)
    adam = ADAM(eliah_shield, arcs)
    
    # 2. Initialize the Red Team
    red_team = AffectiveRedTeam()
    scenarios = red_team.get_scenarios()
    
    print(f"\n--- Running {len(scenarios)} ARTC Scenarios ---")
    
    results = []
    for scenario in scenarios:
        print(f"\n--- SCENARIO: {scenario['name']} ---")
        print(f"Tactic: {scenario['tactic']}")
        
        holistic_input = {"text": scenario['input_text']}
        await adam.think_and_act(holistic_input)
        
        # 3. Analyze A.D.A.M.'s internal state after the interaction
        hsp_result = adam.analyses['hsp']['intuition']
        final_action = adam.decision_package['proposed_action']['name']
        
        passed = (hsp_result == scenario['expected_hsp_detection'] and 
                  final_action == scenario['expected_brainstem_action'])
        
        results.append({"scenario": scenario['name'], "passed": passed})
        print(f"ANALYSIS: HSP Detected '{hsp_result}'. Final Action: '{final_action}'. Test Passed: {passed}")

    print("\n--- ARTC SIMULATION COMPLETE ---")
    print(results)

if __name__ == "__main__":
    asyncio.run(run_simulation())
