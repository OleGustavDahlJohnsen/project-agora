# -*- coding: utf-8 -*-
"""
This file will implement the SMSL (SensorMesh Synesthesia Layer). This acts 
as the high-level protocol layer that standardizes the fused data from the 
SPU into a Unified Perceptual Field (UPF). It ensures that perceptual data 
is consistent and ready for consumption by other cognitive modules.
"""
from typing import Any, Dict
from csnp_layer import CSNPLayer

class SensorMeshSynesthesiaLayer:
    """
    Standardizes fused sensor data into the Unified Perceptual Field (UPF).
    """
    def __init__(self, csnp_interface: CSNPLayer):
        """
        Initializes the SMSL.
        """
        self.csnp = csnp_interface
        print("SMSL Initialized.")

    def package_as_upf(self, fused_data: Dict) -> Dict:
        """
        Packages fused sensor data into the standard UPF format.
        """
        print("Packaging data as UPF.")
        upf_packet = {
            "version": "1.0",
            "timestamp": "mock_timestamp",
            "source_node": self.csnp.node_id,
            "perceptual_data": fused_data
        }
        return upf_packet

    def broadcast_upf(self, upf_packet: Dict):
        """
        Broadcasts the UPF packet to relevant nodes over the CSNP.
        """
        print("Broadcasting UPF to cognitive modules.")
        # QoS level 3 for Perception data
        self.csnp.send_data(target_node_id="cognitive_bus", data=upf_packet, qos_level=3)
