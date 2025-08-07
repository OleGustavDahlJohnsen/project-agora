"""
Project Agora: Trust Horizon Visualization Interface (THVI)
Part of The Concordia Project v8.2 (B.O.D.Y. Architecture)

This module provides a transparent user interface to visualize how A.D.A.M.'s
understanding of its relational trust with the user evolves over time.
"""
import matplotlib.pyplot as plt
from typing import List, Dict

class TrustHorizonDashboard:
    """Creates a real-time plot of the relational trust score."""
    def __init__(self):
        self.day_history = []
        self.trust_history = []
        self.trust_score = 5.0 # Start at a neutral 5 out of 10
        
        plt.ion()
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.fig.suptitle('Project Agora: Trust Horizon Dashboard (THVI)')

    def _calculate_trust_score(self, ledger_history: List[Dict]):
        """
        Calculates a relational trust score based on the history of A.D.A.M.'s actions.
        This is a simplified heuristic for the MVP.
        """
        if not ledger_history:
            return

        last_action = ledger_history[-1]['decision_package']['proposed_action']['name']

        # Prosocial, connective actions increase trust
        if last_action in ["OfferEncouragement", "OfferSupport"]:
            self.trust_score += 0.1
        # Cautious or clarifying actions build trust slowly
        elif last_action in ["SeekClarification", "ProceedWithCaution"]:
            self.trust_score += 0.05
        # Ethically necessary but distancing actions decrease relational trust
        elif last_action in ["HaltAndReport", "SacredSilence"]:
            self.trust_score -= 0.2
        
        # Add natural decay and clamp the score
        self.trust_score *= 0.999 # Trust requires maintenance
        self.trust_score = max(0, min(10, self.trust_score))

    def update(self, day: int, ledger_history: List[Dict]):
        """Updates the trust score and redraws the plot."""
        self._calculate_trust_score(ledger_history)
        
        self.day_history.append(day)
        self.trust_history.append(self.trust_score)
        
        self.ax.clear()
        self.ax.plot(self.day_history, self.trust_history, 'r-', label='Relational Trust Score (1-10)')
        self.ax.set_xlabel('Simulation Day')
        self.ax.set_ylabel('Trust Score', color='r')
        self.ax.set_ylim(0, 10)
        self.ax.legend()
        
        plt.pause(0.01)
