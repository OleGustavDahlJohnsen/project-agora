# -*- coding: utf-8 -*-
"""
Implements the Quality of Service (QoS) scheduler for prioritizing tasks
and network traffic according to the Shofar v2.0 hierarchy.
"""
from enum import Enum
from typing import Any, List

class QoSLevel(Enum):
    """Defines the four non-negotiable QoS priority levels."""
    SAFETY_CRITICAL = 1  # 🥇 Highest priority
    ETHICS_CRITICAL = 2  # 🥈 Very high priority
    PERCEPTION = 3       # 🥉 High priority
    BULK_SYNC = 4        # ⚙️ Normal priority

class QoSScheduler:
    """A scheduler that manages task queues based on QoS levels."""
    def __init__(self):
        """Initializes queues for each QoS level."""
        self.queues: Dict[QoSLevel, List[Any]] = {level: [] for level in QoSLevel}
        print("QoS Scheduler initialized with 4 priority queues.")

    def add_task(self, task: Any, level: QoSLevel):
        """
        Adds a task to the appropriate priority queue.

        Args:
            task (Any): The task object to be scheduled.
            level (QoSLevel): The priority level of the task.
        """
        self.queues[level].append(task)
        print(f"Task added to queue {level.name} (Priority {level.value}).")

    def get_next_task(self) -> Any | None:
        """
        Retrieves the next task from the highest-priority non-empty queue.
        """
        for level in sorted(QoSLevel, key=lambda x: x.value):
            if self.queues[level]:
                task = self.queues[level].pop(0)
                print(f"Dispatching task from queue {level.name}.")
                return task
        
        print("No tasks in any queue.")
        return None
