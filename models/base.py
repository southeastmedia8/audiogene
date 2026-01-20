from abc import ABC, abstractmethod

class BaseModel(ABC):
    """Abstract base class for all models in the ecosystem."""

    def __init__(self, name="BaseModel"):
        self.name = name

    @abstractmethod
    def generate(self, *args, **kwargs):
        """Generates output based on the model's logic."""
        pass
