from abc import abstractmethod
from models.base import BaseModel

class BaseAIModel(BaseModel):
    """Abstract base class for AI models."""

    def __init__(self, name="AIModel"):
        super().__init__(name)

    @abstractmethod
    def generate_sequence(self, input_context=None, **kwargs):
        """Generates a sequence of musical events or data."""
        pass

    def generate(self, *args, **kwargs):
        return self.generate_sequence(*args, **kwargs)
