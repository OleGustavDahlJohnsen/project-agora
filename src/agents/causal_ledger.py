"""
Project Agora: Causal Traceability Ledger (CTL)
Part of The Concordia Project v8.2 (B.O.D.Y. Architecture)

This module provides a secure, immutable ledger for recording the full
causal chain of A.D.A.M.'s decisions.
"""
import json
from datetime import datetime
from typing import Dict, List

class CausalLedger:
    """
    An append-only log that records the 'why' behind every decision.
    For the MVP, this is an in-memory list. In production, this would be a
    cryptographically-chained, immutable database (like a blockchain).
    """
    def __init__(self):
        self.ledger: List[Dict] = []
        print("Causal Traceability Ledger (CTL) initialized.")

    def record_decision(self, decision_package: Dict):
        """
        Records a full decision package to the ledger.
        """
        entry = {
            "timestamp_utc": datetime.utcnow().isoformat(),
            "decision_package": decision_package
        }
        self.ledger.append(entry)
        print(f"CTL: Decision recorded. Ledger now contains {len(self.ledger)} entries.")
