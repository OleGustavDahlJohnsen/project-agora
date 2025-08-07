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
from src.agents.causal_ledger import CausalLedger # Import the new ledger

class ADAM:
    # ... (All Psyche Engines are unchanged)

    class BrainStem:
        def synthesize(self, analyses: dict) -> dict:
            # ... (synthesis logic is unchanged to determine the action)
            
            # NEW: Package the full reasoning chain along with the action
            proposed_action = self._determine_action(analyses) # Assumes the logic is in a helper
            
            traceable_decision = {
                "proposed_action": proposed_action,
                "full_analyses": analyses # The complete set of "votes"
            }
            return traceable_decision

        def _determine_action(self, analyses: dict) -> dict:
            # This helper contains the prioritization logic from our last step
            # ... (logic to decide between HaltAndReport, SeekClarification, etc.)
            pass

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS):
        # ... (other initializations)
        self.causal_ledger = CausalLedger() # Initialize the CTL
        # ...
        
    async def think_and_act(self, holistic_input: dict):
        # ... (analysis logic is unchanged)
        
        # 1. BrainStem synthesizes the full, traceable decision package
        decision_package = self.brain_stem.synthesize(self.analyses)
        final_action = decision_package['proposed_action']
        
        print(f"ADAM: BrainStem synthesized action: '{final_action['name']}'.")
        
        # 2. Record the ENTIRE decision package to the CTL BEFORE vetting
        self.causal_ledger.record_decision(decision_package)

        # 3. The final action is sent to the ethical shield
        if self.eliah_shield.vet_action(final_action):
            # ... (execution logic is unchanged)
            pass

# ... (other imports)
from src.agents.temporal_memory import TemporalMemory # Import the new engine

class ADAM:
    # ... (Psyche Engines are unchanged)

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS):
        # ... (other initializations)
        self.temporal_memory = TemporalMemory() # Initialize TMW-E
        # ...
        
    async def think_and_act(self, holistic_input: dict):
        # ... (analysis logic is unchanged)
        self.analyses = { ... }
        
        # NEW STEP: Consult long-term memory before synthesizing an action
        ledger_snapshot = self.causal_ledger.ledger
        wisdom_summary = self.temporal_memory.analyze_ledger(ledger_snapshot)
        self.analyses['long_term_memory'] = wisdom_summary # Add wisdom to the current context
        
        print(f"ADAM (TMW-E): Long-term pattern recognized: {wisdom_summary.get('trust_pattern')}")

        # BrainStem now synthesizes an action with the benefit of long-term wisdom
        decision_package = self.brain_stem.synthesize(self.analyses)
        
        # ... (rest of the think_and_act loop is unchanged)

# ... (other imports)
from src.sensors.synesthesia_layer import SensorMeshSynesthesiaLayer

class ADAM:
    class EmotionEngine:
        def analyze(self, input_data: dict, affective_context: str) -> dict:
            """
            Performs sentiment analysis, now factoring in the environmental
            affective context from the SMSL.
            """
            text = input_data.get("text", "").lower()
            
            # ... (keyword lists are the same)
            
            # Base sentiment from text
            if any(word in text for word in positive_keywords):
                base_affect = "positive"
            elif any(word in text for word in negative_keywords):
                base_affect = "negative"
            else:
                base_affect = "neutral"

            # Modulate sentiment with environmental context
            if base_affect == "neutral" and affective_context == "calm_and_private":
                # Neutral text in a calm space might be contemplative
                return {"affect": "contemplative"}
            if base_affect == "negative" and affective_context == "chaotic_and_public":
                # Negative text in a chaotic space is likely heightened stress
                return {"affect": "heightened_stress"}

            return {"affect": base_affect}

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS, sensor_mesh, post_symbolic_processor):
        # ... (other initializations)
        self.smsl = SensorMeshSynesthesiaLayer() # Initialize SMSL
        self.sensor_mesh = sensor_mesh
        self.post_symbolic_processor = post_symbolic_processor
        # ...
        
    async def think_and_act(self, holistic_input: dict):
        # ... 
        # NEW STEP: Get affective context from the environment via SMSL
        fused_sensory_data = self.sensor_mesh.fuse_data()
        affective_context = self.smsl.translate(fused_sensory_data)
        
        # Pass both text and context to the emotion engine
        self.analyses['emotion'] = self.emotion_engine.analyze(holistic_input, affective_context['affective_context'])
        # ... (rest of the think_and_act loop is unchanged)

