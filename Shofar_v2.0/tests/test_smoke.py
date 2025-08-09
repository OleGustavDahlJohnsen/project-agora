# -*- coding: utf-8 -*-
"""
Smoke test for the Shofar v2.0 package.
Verifies that all core modules can be initialized without errors.
"""
import unittest

# Import all major classes to check for import errors
from Shofar_v2.0.ctl import CausalTraceabilityLedger
from Shofar_v2.0.qos_scheduler import QoSScheduler
from Shofar_v2.0.artc import AffectiveRedTeamCore
from Shofar_v2.0.csnp_layer import CSNPLayer
# ... import other main classes as they are built

class TestSmokeInitialization(unittest.TestCase):
    """A test suite to ensure core components can be instantiated."""

    def test_can_initialize_core_modules(self):
        """
        Tests if the main service classes can be created.
        This is a basic check to catch dependency or syntax errors.
        """
        print("\n--- Running Smoke Test ---")
        
        # Mock dependencies
        mock_ctl = CausalTraceabilityLedger()
        mock_qos = QoSScheduler()
        mock_csnp = CSNPLayer(node_id="test_node", config={})
        
        # Test instantiation
        artc_instance = AffectiveRedTeamCore(ctl_interface=mock_ctl, qos_scheduler=mock_qos)
        
        # Assert that objects were created successfully
        self.assertIsNotNone(mock_ctl, "CTL should be initializable")
        self.assertIsNotNone(mock_qos, "QoS Scheduler should be initializable")
        self.assertIsNotNone(mock_csnp, "CSNP Layer should be initializable")
        self.assertIsNotNone(artc_instance, "ARTC should be initializable")
        
        print("--- Smoke Test Passed Successfully ---\n")

if __name__ == '__main__':
    unittest.main()
