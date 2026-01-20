from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """Abstract base class for all agents."""

    def __init__(self, name="BaseAgent"):
        self.name = name

    @abstractmethod
    def run(self, *args, **kwargs):
        """Executes the agent's main task."""
        pass
