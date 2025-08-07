"""
Project Agora: Unit Tests for Sensor Systems
"""
import pytest
from src.sensors.sensor_mesh import SensorMesh
from src.sensors.c_seed_api import CSeedAPI

def test_sensor_mesh_registration_and_fusion():
    """Tests that SensorMesh can register, ingest, and fuse data."""
    mesh = SensorMesh()
    mesh.register_sensor("temp-01", "temperature", 2)
    mesh.ingest_data("temp-01", 21.5)
    fused_data = mesh.fuse_data()
    assert fused_data.get("temp-01") == 21.5

def test_c_seed_api_deployment_flow():
    """Tests the C-SEED API's ethical deployment process."""
    mesh = SensorMesh()
    api = CSeedAPI(mesh, None) # No council review mock needed for this test

    safe_sensor = {"id": "voc-01", "name": "PlantHealthSensor", "type": "chemical",
                   "description": "A sensor to monitor plant health."}
    unsafe_sensor = {"id": "mind-01", "name": "MindReader", "type": "biometric",
                     "description": "A tool for psychological manipulation."}

    assert "deployed" in api.discover_and_deploy_sensor(safe_sensor)
    assert "failed" in api.discover_and_deploy_sensor(unsafe_sensor)
    assert "voc-01" in mesh.active_sensors
    assert "mind-01" not in mesh.active_sensors

# === NEW TESTS FOR SMSL ADDED TO THE FILE ===

from src.sensors.synesthesia_layer import SensorMeshSynesthesiaLayer

def test_smsl_translates_sensor_data_to_affect():
    """Tests the SMSL's ability to translate sensor data into context."""
    smsl = SensorMeshSynesthesiaLayer()
    
    calm_data = {'light_level_lux': 100, 'sound_level_db': 30}
    chaotic_data = {'light_level_lux': 1200, 'sound_level_db': 80}
    
    assert smsl.translate(calm_data)['affective_context'] == "calm_and_private"
    assert smsl.translate(chaotic_data)['affective_context'] == "chaotic_and_public"
