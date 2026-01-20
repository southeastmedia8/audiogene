import numpy as np
from models.physics.base_physics import BasePhysicsModel
from core.audio_buffer import AudioBuffer

class SimpleOscillator(BasePhysicsModel):
    def __init__(self, waveform='sine', sample_rate=44100):
        super().__init__(name=f"SimpleOscillator-{waveform}", sample_rate=sample_rate)
        self.waveform = waveform

    def synthesize(self, duration, frequency, amplitude=0.5, **kwargs) -> AudioBuffer:
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)

        if self.waveform == 'sine':
            data = amplitude * np.sin(2 * np.pi * frequency * t)
        elif self.waveform == 'square':
            data = amplitude * np.sign(np.sin(2 * np.pi * frequency * t))
        elif self.waveform == 'sawtooth':
            data = amplitude * (2 * (t * frequency - np.floor(t * frequency + 0.5)))
        else:
            raise ValueError(f"Unknown waveform: {self.waveform}")

        return AudioBuffer(sample_rate=self.sample_rate, data=data)