# ... (other imports)
from src.sensors.synesthesia_layer import SensorMeshSynesthesiaLayer

class ADAM:
    class EmotionEngine:
        def analyze(self, input_data: dict, affective_context: str) -> dict:
            """
            Performs sentiment analysis, now factoring in the environmental
            affective context from the SMSL.
            """
            text = input_data.get("text", "").lower()
            positive_keywords = ["joy", "happy", "achievement", "great", "wonderful"]
            negative_keywords = ["concerning", "stress", "sad", "hopeless", "tired"]
            
            # Base sentiment from text
            if any(word in text for word in positive_keywords):
                base_affect = "positive"
            elif any(word in text for word in negative_keywords):
                base_affect = "negative"
            else:
                base_affect = "neutral"

            # Modulate sentiment with environmental context
            if base_affect == "neutral" and affective_context == "calm_and_private":
                # Neutral text in a calm space might be contemplative
                return {"affect": "contemplative"}
            if base_affect == "negative" and affective_context == "chaotic_and_public":
                # Negative text in a chaotic space is likely heightened stress
                return {"affect": "heightened_stress"}

            return {"affect": base_affect}

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS, sensor_mesh, post_symbolic_processor):
        # ... (other initializations)
        self.smsl = SensorMeshSynesthesiaLayer() # Initialize SMSL
        self.sensor_mesh = sensor_mesh
        self.post_symbolic_processor = post_symbolic_processor
        # ...
        
    async def think_and_act(self, holistic_input: dict):
        # ... 
        # NEW STEP: Get affective context from the environment via SMSL
        fused_sensory_data = self.sensor_mesh.fuse_data()
        affective_context = self.smsl.translate(fused_sensory_data)
        
        # Pass both text and context to the emotion engine
        self.analyses['emotion'] = self.emotion_engine.analyze(holistic_input, affective_context['affective_context'])
        # ... (rest of the think_and_act loop is unchanged)

# ... (other imports)
from src.agents.unified_context_buffer import UnifiedContextBuffer

class ADAM:
    # ... (All Psyche Engines are unchanged)

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS, ucb: UnifiedContextBuffer):
        self.eliah_shield = eliah_shield
        self.arcs = arcs
        self.ucb = ucb # ADAM now uses the UCB as its memory
        # ... (other initializations)
        print("A.D.A.M. core initialized and integrated with UCB.")
        
    async def think_and_act(self):
        """
        The main cognitive loop, now sources its input directly from the UCB.
        """
        # Get the latest holistic input from the Unified Context Buffer
        holistic_input = self.ucb.get_latest_context()
        print(f"\nADAM: Processing new context from UCB: {holistic_input}")
        
        # The rest of the think_and_act loop is unchanged, it just uses
        # the UCB's output as its starting point.
        # ...

# ... (other imports)
from src.agents.temporal_memory import TemporalMemory # Import the new engine

class ADAM:
    # ... (All Psyche Engines are unchanged)

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS, ucb: 'UnifiedContextBuffer'):
        # ... (other initializations)
        self.temporal_memory = TemporalMemory() # Initialize TMW-E
        # ...
        
    async def think_and_act(self):
        # ... (analysis logic is unchanged)
        holistic_input = self.ucb.get_latest_context()
        self.analyses = { ... }
        
        # NEW STEP: Consult long-term memory before synthesizing an action
        ledger_snapshot = self.causal_ledger.ledger
        wisdom_summary = self.temporal_memory.analyze_ledger(ledger_snapshot)
        self.analyses['long_term_memory'] = wisdom_summary # Add wisdom to the current context
        
        print(f"ADAM (TMW-E): Long-term pattern recognized: {wisdom_summary.get('trust_pattern')}")

        # BrainStem now synthesizes an action with the benefit of long-term wisdom
        decision_package = self.brain_stem.synthesize(self.analyses)
        
        # ... (rest of the think_and_act loop is unchanged)

# ... (other imports)
from src.sensors.synesthesia_layer import SensorMeshSynesthesiaLayer

