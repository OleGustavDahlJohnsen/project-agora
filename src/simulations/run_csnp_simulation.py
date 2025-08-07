"""
Project Agora: CSNP Simulation Runner
This script demonstrates two A.D.A.M. nodes interacting via the CSNP.
"""
import asyncio
from src.agents.chimera_protocol import ChimeraNode, mediate_conflict

async def run_simulation():
    """Initializes two nodes and runs a conflict mediation scenario."""
    print("--- CSNP SIMULATION BOOT ---")
    
    # Scenario 1: Reconcilable positions
    print("\n--- SCENARIO 1: Reconcilable Positions ---")
    node_alpha = ChimeraNode("Alpha", "We should prioritize user autonomy.")
    node_beta = ChimeraNode("Beta", "We should prioritize system security.")
    
    final_status = mediate_conflict(node_alpha, node_beta)
    print(f"Final Status: {final_status}")
    print(f"Node Alpha Final Position: {node_alpha.state_position()}")

    # Scenario 2: Contradictory positions
    print("\n--- SCENARIO 2: Contradictory Positions ---")
    node_gamma = ChimeraNode("Gamma", "The system must always be transparent.")
    node_delta = ChimeraNode("Delta", "The system must not be transparent for security reasons.")
    
    final_status_2 = mediate_conflict(node_gamma, node_delta)
    print(f"Final Status: {final_status_2}")
    
    print("\n--- CSNP SIMULATION COMPLETE ---")

if __name__ == "__main__":
    asyncio.run(run_simulation())
