"""
Project Agora: PORTA SANCTA - Proposal Handler
"""
class ProposalHandler:
    """Handles the submission and initial processing of new proposals."""
    def __init__(self):
        self.proposals_db = {}
        print("Porta Sancta: Proposal Handler initialized.")

    def submit_proposal(self, user_id, proposal_data):
        if all(k in proposal_data for k in ('name', 'description')):
            proposal_id = len(self.proposals_db) + 1
            self.proposals_db[proposal_id] = proposal_data
            return {"status": "submitted", "proposal_id": proposal_id, "data": proposal_data}
        return {"status": "rejected", "reason": "Incomplete proposal."}
