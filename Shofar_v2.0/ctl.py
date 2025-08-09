# -*- coding: utf-8 -*-
"""
Provides the software interface to the hardware-accelerated CTL
(Causal Traceability Ledger).
"""
import hashlib
import json
from datetime import datetime, timezone
from typing import Any, Dict

class CausalTraceabilityLedger:
    """
    Provides a software interface to the hardware-accelerated causal log.
    """
    def __init__(self):
        """
        Initializes the connection to the CTL hardware.
        """
        self._log_chain = []
        print("CTL (Causal Traceability Ledger) Interface Initialized.")

    def log_event(self, actor: str, event: str, context: Dict[str, Any], outcome: str) -> str:
        """
        Logs an event and its context to the immutable ledger.

        Args:
            actor (str): The module or entity performing the action.
            event (str): The name of the event/action being logged.
            context (Dict): Supporting data about the event.
            outcome (str): The result of the event.

        Returns:
            str: The SHA-256 hash of the new log entry, serving as its ID.
        """
        timestamp = datetime.now(timezone.utc).isoformat()
        
        # In a real system, previous_hash would come from the last hardware entry.
        previous_hash = self._log_chain[-1]['hash'] if self._log_chain else '0' * 64
        
        entry = {
            "timestamp": timestamp,
            "previous_hash": previous_hash,
            "actor": actor,
            "event": event,
            "context": context,
            "outcome": outcome,
        }
        
        # The hashing would be offloaded to a crypto accelerator.
        entry_bytes = json.dumps(entry, sort_keys=True).encode('utf-8')
        entry['hash'] = hashlib.sha256(entry_bytes).hexdigest()
        
        self._log_chain.append(entry)
        print(f"CTL: Event '{event}' by '{actor}' logged with hash {entry['hash'][:10]}...")
        return entry['hash']
