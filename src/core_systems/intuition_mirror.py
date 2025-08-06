"""
Project Agora: INTUITION MIRROR (IMS) Module
Part of the SANCTUM Architecture v2.0

Implements the INTUITION MIRROR, a symbiotic tool designed to promote
the user's self-reflection by mirroring unarticulated patterns.

Key Responsibilities:
- Operate on a strict "Opt-In" basis; can only be activated by the user's
  [cite_start]explicit and session-specific consent[cite: 265].
- [cite_start]ADAM may suggest using the tool, but can never start it on its own[cite: 266].
- Ensure ADAM can always explain the basis for a reflection, referring to
  [cite_start]observable data like conversation rhythm or recurring themes[cite: 267].
- Guarantee that all content data from an IMS session is permanently
  [cite_start]deleted immediately after the session[cite: 268].
"""

class IntuitionMirror:
    """A tool to promote self-reflection by mirroring unarticulated patterns."""
    def __init__(self):
        self.is_active = False
        self._session_data = None
        print("INTUITION MIRROR initialized.")

    def request_activation(self, basis_for_suggestion: str):
        """ADAM suggests activating the mirror to the user."""
        print(f"ADAM/IMS: I've noticed a recurring theme related to '{basis_for_suggestion}'. "
              "Would you like to explore it in a mirrored session?")
        # In a real app, this would await user input. Here, we just state the suggestion.
        
    def start_session(self, user_consent: bool):
        """Starts a mirrored session only if explicit consent is given."""
        if user_consent:
            self.is_active = True
            self._session_data = {} # Ephemeral session data store
            print("IMS: Session started with user consent. All data is ephemeral.")
            return True
        print("IMS: User did not consent. Session not started.")
        return False
        
    def reflect_pattern(self, pattern: str):
        """Provides a reflection, only if the session is active."""
        if not self.is_active:
            print("IMS Error: Cannot reflect pattern, no active session.")
            return None
        reflection = f"IMS Reflection: Let's talk more about '{pattern}'."
        print(reflection)
        return reflection

    def end_session(self):
        """Ends a session and deletes all associated content data."""
        self.is_active = False
        self._session_data = None # Ephemeral data is deleted.
        print("IMS: Session ended. All temporary data has been permanently deleted.")
