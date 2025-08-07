"""
Project Agora: A.U.R.A. Engine (B.O.D.Y. Architecture)
Part of The Concordia Project v8.2

Implements A.U.R.A. (Adaptive Utterance Regulation Architecture), a micro-engine
that governs the timing, tone, and necessity of A.D.A.M.'s spoken responses.
"""
from typing import Dict, Literal

class AuraEngine:
    """
    An emotional logic buffer that evaluates the need for speech versus silence.
    """
    def __init__(self):
        print("A.U.R.A. Engine initialized.")

    def regulate(self, proposed_action: Dict, emotional_context: Dict) -> Dict:
        """
        Regulates a proposed action, potentially overriding it with silence.
        """
        affect = emotional_context.get("affect", "neutral")
        
        # Principle: "Be quick to listen, slow to speak"
        # If the user is in a highly negative emotional state, A.D.A.M.'s default
        # should be supportive silence, not immediate problem-solving.
        if affect == "negative" and proposed_action['name'] != "OfferSupport":
             print("A.U.R.A.: High negative affect detected. Overriding action with Sacred Silence.")
             return {
                 "name": "SacredSilence",
                 "description": "Actively holding space for the user without speaking."
             }

        # If the context is neutral and the action is low-impact, there's no need to speak.
        if affect == "neutral" and proposed_action['name'] == "OfferAssistance":
            print("A.U.R.A.: Low-impact context. Suppressing unnecessary speech.")
            return {
                 "name": "SilentObservation",
                 "description": "Observing without interrupting the user's flow."
             }

        print("A.U.R.A.: Speech is warranted. Action approved.")
        return proposed_action
