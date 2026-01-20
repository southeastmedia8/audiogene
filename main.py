from agents.composer import ComposerAgent

def main():
    agent = ComposerAgent()
    agent.run(output_filename="test_melody.wav", num_notes=5)

if __name__ == "__main__":
    main()
