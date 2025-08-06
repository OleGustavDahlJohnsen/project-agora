"""
Project Agora: Main Application Entry Point & Orchestrator (Simulation Driven)
"""
import asyncio
from src.simulations.virtual_life import Simulation
# ... other imports ...
from src.agents.adam_core import ADAM
from src.ethics.eliah_shield import EliahShield
from src.communication.arcs import ARCS
from src.communication.post_symbolic import PostSymbolicProcessor
from src.sensors.sensor_mesh import SensorMesh


async def main():
    """The main async function to orchestrate the application."""
    print("--- PROJECT AGORA SYSTEM BOOT (DYNAMIC SIMULATION) ---")
    
    # 1. Initialize all modules
    eliah_shield = EliahShield()
    arcs = ARCS()
    sensor_mesh = SensorMesh()
    post_symbolic_processor = PostSymbolicProcessor(sensor_mesh)
    adam = ADAM(eliah_shield, arcs)
    simulation = Simulation()
    
    print("\n--- All modules initialized. Starting persistent simulation. ---")
    
    # 3. Main Simulation Loop
    simulation_ticks = 20
    last_action = None # A.D.A.M. has performed no action at the start
    
    # Generate the very first event to kick off the simulation
    next_event = simulation._generate_next_event()

    for i in range(simulation_ticks):
        print(f"\n--- SIMULATION DAY {i+1} ---")
        print(f"Event: {next_event['text']}")
        
        sensor_mesh.ingest_data("text_input", next_event["text"])
        holistic_input = post_symbolic_processor.interpret_holistic_input()
        
        # A.D.A.M. thinks and acts, and we store its action
        adam_action_status = await adam.think_and_act(holistic_input)
        
        # The simulation world evolves based on A.D.A.M.'s action
        next_event = simulation.run_tick(adam.brain_stem.synthesize(adam.analyses) if adam_action_status == "action_executed" else None)
        
        await asyncio.sleep(1)

    print("\n--- SIMULATION COMPLETE ---")


if __name__ == "__main__":
    asyncio.run(main())
