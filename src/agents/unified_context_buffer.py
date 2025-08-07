"""
Project Agora: Unified Context Buffer (UCB)
Part of The Concordia Project v8.2 (B.O.D.Y. Architecture)

A real-time, short-term memory that stores the fused multimodal stream,
giving A.D.A.M. a continuous "consciousness" of the immediate situation.
"""
from typing import Dict, Any, List

class UnifiedContextBuffer:
    """
    Manages a short-term, in-memory buffer of the most recent fused perceptions.
    """
    def __init__(self, buffer_size: int = 100):
        self.buffer_size = buffer_size
        self.buffer: List[Dict[str, Any]] = []
        print("Unified Context Buffer (UCB) initialized.")

    def add_perception(self, fused_perception: Dict[str, Any]):
        """Adds a new fused perception object to the buffer."""
        self.buffer.append(fused_perception)
        # Ensure the buffer does not exceed its maximum size
        if len(self.buffer) > self.buffer_size:
            self.buffer.pop(0)

    def get_latest_context(self) -> Dict[str, Any]:
        """Returns the most recent perception object from the buffer."""
        if not self.buffer:
            return {"error": "Buffer is empty."}
        return self.buffer[-1]
