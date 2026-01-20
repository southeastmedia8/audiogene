import os
import io
import numpy as np
from scipy.io import wavfile
from huggingface_hub import InferenceClient
from models.ai.base_ai import BaseAIModel
from core.audio_buffer import AudioBuffer

class HFMusicGen(BaseAIModel):
    def __init__(self, model_id="facebook/musicgen-small", api_key_env="HF_TOKEN"):
        super().__init__(name=f"HF-{model_id}")
        self.model_id = model_id
        self.api_key = os.environ.get(api_key_env)

        if self.api_key:
            self.client = InferenceClient(token=self.api_key)
        else:
            self.client = None

    def generate_sequence(self, input_context=None, **kwargs):
        """
        Generates audio from text using HF Inference API.

        Args:
            input_context (str): The text description of the music.

        Returns:
            AudioBuffer: The generated audio.
        """
        if not self.client:
            print("Warning: No HF_TOKEN found. Returning silent buffer.")
            return AudioBuffer(duration=1.0)

        prompt = input_context if input_context else "A simple melody"

        try:
            # text_to_audio returns bytes of a wav file usually
            audio_bytes = self.client.text_to_audio(
                prompt,
                model=self.model_id
            )

            # Convert bytes to AudioBuffer
            # audio_bytes is a raw bytes object containing the WAV file
            # We need to read it into numpy

            # Use io.BytesIO to make it file-like
            import io
            with io.BytesIO(audio_bytes) as f:
                sample_rate, data = wavfile.read(f)

            # Convert to float32 normalized
            if data.dtype == np.int16:
                data = data.astype(np.float32) / 32767.0
            elif data.dtype == np.int32:
                 data = data.astype(np.float32) / 2147483648.0
            elif data.dtype == np.uint8:
                data = (data.astype(np.float32) - 128.0) / 128.0

            channels = 1 if len(data.shape) == 1 else data.shape[1]

            return AudioBuffer(sample_rate=sample_rate, data=data, channels=channels)

        except Exception as e:
            print(f"HF API Error: {e}")
            return AudioBuffer(duration=1.0)
