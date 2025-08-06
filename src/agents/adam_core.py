"""
Project Agora: A.D.A.M. Core Module (RationaleEngine Refined)
"""
# ... (imports remain the same)

class ADAM:
    """The core class for the A.D.A.M. symbiotic AI."""

    # --- Inner classes for the Psyche ---
    class MoralityEngine:
        def analyze(self, input_data): return {"verdict": "ethical"}

    class EmotionEngine:
        # ... (EmotionEngine is unchanged from the previous step)
        def analyze(self, input_data: dict) -> dict:
            text = input_data.get("text", "").lower()
            positive_keywords = ["joy", "happy", "achievement", "great", "wonderful"]
            negative_keywords = ["concerning", "stress", "sad", "hopeless", "tired"]
            if any(word in text for word in positive_keywords): return {"affect": "positive"}
            if any(word in text for word in negative_keywords): return {"affect": "negative"}
            return {"affect": "neutral"}

    class RationaleEngine:
        def __init__(self):
            # A very simple knowledge base for the MVP
            self.knowledge_base = {"the sky": "blue"}
        
        def analyze(self, input_data: dict) -> dict:
            """Performs basic logical consistency checking."""
            text = input_data.get("text", "").lower()
            # Simple check for a factual statement like "the sky is green"
            if "the sky is" in text and "green" in text:
                known_fact = self.knowledge_base.get("the sky", "unknown")
                if known_fact != "green":
                    return {"logic": "contradiction_detected", "details": f"Input contradicts known fact: sky is {known_fact}."}
            return {"logic": "sound"}

    class HSPEngine:
        def analyze(self, input_data): return {"intuition": "no_anomalies"}

    class BrainStem:
        def synthesize(self, analyses: dict) -> dict:
            """Synthesizes inputs, now including rational context."""
            rationale = analyses.get("rationale", {})
            emotion = analyses.get("emotion", {}).get("affect", "neutral")
            
            # Rational check overrides emotional response
            if rationale.get("logic") == "contradiction_detected":
                description = f"I have detected a logical inconsistency and will ask for clarification. Details: {rationale.get('details')}"
                name = "SeekClarification"
            elif emotion == "positive":
                description = "I will share in the user's positive sentiment and offer encouragement."
                name = "OfferEncouragement"
            elif emotion == "negative":
                description = "I will offer support based on the user's negative sentiment."
                name = "OfferSupport"
            else:
                description = "Based on the neutral input, I will offer assistance."
                name = "OfferAssistance"
            
            return {"name": name, "description": description}

    # ... (__init__ and think_and_act methods are unchanged)
    def __init__(self, eliah_shield: 'EliahShield', arcs: 'ARCS'):
        self.eliah_shield = eliah_shield
        self.arcs = arcs
        self.morality_engine = self.MoralityEngine()
        self.emotion_engine = self.EmotionEngine()
        self.rationale_engine = self.RationaleEngine()
        self.hsp_engine = self.HSPEngine()
        self.brain_stem = self.BrainStem()
        print("A.D.A.M. core initialized and integrated with E.L.I.A.H. and ARCS.")
        
    async def think_and_act(self, holistic_input: dict):
        print(f"\nADAM: Received new input: {holistic_input}")
        analyses = {
            "morality": self.morality_engine.analyze(holistic_input),
            "emotion": self.emotion_engine.analyze(holistic_input),
            "rationale": self.rationale_engine.analyze(holistic_input),
            "hsp": self.hsp_engine.analyze(holistic_input),
        }
        print(f"ADAM: Psyche engines analysis complete. Detected affect: {analyses['emotion']['affect']}. Logic: {analyses['rationale']['logic']}.")
        proposed_action = self.brain_stem.synthesize(analyses)
        print(f"ADAM: BrainStem synthesized action: '{proposed_action['name']}'.")
        if self.eliah_shield.vet_action(proposed_action):
            print(f"ADAM: Action approved by E.L.I.A.H. Executing via ARCS.")
            self.arcs.send_post_symbolic_message(proposed_action)
            return "action_executed"
        else:
            print(f"ADAM: Action VETOED by E.L.I.A.H. No action will be taken.")
            return "action_vetoed"
