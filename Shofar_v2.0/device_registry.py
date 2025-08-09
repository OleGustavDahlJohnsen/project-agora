# -*- coding: utf-8 -*-
"""
Manages the registration, status, and capabilities of all nodes
in the Shofar SensorMesh network.
"""
from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class ShofarNode:
    """Represents a single registered node in the ecosystem."""
    node_id: str
    node_type: str # e.g., 'Shofar-Mobile', 'Shofar-Secure'
    capabilities: List[str]
    trust_horizon: str
    status: str = "offline"

class DeviceRegistry:
    """A secure registry for all Shofar nodes."""
    def __init__(self):
        self._nodes: Dict[str, ShofarNode] = {}
        print("Device Registry initialized.")

    def register_node(self, node_info: ShofarNode) -> bool:
        """
        Registers a new node after successful attestation.
        """
        if node_info.node_id in self._nodes:
            print(f"Error: Node {node_info.node_id} already registered.")
            return False
        
        self._nodes[node_info.node_id] = node_info
        print(f"Node {node_info.node_id} ({node_info.node_type}) registered successfully.")
        return True

    def get_node_info(self, node_id: str) -> Optional[ShofarNode]:
        """
        Retrieves information for a specific node.
        """
        return self._nodes.get(node_id)

    def update_node_status(self, node_id: str, status: str):
        """
        Updates the operational status of a node (e.g., 'online', 'degraded').
        """
        if node_id in self._nodes:
            self._nodes[node_id].status = status
            print(f"Status for node {node_id} updated to {status}.")
        else:
            print(f"Warning: Attempted to update status for unregistered node {node_id}.")
