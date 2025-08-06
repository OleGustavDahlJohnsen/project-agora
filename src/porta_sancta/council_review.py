"""
Project Agora: PORTA SANCTA - Council Review (Refined)
Part of the PORTA SANCTA Ethical Sluice System v1.0

This module implements Layer 4, simulating the Triad Council's
deliberation and decision-making process based on sandbox test data.
"""

class CouncilReview:
    """Manages the final, manual review and approval process."""
    def __init__(self):
        print("Porta Sancta: Council Review module (Refined) initialized.")

    def _simulate_triad_council_vote(self, test_report: dict) -> dict:
        """Simulates the voting of the three council members."""
        votes = {}
        report_data = test_report.get("data", {})
        
        # Ethics/Law Vote (has veto power)
        if report_data.get("status") == "failed":
            votes["ethics_law"] = "NO (VETO)"
        else:
            votes["ethics_law"] = "YES"
            
        # Security Vote (e.g., The Sentinel)
        # For MVP, let's assume security concerns are in the report notes
        if "vulnerability" in report_data.get("notes", ""):
             votes["security"] = "NO"
        else:
             votes["security"] = "YES"
        
        # Economics Vote
        # For MVP, assume economics are always favorable
        votes["economics"] = "YES"
        
        # Determine final decision
        if votes["ethics_law"] == "NO (VETO)":
            final_decision = "rejected"
        else:
            # Simple majority needed (in this case, 2/3 YES votes)
            yes_votes = list(votes.values()).count("YES")
            if yes_votes >= 2:
                final_decision = "approved"
            else:
                final_decision = "rejected"
        
        return {"decision": final_decision, "votes": votes}


    def present_for_review(self, test_report: dict) -> dict:
        """Presents a test report to the Triad Council for a decision."""
        print(f"CouncilReview: Presenting report to Triad Council...")
        
        deliberation_result = self._simulate_triad_council_vote(test_report)
        print(f"CouncilReview: Deliberation complete. Votes: {deliberation_result['votes']}")

        if deliberation_result["decision"] == "approved":
            print("CouncilReview: Proposal approved by the Triad Council.")
            return {"decision": "approved", "defcon": 5} # Assigns a low-risk DEFCON level
        else:
            print("CouncilReview: Proposal rejected by the Triad Council.")
            return {"decision": "rejected", "reason": "Failed to secure council majority or was vetoed."}
