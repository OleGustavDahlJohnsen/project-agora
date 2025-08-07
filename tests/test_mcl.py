"""
Project Agora: Unit Tests for the Multimodal Core Layer (MCL)
"""
import pytest
from src.sensors.multimodal_fusion_layer import MultimodalFusionLayer
from src.agents.unified_context_buffer import UnifiedContextBuffer

def test_mfl_fuses_multiple_modalities():
    """Tests that the MultimodalFusionLayer can fuse different inputs."""
    mfl = MultimodalFusionLayer()
    
    inputs = [
        {"modality": "text", "data": "User seems concerned."},
        {"modality": "audio", "data": {"tone": "hesitant", "volume_db": -20}},
        {"modality": "biometric", "data": {"hrv_sdnn": 45}}
    ]
    
    fused_data = mfl.fuse_inputs(inputs)
    
    assert "text" in fused_data["modalities"]
    assert "audio" in fused_data["modalities"]
    assert "biometric" in fused_data["modalities"]
    assert fused_data["modalities"]["text"] == "User seems concerned."

def test_ucb_stores_and_retrieves_context():
    """Tests that the UnifiedContextBuffer functions as a FIFO buffer."""
    ucb = UnifiedContextBuffer(buffer_size=2)
    
    perception1 = {"modalities": {"text": "Hello"}}
    perception2 = {"modalities": {"text": "How are you?"}}
    perception3 = {"modalities": {"text": "Goodbye"}}
    
    ucb.add_perception(perception1)
    assert ucb.get_latest_context() == perception1
    
    ucb.add_perception(perception2)
    assert ucb.get_latest_context() == perception2
    
    # This should push perception1 out of the buffer
    ucb.add_perception(perception3)
    assert ucb.get_latest_context() == perception3
    assert len(ucb.buffer) == 2

"""
Project Agora: Unit Tests for the Multimodal Core Layer (MCL)
"""
# ... (other imports)
from src.sensors.modal_confidence_scaler import ModalConfidenceScaler

# ... (existing tests for MFL and UCB are unchanged)

def test_modal_confidence_scaler_assigns_scores():
    """Tests that the scaler correctly adds confidence scores to modalities."""
    scaler = ModalConfidenceScaler()
    
    fused_perception = {
        "modalities": {
            "text": "This is a direct command.",
            "biometric": {"hrv_sdnn": 50}
        }
    }
    
    scaled_perception = scaler.scale(fused_perception)
    
    text_modality = scaled_perception["modalities"]["text"]
    biometric_modality = scaled_perception["modalities"]["biometric"]
    
    assert "data" in text_modality
    assert "confidence_score" in text_modality
    assert text_modality["confidence_score"] == 0.95
    
    assert "data" in biometric_modality
    assert "confidence_score" in biometric_modality
    assert biometric_modality["confidence_score"] == 0.65
