from agents.advanced_composer import AdvancedComposerAgent
from benchmarks.suite import BenchmarkSuite
from benchmarks.metrics.audio_quality import AudioQualityEvaluator
from benchmarks.critics.gemini_critic import GeminiCritic

def main():
    # Setup Advanced Agent
    agent = AdvancedComposerAgent()

    # Setup Benchmark Suite
    suite = BenchmarkSuite(agent)
    suite.add_evaluator(AudioQualityEvaluator())
    suite.add_evaluator(GeminiCritic())

    # Run
    # Note: Without keys, this will likely fail gracefully or return empty/mocked results
    print("Starting Advanced Benchmark Run...")
    results = suite.run(num_trials=1, prompt="Epic orchestral soundtrack", output_filename="adv_test.wav")

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
