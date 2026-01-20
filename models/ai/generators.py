import random
from models.ai.base_ai import BaseAIModel

class RandomMelodyGenerator(BaseAIModel):
    def __init__(self, scale=None):
        super().__init__(name="RandomMelodyGenerator")
        # Default C Major scale frequencies (approximate)
        self.scale = scale if scale else [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

    def generate_sequence(self, num_notes=8, min_duration=0.5, max_duration=1.0, **kwargs):
        """Generates a random sequence of (frequency, duration)."""
        sequence = []
        for _ in range(num_notes):
            freq = random.choice(self.scale)
            duration = random.uniform(min_duration, max_duration)
            sequence.append({'frequency': freq, 'duration': duration})
        return sequence
