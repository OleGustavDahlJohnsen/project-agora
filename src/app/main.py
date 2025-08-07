"""
Project Agora: Main Application Entry Point & Orchestrator (Final B.O.D.Y. Sim)
Part of The Concordia Project v8.2

This final version orchestrates the full B.O.D.Y. architecture and runs the
persistent, long-duration simulation to observe emergent behavior and generate
verifiable results.
"""

import asyncio
import csv
from src.agents.adam_core import ADAM
from src.agents.unified_context_buffer import UnifiedContextBuffer
from src.communication.arcs import ARCS
from src.communication.post_symbolic import PostSymbolicProcessor
from src.ethics.eliah_shield import EliahShield
from src.sensors.multimodal_fusion_layer import MultimodalFusionLayer
from src.sensors.sensor_mesh import SensorMesh
from src.simulations.virtual_life import Simulation
from src.visualization.dashboard import Dashboard
from src.visualization.trust_horizon import TrustHorizonDashboard

async def main():
    """The main async function to orchestrate the long-duration simulation."""
    print("--- PROJECT AGORA V2.0 (B.O.D.Y.) SYSTEM BOOT ---")
    
    # 1. Initialize all core modules
    print("Initializing core modules...")
    eliah_shield = EliahShield()
    arcs = ARCS()
    ucb = UnifiedContextBuffer()
    mfl = MultimodalFusionLayer()
    sensor_mesh = SensorMesh()
    post_symbolic_processor = PostSymbolicProcessor(sensor_mesh)
    adam = ADAM(eliah_shield, arcs, ucb, sensor_mesh)
    simulation = Simulation()
    dashboard = Dashboard()
    trust_dashboard = TrustHorizonDashboard()
    
    print("\n--- All modules initialized. Starting 365-day simulation. ---")
    
    # 2. Main Simulation Loop
    simulation_ticks = 365
    simulation_history = []
    next_event = simulation._generate_next_event()

    for i in range(simulation_ticks):
        print(f"\n--- SIMULATION DAY {i+1} ---")
        
        # a. Fuse sensory input and add to the Unified Context Buffer
        fused_perception = mfl.fuse_and_scale_inputs([
            {"modality": "text", "data": next_event.get("text", "")},
            {"modality": "biometric", "data": next_event.get("biometric", "")}
        ])
        ucb.add_perception(fused_perception)
        
        # b. A.D.A.M.'s cognitive loop processes the latest context from the UCB
        await adam.think_and_act()
        
        # c. The simulation world evolves based on A.D.A.M.'s action
        last_action = adam.decision_package['proposed_action'] if adam.decision_package else None
        next_event = simulation.run_tick(last_action)
        
        # d. Log the world state for final analysis
        simulation_history.append(simulation.world_state.copy())
        
        # e. Update the live dashboards
        dashboard.update(simulation.world_state)
        trust_dashboard.update(simulation.world_state['day'], adam.causal_ledger.ledger)
        
        await asyncio.sleep(0.01) # Minimal sleep for speed

    print("\n--- SIMULATION COMPLETE ---")
    
    # 3. Save final results to a CSV file for analysis
    output_file = "simulation_results.csv"
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=simulation_history[0].keys())
        writer.writeheader()
        writer.writerows(simulation_history)
    print(f"Results for {simulation_ticks} days saved to {output_file}.")
    input("Press Enter to close the plots and exit.")


if __name__ == "__main__":
    asyncio.run(main())
