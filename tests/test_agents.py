import unittest
import os
from agents.composer import ComposerAgent

class TestComposerAgent(unittest.TestCase):
    def test_run(self):
        agent = ComposerAgent()
        filename = "test_agent_output.wav"
        output = agent.run(output_filename=filename, num_notes=2)

        self.assertEqual(output, filename)
        self.assertTrue(os.path.exists(filename))

        # Cleanup
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    unittest.main()
