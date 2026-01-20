from agents.base_agent import BaseAgent
from models.ai.hf_musicgen import HFMusicGen
from benchmarks.critics.gemini_critic import GeminiCritic
from core.audio_buffer import AudioBuffer

class AdvancedComposerAgent(BaseAgent):
    def __init__(self, name="AdvancedComposer"):
        super().__init__(name)
        self.music_model = HFMusicGen()
        self.critic = GeminiCritic()
        self.last_prompt = None

    def run(self, prompt="A calm piano melody", output_filename="advanced_output.wav", self_critique=False):
        print(f"[{self.name}] Composing: '{prompt}'")
        self.last_prompt = prompt

        # Generate Audio
        audio_buffer = self.music_model.generate_sequence(input_context=prompt)

        # Optional: Self-Critique Loop (The "Perfectionist")
        if self_critique:
            print(f"[{self.name}] Requesting self-critique...")
            # We mock metadata as the prompt since we don't have midi from AudioGen
            critique = self.critic.evaluate(audio_buffer, metadata={"sequence": prompt})
            print(f"[{self.name}] Critique: {critique.get('gemini_reason', 'No response')}")

        print(f"[{self.name}] Saving to {output_filename}")
        audio_buffer.save(output_filename)
        return output_filename
