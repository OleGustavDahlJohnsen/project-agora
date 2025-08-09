# -*- coding: utf-8 -*-
"""
Provides tools for generating synthetic sensor data streams to test
the SPU and the wider cognitive pipeline.
"""
import time
import random
from typing import Dict, Any, Generator

class SyntheticSensorStream:
    """
    Generates mock data for various sensor types to simulate real-world scenarios.
    """
    def __init__(self, scenario: str = "urban_street"):
        """
        Initializes the synthetic sensor stream for a given scenario.
        """
        self.scenario = scenario
        print(f"Synthetic Sensor Stream initialized for scenario: '{self.scenario}'.")

    def _generate_lidar_packet(self) -> Dict[str, Any]:
        """Generates a single mock LiDAR data packet."""
        return {
            "sensor_type": "lidar",
            "timestamp": time.time(),
            "point_cloud": [
                {"x": random.uniform(-10, 10), "y": random.uniform(0, 20), "z": 0.5}
                for _ in range(50) # 50 random points
            ]
        }
        
    def _generate_audio_packet(self) -> Dict[str, Any]:
        """Generates a single mock audio data packet."""
        return {
            "sensor_type": "microphone_array",
            "timestamp": time.time(),
            "dominant_frequency": random.uniform(200, 800),
            "amplitude_db": -random.uniform(10, 40)
        }

    def run_simulation(self, duration_sec: int) -> Generator[Dict[str, Any], None, None]:
        """
        Runs the simulation and yields sensor data packets over time.
        """
        print(f"Running '{self.scenario}' simulation for {duration_sec} seconds...")
        start_time = time.time()
        while time.time() - start_time < duration_sec:
            yield self._generate_lidar_packet()
            yield self._generate_audio_packet()
            time.sleep(0.1) # 10 Hz data rate
        print("Simulation complete.")
