import unittest
import numpy as np
import os
from core.audio_buffer import AudioBuffer

class TestAudioBuffer(unittest.TestCase):
    def test_initialization(self):
        buf = AudioBuffer(duration=1.0, sample_rate=44100)
        self.assertEqual(len(buf), 44100)
        self.assertEqual(buf.sample_rate, 44100)
        self.assertTrue(np.all(buf.data == 0))

    def test_append(self):
        buf1 = AudioBuffer(data=[0.1, 0.2], sample_rate=100)
        buf2 = AudioBuffer(data=[0.3, 0.4], sample_rate=100)
        buf1.append(buf2)
        self.assertEqual(len(buf1), 4)
        np.testing.assert_array_equal(buf1.data, np.array([0.1, 0.2, 0.3, 0.4], dtype=np.float32))

    def test_mix(self):
        buf1 = AudioBuffer(data=[0.1, 0.1, 0.1, 0.1], sample_rate=100)
        buf2 = AudioBuffer(data=[0.2, 0.2], sample_rate=100)

        # Mix buf2 into buf1 starting at sample 1 (0.01s)
        buf1.mix(buf2, start_time=0.01)

        expected = np.array([0.1, 0.3, 0.3, 0.1], dtype=np.float32)
        np.testing.assert_almost_equal(buf1.data, expected)

    def test_save(self):
        buf = AudioBuffer(duration=0.1, sample_rate=44100)
        filename = "test_output.wav"
        buf.save(filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
