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
