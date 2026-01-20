from agents.composer import ComposerAgent
from benchmarks.suite import BenchmarkSuite
from benchmarks.metrics.audio_quality import AudioQualityEvaluator
from benchmarks.critics.llm_critic import LLMCritic

def main():
    # Setup Agent
    agent = ComposerAgent()

    # Setup Benchmark Suite
    suite = BenchmarkSuite(agent)
    suite.add_evaluator(AudioQualityEvaluator())
    suite.add_evaluator(LLMCritic())

    # Run
    print("Starting Benchmark Run...")
    results = suite.run(num_trials=2, output_filename="bench_test.wav", num_notes=3)

    # Report
    print("\n--- Benchmark Results ---")
    for res in results:
        print(f"Trial {res['trial']}:")
        if 'error' in res:
            print(f"  Error: {res['error']}")
        else:
            for k, v in res['metrics'].items():
                print(f"  {k}: {v}")

if __name__ == "__main__":
    main()
