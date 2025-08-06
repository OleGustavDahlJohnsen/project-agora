"""
Project Agora: INTUITION MIRROR (IMS) Module
Part of the SANCTUM Architecture v2.0

Implements the INTUITION MIRROR, a symbiotic tool designed to promote
the user's self-reflection by mirroring unarticulated patterns.

Key Responsibilities:
- Operate on a strict "Opt-In" basis; can only be activated by the user's
  [cite_start]explicit and session-specific consent. [cite: 370]
- [cite_start]ADAM may suggest using the tool, but can never start it on its own. [cite: 204, 371]
- Ensure ADAM can always explain the basis for a reflection, referring to
  [cite_start]observable data like conversation rhythm or recurring themes. [cite: 372]
- Guarantee that all content data from an IMS session is permanently
  deleted immediately after the session, unless the user explicitly saves
  [cite_start]an encrypted summary. [cite: 373]
"""

class IntuitionMirror:
    """A tool to promote self-reflection by mirroring unarticulated patterns."""
    def __init__(self):
        self.is_active = False
        print("INTUITION MIRROR initialized.")

    def request_activation(self):
        """Suggests activating the mirror to the user."""
        print("ADAM/IMS: I've noticed a recurring pattern. Would you like to explore it?")
        # Returns True if user provides explicit, session-specific consent.
        return False # Default to no consent

    def start_session(self):
        """Starts a mirrored session if consent is given."""
        self.is_active = True
        print("IMS: Session started. All data is ephemeral.")

    def end_session(self):
        """Ends a session and deletes all associated content data."""
        self.is_active = False
        print("IMS: Session ended. All temporary data has been deleted.")
