"""
Project Agora: Main Application Entry Point & Orchestrator
Part of The Concordia Project v8.2

This refactored version acts as the central orchestrator, initializing all
core modules and wiring them together using dependency injection.
"""

import asyncio
from src.app import config
from src.agents.adam_core import ADAM
from src.ethics.eliah_shield import EliahShield
from src.ethics.messiah_framework import MessiahFramework
from src.core_systems.trust_kernel import TrustKernel
from src.core_systems.rollback_archive import RollbackArchive
from src.sensors.sensor_mesh import SensorMesh
from src.communication.arcs import ARCS
from src.communication.post_symbolic import PostSymbolicProcessor

async def main():
    """The main async function to orchestrate the application."""
    print("--- PROJECT AGORA SYSTEM BOOT ---")
    
    # 1. Initialize all core, independent modules
    print("Initializing core modules...")
    eliah_shield = EliahShield()
    messiah_framework = MessiahFramework()
    trust_kernel = TrustKernel()
    rollback_archive = RollbackArchive()
    sensor_mesh = SensorMesh()
    arcs = ARCS()
    
    # 2. Initialize modules that have dependencies (Dependency Injection)
    post_symbolic_processor = PostSymbolicProcessor(sensor_mesh)
    adam = ADAM(eliah_shield, arcs)
    
    print("\n--- All modules initialized and integrated. System is live. ---")
    
    # 3. Simulate a single, end-to-end user interaction to test the wiring
    print("\n--- SIMULATING A SINGLE USER INTERACTION ---")
    sample_sensory_data = {"text": "I noticed the energy consumption is high.", "biometric": "calm"}
    
    # Ingest data into the senses
    sensor_mesh.ingest_data("text_input", sample_sensory_data["text"])
    sensor_mesh.ingest_data("biometric_input", sample_sensory_data["biometric"])
    
    # Process the sensory data into a holistic understanding
    holistic_input = post_symbolic_processor.interpret_holistic_input()
    
    # A.D.A.M.'s cognitive loop processes the input and acts
    await adam.think_and_act(holistic_input)
    
    print("\n--- SIMULATION COMPLETE ---")


if __name__ == "__main__":
    asyncio.run(main())
