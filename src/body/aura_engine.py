import numpy as np
from typing import Dict

class AuraEngine:
    """An emotional logic buffer that evaluates the need for speech versus silence."""

    def __init__(self, config: Dict = None):
        """Initializes with default thresholds."""
        if config is None:
            config = {}
        self.thresholds = config.get("aura_thresholds", {
            "hrv_threshold": 40,  # ms RMSSD for fragility
            "confidence_threshold": 0.4,  # Model confidence
            "max_silence_duration": 30  # Seconds
        })

    def _should_invoke_silence(self, affective_context: Dict, proposed_action: Dict) -> bool:
        """Check if silence should be invoked based on thresholds."""
        hrv = affective_context.get("hrv", 0)  # Dummy HRV (replace with real sensor data later)
        confidence = proposed_action.get("confidence", 0)
        # Crisis detection: Bypass silence for self-harm keywords
        if "self-harm" in affective_context.get("text", "").lower():
            return False
        # Entropy check for uncertainty
        if 'probabilities' in proposed_action:
            probs = np.array(proposed_action['probabilities'])
            entropy = -np.sum(probs * np.log(probs + 1e-10))
            if entropy > 0.7:
                return True
        return hrv < self.thresholds["hrv_threshold"] or confidence < self.thresholds["confidence_threshold"]

    def _create_silent_action(self) -> Dict:
        """Create a silent action with non-verbal feedback."""
        return {
            "action": "SacredSilence",
            "output": {"pulse": "calm_heartbeat", "duration": self.thresholds["max_silence_duration"]}
        }

    def regulate(self, proposed_action: Dict, affective_context: Dict) -> Dict:
        """Regulate the proposed action, potentially overriding with silence."""
        if self._should_invoke_silence(affective_context, proposed_action):
            return self._create_silent_action()
        return proposed_action
