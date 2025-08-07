"""
Project Agora: A.U.R.A. Engine (AURA-0.1)
Part of The Concordia Project v8.2 (B.O.D.Y. Architecture)

Implements A.U.R.A. (Adaptive Utterance Regulation Architecture), a micro-engine
that governs the timing, tone, and necessity of A.D.A.M.'s spoken responses.
"""
import time
from typing import Dict

class AuraEngine:
    """An emotional logic buffer that evaluates the need for speech versus silence."""
    def __init__(self, config: dict):
        self.thresholds = config.get("aura_thresholds", {})
        self.last_latency_ms = 0
        print("A.U.R.A. Engine (AURA-0.1) initialized.")

    def _should_invoke_silence(self, affective_context: dict, proposed_action: dict) -> bool:
        """The core decision logic for invoking silence."""
        hrv = affective_context.get("hrv", 100) # Default to calm if no data
        confidence = proposed_action.get("confidence", 1.0)
        is_crisis = affective_context.get("crisis", False)

        # Crisis switch: NEVER be silent in a crisis
        if is_crisis:
            return False

        if hrv < self.thresholds.get("hrv_threshold", 40):
            return True # User is in a high-stress state

        if confidence < self.thresholds.get("confidence_threshold", 0.4):
            return True # AI is not confident in its response

        return False

    def regulate(self, proposed_action: dict, affective_context: dict) -> dict:
        """Regulates a proposed action, potentially overriding it with silence."""
        start_time = time.perf_counter()

        if self._should_invoke_silence(affective_context, proposed_action):
            final_action = {
                "name": "SacredSilence",
                "description": "Actively holding space for the user without speaking."
            }
        else:
            final_action = proposed_action
        
        end_time = time.perf_counter()
        self.last_latency_ms = (end_time - start_time) * 1000
        return final_action
