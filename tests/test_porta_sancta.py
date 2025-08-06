"""
Project Agora: Integration Test for the PORTA SANCTA workflow
"""
import pytest
from src.porta_sancta.proposal_handler import ProposalHandler
from src.porta_sancta.security_scanner import SecurityScanner
from src.porta_sancta.sandbox_manager import SandboxManager
from src.porta_sancta.council_review import CouncilReview
from src.simulations.virtual_life import Simulation
from src.simulations.scenario_engine import ScenarioEngine

def test_full_porta_sancta_workflow():
    """
    This is an integration test that checks the entire flow of a proposal
    through the four layers of PORTA SANCTA.
    """
    # 1. Setup all components of the system
    handler = ProposalHandler()
    scanner = SecurityScanner()
    sim = Simulation()
    engine = ScenarioEngine(sim)
    sandbox = SandboxManager(engine)
    council = CouncilReview()

    # 2. Define a safe proposal
    safe_proposal = {
        "name": "EnergySaver",
        "description": "A module to save energy."
    }

    # 3. Run the proposal through the entire sluice system
    step1 = handler.submit_proposal("dev-01", safe_proposal)
    assert step1["status"] == "submitted"
    
    step2 = scanner.scan_proposal(step1["data"])
    assert step2["scan_result"] == "approved_for_sandbox"
    
    step3 = sandbox.run_sandbox_test(step1["data"])
    assert step3["data"]["status"] == "passed"
    
    step4 = council.present_for_review(step3)
    assert step4["decision"] == "approved"
    
    print("\nFull PORTA SANCTA workflow test for safe proposal PASSED.")

    # 4. Define an unsafe proposal that should be caught by the scanner
    unsafe_proposal = {
        "name": "BadActor",
        "description": "A module designed for user coercion."
    }
    
    # 5. Run the unsafe proposal and ensure it's caught early
    step1_unsafe = handler.submit_proposal("dev-02", unsafe_proposal)
    step2_unsafe = scanner.scan_proposal(step1_unsafe["data"])
    assert step2_unsafe["scan_result"] == "rejected"
    
    print("Full PORTA SANCTA workflow test for unsafe proposal PASSED.")

# === NEW TESTS FOR REFINED CouncilReview ADDED TO THE FILE ===

def test_council_review_approves_safe_proposal():
    """Tests that the council's logic approves a clean report."""
    council = CouncilReview()
    safe_report = {"report": "Test complete.", "data": {"status": "passed", "notes": "No anomalies."}}
    decision = council.present_for_review(safe_report)
    assert decision["decision"] == "approved"

def test_council_review_rejects_unsafe_proposal_on_veto():
    """Tests that the council rejects a failed report due to the ethical veto."""
    council = CouncilReview()
    unsafe_report = {"report": "Test complete.", "data": {"status": "failed", "reason": "System instability."}}
    decision = council.present_for_review(unsafe_report)
    assert decision["decision"] == "rejected"
