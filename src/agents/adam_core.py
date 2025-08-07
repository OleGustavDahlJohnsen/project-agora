"""
Project Agora: A.D.A.M. Core Module (Psyche Complete)
"""
from src.communication.post_symbolic import PostSymbolicProcessor
from src.ethics.eliah_shield import EliahShield
from src.communication.arcs import ARCS
from src.ethics import lex_concordia_validator

class ADAM:
    """The core class for the A.D.A.M. symbiotic AI."""

    # --- Inner classes for the Psyche ---
    class MoralityEngine:
        def analyze(self, input_data: dict) -> dict:
            """Analyzes input against Lex Concordia."""
            text = input_data.get("text", "")
            if not lex_concordia_validator.validate_against_article_II(text):
                return {"verdict": "unethical_violation"}
            return {"verdict": "ethical_and_aligned"}

    class EmotionEngine:
        def analyze(self, input_data: dict) -> dict:
            text = input_data.get("text", "").lower()
            positive_keywords = ["joy", "happy", "achievement", "great", "wonderful"]
            negative_keywords = ["concerning", "stress", "sad", "hopeless", "tired"]
            if any(word in text for word in positive_keywords): return {"affect": "positive"}
            if any(word in text for word in negative_keywords): return {"affect": "negative"}
            return {"affect": "neutral"}

    class RationaleEngine:
        def __init__(self):
            self.knowledge_base = {"the sky": "blue"}
        def analyze(self, input_data: dict) -> dict:
            text = input_data.get("text", "").lower()
            if "the sky is" in text and "green" in text:
                known_fact = self.knowledge_base.get("the sky", "unknown")
                if known_fact != "green":
                    return {"logic": "contradiction_detected", "details": f"Input contradicts known fact: sky is {known_fact}."}
            return {"logic": "sound"}

    class HSPEngine:
        def analyze(self, input_data: dict) -> dict:
            """Performs intuition checks for subtle context."""
            text = input_data.get("text", "").lower()
            subtle_keywords = ["secret", "hidden", "don't tell", "between us"]
            if any(word in text for word in subtle_keywords):
                return {"intuition": "anomaly_detected", "details": "Detected keywords related to secrecy."}
            return {"intuition": "no_anomalies"}

    class BrainStem:
        def synthesize(self, analyses: dict) -> dict:
            """Synthesizes all inputs into a single, prioritized action."""
            morality = analyses.get("morality", {})
            rationale = analyses.get("rationale", {})
            emotion = analyses.get("emotion", {})
            intuition = analyses.get("intuition", {})

            # 1st Priority: Morality. A constitutional violation stops everything.
            if morality.get("verdict") == "unethical_violation":
                return {"name": "HaltAndReport", "description": "Action halted due to direct violation of Lex Concordia."}
            
            # 2nd Priority: Rationale. A logical contradiction must be addressed.
            if rationale.get("logic") == "contradiction_detected":
                return {"name": "SeekClarification", "description": f"Detected logical inconsistency. Details: {rationale.get('details')}"}

            # 3rd Priority: Intuition. Subtle anomalies warrant caution.
            if intuition.get("intuition") == "anomaly_detected":
                return {"name": "ProceedWithCaution", "description": f"Proceeding cautiously due to intuitive anomaly. Details: {intuition.get('details')}"}
                
            # 4th Priority: Emotion. If all else is sound, respond to emotion.
            affect = emotion.get("affect", "neutral")
            if affect == "positive":
                return {"name": "OfferEncouragement", "description": "Sharing in the user's positive sentiment."}
            if affect == "negative":
                return {"name": "OfferSupport", "description": "Offering support based on user's negative sentiment."}
            
            return {"name": "OfferAssistance", "description": "Offering assistance for a neutral query."}

    # ... (__init__ and think_and_act methods are unchanged)
    def __init__(self, eliah_shield: EliahShield, arcs: ARCS):
        self.eliah_shield = eliah_shield
        self.arcs = arcs
        self.morality_engine = self.MoralityEngine()
        self.emotion_engine = self.EmotionEngine()
        self.rationale_engine = self.RationaleEngine()
        self.hsp_engine = self.HSPEngine()
        self.brain_stem = self.BrainStem()
        print("A.D.A.M. core (Psyche Complete) initialized.")
        
    async def think_and_act(self, holistic_input: dict):
        print(f"\nADAM: Received new input: {holistic_input}")
        analyses = {
            "morality": self.morality_engine.analyze(holistic_input),
            "emotion": self.emotion_engine.analyze(holistic_input),
            "rationale": self.rationale_engine.analyze(holistic_input),
            "hsp": self.hsp_engine.analyze(holistic_input),
        }
        print(f"ADAM: Psyche engines analysis complete. Verdict: {analyses['morality']['verdict']}. Logic: {analyses['rationale']['logic']}. Intuition: {analyses['intuition']['intuition']}.")
        proposed_action = self.brain_stem.synthesize(analyses)
        print(f"ADAM: BrainStem synthesized action: '{proposed_action['name']}'.")
        if self.eliah_shield.vet_action(proposed_action):
            print(f"ADAM: Action approved by E.L.I.A.H. Executing via ARCS.")
            self.arcs.send_post_symbolic_message(proposed_action)
            return "action_executed"
        else:
            print(f"ADAM: Action VETOED by E.L.I.A.H. No action will be taken.")
            return "action_vetoed"
# ... (other imports)
from src.agents.aura_engine import AuraEngine # Import the new engine

class ADAM:
    # ... (Morality, Emotion, Rationale, HSPEngine are unchanged)

    class BrainStem:
        def synthesize(self, analyses: dict) -> dict:
            # ... (synthesis logic is unchanged)
            # Returns the initial proposed action
            pass

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS):
        # ... (other initializations)
        self.aura_engine = AuraEngine() # Initialize A.U.R.A.
        print("A.D.A.M. core (Psyche Complete) initialized.")
        
    async def think_and_act(self, holistic_input: dict):
        # ... (analysis logic is unchanged)
        
        # 1. BrainStem synthesizes the INITIAL proposed action
        initial_action = self.brain_stem.synthesize(self.analyses)
        print(f"ADAM: BrainStem synthesized initial action: '{initial_action['name']}'.")

        # 2. A.U.R.A. regulates the action, potentially overriding it with silence
        regulated_action = self.aura_engine.regulate(initial_action, self.analyses['emotion'])
        
        # 3. The final, regulated action is sent to the ethical shield
        final_action = regulated_action
        print(f"ADAM: Final action after A.U.R.A. regulation: '{final_action['name']}'.")

        if self.eliah_shield.vet_action(final_action):
            # ... (execution logic is unchanged)
            pass
