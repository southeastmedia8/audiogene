from abc import ABC, abstractmethod

class BaseEvaluator(ABC):
    """Abstract base class for all benchmarking evaluators."""

    def __init__(self, name="BaseEvaluator"):
        self.name = name

    @abstractmethod
    def evaluate(self, audio_buffer, metadata=None):
        """
        Evaluates the given audio buffer and metadata.

        Args:
            audio_buffer (AudioBuffer): The audio data to evaluate.
            metadata (dict): Optional context (e.g., prompt, MIDI sequence).

        Returns:
            dict: Dictionary of metric names and values.
        """
        pass
