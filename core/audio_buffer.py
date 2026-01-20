import numpy as np
from scipy.io import wavfile
import os

class AudioBuffer:
    def __init__(self, sample_rate=44100, data=None, duration=None, channels=1):
        self.sample_rate = sample_rate
        self.channels = channels

        if data is not None:
            self.data = np.array(data, dtype=np.float32)
        elif duration is not None:
            num_samples = int(sample_rate * duration)
            if channels > 1:
                self.data = np.zeros((num_samples, channels), dtype=np.float32)
            else:
                self.data = np.zeros(num_samples, dtype=np.float32)
        else:
            self.data = np.array([], dtype=np.float32)

    def save(self, filepath):
        """Saves the audio buffer to a WAV file."""
        # Normalize to 16-bit PCM for broader compatibility
        # Check if empty
        if self.data.size == 0:
            print("Warning: Saving empty audio buffer.")
            return

        # Simple normalization to prevent clipping if max > 1.0
        max_val = np.max(np.abs(self.data))
        if max_val > 1.0:
            normalized_data = self.data / max_val
        else:
            normalized_data = self.data

        # Convert to 16-bit integer
        audio_int16 = (normalized_data * 32767).astype(np.int16)

        wavfile.write(filepath, self.sample_rate, audio_int16)
        print(f"Saved audio to {filepath}")

    def append(self, other_buffer):
        """Appends another AudioBuffer to this one."""
        if self.sample_rate != other_buffer.sample_rate:
            raise ValueError("Sample rates must match to append buffers.")

        if self.data.size == 0:
            self.data = other_buffer.data
        else:
            self.data = np.concatenate((self.data, other_buffer.data))

    def mix(self, other_buffer, start_time=0):
        """Mixes another buffer into this one at a specific start time."""
        if self.sample_rate != other_buffer.sample_rate:
            raise ValueError("Sample rates must match to mix buffers.")

        start_sample = int(start_time * self.sample_rate)
        end_sample = start_sample + len(other_buffer.data)

        # Extend current buffer if needed
        if end_sample > len(self.data):
            padding = np.zeros(end_sample - len(self.data), dtype=np.float32)
            self.data = np.concatenate((self.data, padding))

        self.data[start_sample:end_sample] += other_buffer.data

    def __len__(self):
        return len(self.data)

    @property
    def duration(self):
        return len(self.data) / self.sample_rate

    @classmethod
    def load(cls, filepath):
        """Loads an AudioBuffer from a WAV file."""
        sample_rate, data = wavfile.read(filepath)

        # Convert back to float32 [-1.0, 1.0]
        if data.dtype == np.int16:
            data = data.astype(np.float32) / 32767.0
        elif data.dtype == np.uint8:
            data = (data.astype(np.float32) - 128.0) / 128.0

        channels = 1 if len(data.shape) == 1 else data.shape[1]

        return cls(sample_rate=sample_rate, data=data, channels=channels)
