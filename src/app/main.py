"""
Project Agora: Main Application Entry Point & Orchestrator (THVI Integrated)
"""
import asyncio
from src.simulations.virtual_life import Simulation
from src.visualization.dashboard import Dashboard
from src.visualization.trust_horizon import TrustHorizonDashboard
from src.agents.adam_core import ADAM
from src.ethics.eliah_shield import EliahShield
from src.communication.arcs import ARCS
from src.communication.post_symbolic import PostSymbolicProcessor
from src.sensors.sensor_mesh import SensorMesh
from src.agents.unified_context_buffer import UnifiedContextBuffer
from src.sensors.multimodal_fusion_layer import MultimodalFusionLayer

async def main():
    """The main async function to orchestrate the application."""
    print("--- PROJECT AGORA SYSTEM BOOT (VISUAL SIMULATION V2) ---")
    
    # 1. Initialize all modules
    eliah_shield = EliahShield()
    arcs = ARCS()
    ucb = UnifiedContextBuffer()
    mfl = MultimodalFusionLayer()
    sensor_mesh = SensorMesh()
    post_symbolic_processor = PostSymbolicProcessor(sensor_mesh)
    adam = ADAM(eliah_shield, arcs, ucb, sensor_mesh)
    simulation = Simulation()
    dashboard = Dashboard()
    trust_dashboard = TrustHorizonDashboard() # Initialize the THVI dashboard
    
    print("\n--- All modules initialized. Starting persistent simulation. ---")
    
    # ... (simulation loop logic is mostly unchanged)
    simulation_ticks = 50
    # ...

    for i in range(simulation_ticks):
        # ... (core logic of the loop is unchanged)
        
        # UPDATE: Update both dashboards with the new world state
        dashboard.update(simulation.world_state)
        trust_dashboard.update(simulation.world_state['day'], adam.causal_ledger.ledger)
        
        await asyncio.sleep(0.2)

    print("\n--- SIMULATION COMPLETE ---")
    input("Press Enter to close the plot and exit.")

if __name__ == "__main__":
    asyncio.run(main())
