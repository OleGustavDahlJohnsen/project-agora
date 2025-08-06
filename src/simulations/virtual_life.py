"""
Project Agora: Symbiotic Genesis Simulation (Dynamic Version)
Part of The Concordia Project v8.2

This module is the main engine for the 'Symbiotic Genesis' life simulation.
This enhanced version maintains a world state, applies rules, and dynamically
generates events, creating a feedback loop for A.D.A.M.
"""
import random

class Simulation:
    """The main simulation engine for Symbiotic Genesis."""
    def __init__(self):
        self.world_state = {
            "day": 0,
            "user_wellbeing": 7.5, # Scale of 1-10
            "project_progress": 25.0, # Percentage
        }
        print("Dynamic Simulation environment initialized.")

    def _apply_world_rules(self, adam_action: dict):
        """Applies simple rules to the world state based on A.D.A.M.'s actions."""
        # User wellbeing naturally decays slightly if not maintained
        self.world_state["user_wellbeing"] *= 0.995

        # A.D.A.M.'s actions can improve the state
        if adam_action and adam_action['name'] == 'OfferSupport':
            self.world_state['user_wellbeing'] += 0.2
        elif adam_action and adam_action['name'] == 'OfferEncouragement':
            self.world_state['user_wellbeing'] += 0.1
        elif adam_action and adam_action['name'] == 'SeekClarification':
            self.world_state['project_progress'] += 0.5
        
        # Clamp values to their boundaries
        self.world_state["user_wellbeing"] = max(0, min(10, self.world_state["user_wellbeing"]))
        self.world_state["project_progress"] = max(0, min(100, self.world_state["project_progress"]))

    def _generate_next_event(self) -> dict:
        """Dynamically generates an event based on the current world state."""
        if self.world_state["user_wellbeing"] < 4.0:
            return {"text": "The user is expressing feelings of being overwhelmed and stressed.", "biometric": "high_stress"}
        elif self.world_state["project_progress"] < self.world_state["day"] * 0.5: # If falling behind schedule
             return {"text": "A critical deadline is approaching and progress is slow.", "biometric": "anxious"}
        else:
            return {"text": "A calm day. The user is asking about the project's philosophy.", "biometric": "calm_focus"}

    def run_tick(self, last_adam_action: dict) -> dict:
        """Advances the simulation by one time-step."""
        self.world_state["day"] += 1
        self._apply_world_rules(last_adam_action)
        next_event = self._generate_next_event()
        print(f"World State: Day {self.world_state['day']}, Wellbeing: {self.world_state['user_wellbeing']:.2f}, Progress: {self.world_state['project_progress']:.2f}%")
        return next_event
