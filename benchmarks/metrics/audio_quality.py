import numpy as np
from benchmarks.base_evaluator import BaseEvaluator

class AudioQualityEvaluator(BaseEvaluator):
    def __init__(self):
        super().__init__(name="AudioQuality")

    def evaluate(self, audio_buffer, metadata=None):
        data = audio_buffer.data
        if len(data) == 0:
            return {"rms": 0, "peak": 0, "clipping_ratio": 0, "is_silent": True}

        # RMS (Root Mean Square) - Measure of average loudness
        rms = np.sqrt(np.mean(data**2))

        # Peak Amplitude
        peak = np.max(np.abs(data))

        # Clipping Ratio (samples at max value, assuming float 1.0 or int bounds)
        # Since we use float32 [-1, 1], we check for >= 1.0 (with slight tolerance)
        clipping_threshold = 0.999
        clipping_count = np.sum(np.abs(data) >= clipping_threshold)
        clipping_ratio = clipping_count / len(data)

        # Dynamic Range (rough estimate: Peak / RMS in dB)
        if rms > 0:
            dynamic_range = 20 * np.log10(peak / rms)
        else:
            dynamic_range = 0

        return {
            "rms": float(rms),
            "peak": float(peak),
            "clipping_ratio": float(clipping_ratio),
            "dynamic_range_db": float(dynamic_range),
            "is_silent": bool(peak < 1e-5)
        }
