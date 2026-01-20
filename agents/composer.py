from agents.base_agent import BaseAgent
from models.physics.oscillators import SimpleOscillator
from models.ai.generators import RandomMelodyGenerator
from core.audio_buffer import AudioBuffer

class ComposerAgent(BaseAgent):
    def __init__(self, name="Composer"):
        super().__init__(name)
        self.ai_model = RandomMelodyGenerator()
        self.physics_model = SimpleOscillator(waveform='sine')
        self.last_sequence = None

    def run(self, output_filename="output.wav", num_notes=5):
        print(f"[{self.name}] Generating melody with {num_notes} notes...")
        sequence = self.ai_model.generate(num_notes=num_notes)
        self.last_sequence = sequence

        # Calculate total duration slightly roughly to init buffer
        total_duration = sum(note['duration'] for note in sequence)
        # Add a little tail
        final_buffer = AudioBuffer(duration=total_duration + 1.0)

        current_time = 0.0
        for note in sequence:
            freq = note['frequency']
            dur = note['duration']
            print(f"  - Note: {freq:.2f}Hz for {dur:.2f}s")

            # Synthesize note
            note_buffer = self.physics_model.synthesize(duration=dur, frequency=freq)

            # Mix into main buffer
            # Note: The mix method in AudioBuffer mixes *at* a start time.
            # If we want a sequence, we usually append or mix at offset.
            # Here we mix at offset.
            final_buffer.mix(note_buffer, start_time=current_time)

            current_time += dur

        print(f"[{self.name}] Saving to {output_filename}")
        final_buffer.save(output_filename)
        return output_filename
