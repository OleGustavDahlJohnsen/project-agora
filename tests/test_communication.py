"""
Project Agora: Unit Tests for Communication Systems
"""
import pytest
from src.communication.arcs import ARCS
from src.communication.post_symbolic import PostSymbolicProcessor
from src.sensors.sensor_mesh import SensorMesh # Dependency needed for testing

def test_arcs_send():
    """Tests the ARCS send functionality."""
    arcs = ARCS()
    assert arcs.send_post_symbolic_message({"pattern": "data"}) == "transmission_successful"

def test_post_symbolic_interpretation():
    """Tests that the processor can interpret fused data from the mesh."""
    mesh = SensorMesh()
    mesh.register_sensor("hrv-01", "biometric", 4)
    mesh.ingest_data("hrv-01", {"mean_rr": 850, "sdnn": 55})
    
    processor = PostSymbolicProcessor(mesh)
    understanding = processor.interpret_holistic_input()
    
    assert understanding["semantic_intent"] == "inquiry"
    assert understanding["source_data"].get("hrv-01") is not None
