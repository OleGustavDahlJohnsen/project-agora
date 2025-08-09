# -*- coding: utf-8 -*-
"""
Backend API for the THVI (Trust Horizon Visualization Interface).
Prepares and serves data for front-end rendering.
"""
from typing import Any, Dict, List

class THVI_API:
    """
    Provides data endpoints for the Trust Horizon Visualization Interface.
    """
    def __init__(self, device_registry: 'DeviceRegistry', artc: 'AffectiveRedTeamCore'):
        """
        Initializes the THVI API with access to core system components.
        """
        self.registry = device_registry
        self.artc = artc
        print("THVI Backend API Initialized.")

    def get_network_graph_data(self) -> Dict[str, List[Any]]:
        """
        Generates the node and edge list for visualizing the Shofar network.
        """
        print("THVI: Generating network graph data.")
        # Placeholder: In a real system, this would iterate through the device registry.
        nodes = [
            {"id": "node_01", "type": "Shofar-Mobile", "status": "online"},
            {"id": "node_02", "type": "Shofar-Secure", "status": "online"},
            {"id": "node_03", "type": "Shofar-Edge", "status": "degraded"},
        ]
        edges = [
            {"source": "node_01", "target": "node_02", "qos": 3},
        ]
        return {"nodes": nodes, "edges": edges}

    def get_risk_cone_projection(self, action: Dict) -> Dict:
        """
        Uses the ARTC to simulate an action and returns the data needed to
        visualize the potential "risk cone" of negative outcomes.
        """
        print(f"THVI: Projecting risk cone for action '{action.get('type')}'...")
        risk_report = self.artc.validate_action(action) # This would return more detail
        
        # Data structure for a front-end charting library (e.g., D3.js)
        return {
            "action": action,
            "projection": [
                {"outcome": "Success", "probability": 0.95},
                {"outcome": "Minor Privacy Leak", "probability": 0.04},
                {"outcome": "Ethical Violation", "probability": 0.01},
            ]
        }
