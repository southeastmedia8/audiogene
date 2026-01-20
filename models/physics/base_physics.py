from abc import abstractmethod
from models.base import BaseModel
from core.audio_buffer import AudioBuffer

class BasePhysicsModel(BaseModel):
    """Abstract base class for physics-based audio synthesis models."""

    def __init__(self, name="PhysicsModel", sample_rate=44100):
        super().__init__(name)
        self.sample_rate = sample_rate

    @abstractmethod
    def synthesize(self, duration, frequency, **kwargs) -> AudioBuffer:
        """Synthesizes audio for a given duration and frequency."""
        pass

    def generate(self, *args, **kwargs):
        return self.synthesize(*args, **kwargs)
