# -*- coding: utf-8 -*-
"""
Handles CSNP client resilience, including offline journaling and graceful
degradation during network outages.
"""
import time
from typing import List, Dict, Any
# from .csnp_layer import CSNPLayer

class ResilienceManager:
    """
    Manages failover and resilience for a CSNP node.
    """
    def __init__(self, csnp_interface: 'CSNPLayer'):
        """
        Initializes the manager, linking it to the active CSNP layer.
        """
        self.csnp = csnp_interface
        self.is_offline = False
        self.offline_journal: List[Dict] = []
        self.reconnect_attempts = 0
        print("Resilience Manager Initialized.")

    def handle_connection_loss(self):
        """
        Activates failover procedures when a connection is lost.
        """
        if not self.is_offline:
            print("!!! Network connection lost. Activating failover mode. !!!")
            self.is_offline = True
            self.reconnect_attempts = 0
            self._attempt_reconnect()

    def _attempt_reconnect(self):
        """
        Attempts to reconnect to the network with exponential backoff.
        """
        backoff_time = 2 ** self.reconnect_attempts
        print(f"Attempting to reconnect in {backoff_time} seconds...")
        time.sleep(backoff_time)
        
        # Placeholder for actual reconnection logic
        # if self.csnp.reconnect():
        #     self.is_offline = False
        #     self._flush_journal()
        # else:
        #     self.reconnect_attempts += 1
        #     self._attempt_reconnect()
        pass

    def journal_data(self, data: Dict):
        """
        If offline, saves data to a local journal instead of sending.
        """
        if self.is_offline:
            print("Journaling data locally while offline.")
            self.offline_journal.append(data)
        else:
            # This should ideally not be called if not offline, but as a safeguard.
            self.csnp.send_data("default_target", data)

    def _flush_journal(self):
        """
        Sends all journaled data once the connection is re-established.
        """
        print(f"Connection re-established. Flushing {len(self.offline_journal)} journaled items.")
        for item in self.offline_journal:
            self.csnp.send_data("default_target", item)
        self.offline_journal.clear()
