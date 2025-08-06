# === NY KODE SOM SKAL LEGGES TIL NEDERST I FILEN ===

# Importer de nye klassene vi skal teste
from src.core_systems.inner_shield import InnerShield
from src.core_systems.intuition_mirror import IntuitionMirror

# --- Tests for InnerShield ---

def test_inner_shield_pattern_detection():
    """Tests that InnerShield correctly detects concerning patterns."""
    shield = InnerShield()
    nominal_data = {"text": "I feel great today, the project is moving forward."}
    concerning_data = {"text": "I feel hopeless about this situation."}

    assert shield.analyze_patterns(nominal_data)["status"] == "patterns_nominal"
    assert shield.analyze_patterns(concerning_data)["status"] == "pattern_detected"
    assert shield.analyze_patterns(concerning_data)["recommendation"] == "offer_escalation_to_healthcare"

# --- Tests for IntuitionMirror ---

def test_intuition_mirror_consent_flow():
    """Tests the full consent and session lifecycle of the IntuitionMirror."""
    mirror = IntuitionMirror()

    # 1. Initial state is inactive
    assert mirror.is_active == False

    # 2. Attempt to start without consent fails
    mirror.start_session(user_consent=False)
    assert mirror.is_active == False
    assert mirror.reflect_pattern("test") is None # Cannot reflect when inactive

    # 3. Start with consent succeeds
    mirror.start_session(user_consent=True)
    assert mirror.is_active == True
    assert mirror.reflect_pattern("test") is not None # Can reflect when active

    # 4. End session and verify it's inactive and data is gone
    mirror.end_session()
    assert mirror.is_active == False
    assert mirror._session_data is None
    assert mirror.reflect_pattern("test") is None # Cannot reflect after session ends