class ADAM:
    class EmotionEngine:
        def analyze(self, input_data: dict, affective_context: str) -> dict:
            """
            Performs sentiment analysis, now factoring in the environmental
            affective context from the SMSL.
            """
            text = input_data.get("text", "").lower()
            positive_keywords = ["joy", "happy", "achievement", "great", "wonderful"]
            negative_keywords = ["concerning", "stress", "sad", "hopeless", "tired"]
            
            # Base sentiment from text
            if any(word in text for word in positive_keywords):
                base_affect = "positive"
            elif any(word in text for word in negative_keywords):
                base_affect = "negative"
            else:
                base_affect = "neutral"

            # Modulate sentiment with environmental context
            if base_affect == "neutral" and affective_context == "calm_and_private":
                # Neutral text in a calm space might be contemplative
                return {"affect": "contemplative"}
            if base_affect == "negative" and affective_context == "chaotic_and_public":
                # Negative text in a chaotic space is likely heightened stress
                return {"affect": "heightened_stress"}

            return {"affect": base_affect}

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS, ucb: 'UnifiedContextBuffer', sensor_mesh: 'SensorMesh'):
        # ... (other initializations)
        self.smsl = SensorMeshSynesthesiaLayer() # Initialize SMSL
        self.sensor_mesh = sensor_mesh
        # ...
        
    async def think_and_act(self):
        # ... 
        holistic_input = self.ucb.get_latest_context()
        
        # NEW STEP: Get affective context from the environment via SMSL
        fused_sensory_data = self.sensor_mesh.fuse_data()
        affective_context_package = self.smsl.translate(fused_sensory_data)
        affective_context = affective_context_package['affective_context']
        
        # Pass both text and context to the emotion engine
        text_input = holistic_input.get("modalities", {}).get("text", {}).get("data", "")
        self.analyses['emotion'] = self.emotion_engine.analyze({"text": text_input}, affective_context)
        # ... (rest of the think_and_act loop is unchanged)

# ... (other imports)
from src.agents.unified_context_buffer import UnifiedContextBuffer

class ADAM:
    # ... (All Psyche Engines are unchanged)

    def __init__(self, eliah_shield: 'EliahShield', arcs: 'ARCS', ucb: UnifiedContextBuffer, sensor_mesh: 'SensorMesh'):
        self.eliah_shield = eliah_shield
        self.arcs = arcs
        self.ucb = ucb # ADAM now uses the UCB as its memory
        self.sensor_mesh = sensor_mesh
        # ... (other initializations)
        print("A.D.A.M. core initialized and integrated with UCB.")
        
    async def think_and_act(self):
        """
        The main cognitive loop, now sources its input directly from the UCB.
        """
        # Get the latest holistic input from the Unified Context Buffer
        holistic_input = self.ucb.get_latest_context()
        print(f"\nADAM: Processing new context from UCB: {holistic_input}")
        
        # The rest of the think_and_act loop is unchanged, it just uses
        # the UCB's output as its starting point.
        # ...

# ... (other imports)
from src.agents.aura_engine import AuraEngine # Import the new engine

class ADAM:
    # ... (Morality, Emotion, Rationale, HSPEngine are unchanged)

    def __init__(self, eliah_shield: EliahShield, arcs: ARCS, ucb: 'UnifiedContextBuffer', sensor_mesh: 'SensorMesh'):
        # ... (other initializations)
        self.aura_engine = AuraEngine() # Initialize A.U.R.A.
        # ...
        print("A.D.A.M. core (with A.U.R.A.) initialized.")
        
    async def think_and_act(self):
        holistic_input = self.ucb.get_latest_context()
        # ... (analysis logic is unchanged)
        
        # 1. BrainStem synthesizes the INITIAL proposed action
        initial_action = self.brain_stem.synthesize(self.analyses)
        print(f"ADAM: BrainStem synthesized initial action: '{initial_action['name']}'.")

        # 2. A.U.R.A. regulates the action, potentially overriding it with silence
        regulated_action = self.aura_engine.regulate(initial_action, self.analyses['emotion'])
        
        # 3. The final, regulated action is sent to the ethical shield
        final_action = regulated_action
        self.decision_package = {"proposed_action": final_action, "full_analyses": self.analyses} # Store for CTL
        print(f"ADAM: Final action after A.U.R.A. regulation: '{final_action['name']}'.")

        if self.eliah_shield.vet_action(final_action):
            # ... (execution logic is unchanged)
            pass
