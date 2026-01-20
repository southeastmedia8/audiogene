from core.audio_buffer import AudioBuffer

class BenchmarkSuite:
    def __init__(self, agent):
        self.agent = agent
        self.evaluators = []

    def add_evaluator(self, evaluator):
        self.evaluators.append(evaluator)

    def run(self, num_trials=1, **agent_kwargs):
        print(f"Running Benchmark Suite on agent: {self.agent.name}")
        results = []

        for i in range(num_trials):
            print(f"  Trial {i+1}/{num_trials}...")

            output_file = self.agent.run(**agent_kwargs)

            # Load audio back for analysis
            try:
                audio = AudioBuffer.load(output_file)
            except Exception as e:
                print(f"    Failed to load audio: {e}")
                results.append({"trial": i, "error": str(e)})
                continue

            trial_result = {
                "trial": i,
                "output_file": output_file,
                "metrics": {}
            }

            # Extract metadata if agent has it
            metadata = {}
            if hasattr(self.agent, 'last_sequence'):
                metadata['sequence'] = self.agent.last_sequence

            for evaluator in self.evaluators:
                scores = evaluator.evaluate(audio, metadata=metadata)
                trial_result["metrics"].update(scores)

            results.append(trial_result)

        return results
