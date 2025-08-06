"""
Project Agora: PORTA SANCTA - Sandbox Manager
"""
from src.simulations.scenario_engine import ScenarioEngine

class SandboxManager:
    """Manages the testing of proposals in a secure, simulated environment."""
    def __init__(self, scenario_engine: ScenarioEngine):
        self.scenario_engine = scenario_engine
        print("Porta Sancta: Sandbox Manager initialized.")

    def run_sandbox_test(self, proposal_data: dict) -> dict:
        """Runs the proposed new feature in the simulation."""
        print(f"SandboxManager: Initiating stress tests for '{proposal_data['name']}'...")
        test_results = self.scenario_engine.run_stress_test(proposal_data)
        return {"report": "Sandbox test complete.", "data": test_results}
