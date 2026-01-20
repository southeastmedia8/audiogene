# OmniAudio Benchmarking Strategy

## Goal: The "Best Musician Ever" Standard

To achieve the status of "Best Musician Ever," the OmniAudio system must excel not just in generating sound, but in **Composition**, **Performance**, **Production**, and **Creativity**. This document outlines the plan to benchmark these dimensions quantitatively and qualitatively.

## 1. Evaluation Dimensions

### A. Composition (The "Composer")
- **Structural Coherence**: Does the piece have a beginning, middle, and end? Does it develop motifs?
- **Harmonic Complexity**: Usage of varied chord progressions, modulations, and voice leading.
- **Melodic Interest**: Contour, rhythm, and memorability of melodies.
- **Style Adherence**: When asked for "Jazz", does it play Jazz?

### B. Performance (The "Virtuoso")
- **Humanization**: Micro-timing deviations (rubato), velocity dynamics, and articulation.
- **Instrument Realism**: For physics models, does the violin sound like a bow on a string?
- **Expressivity**: Dynamic range usage to convey emotion.

### C. Production (The "Engineer")
- **Audio Quality**: Sample rate, absence of artifacts (clicks, pops, aliasing).
- **Mix Balance**: Frequency spectrum balance (Pink noise reference), stereo field usage.
- **Loudness**: Target LUFS adherence for streaming platforms (-14 LUFS).

## 2. Methodology

### Tier 1: Objective DSP Metrics (Automated)
These run on every commit/generation.
- **Dynamic Range**: Measures the difference between peak and RMS.
- **Spectral Flatness**: Detects noise vs tone.
- **Clipping Detection**: Percentage of samples at 0dBFS.
- **Silence Detection**: Ensuring the agent actually produced sound.

### Tier 2: Model-Based Evaluation (AI Critics)
Using SOTA models to judge our models.
- **CLAP Score (Contrastive Language-Audio Pretraining)**: Measures text-to-audio alignment. "Does this sound like 'sad piano music'?"
- **LLM Music Theory Critic**: Convert generated sequences (MIDI/ABC) to text and ask GPT-4/Claude to analyze the harmonic structure.
- **FAD (Fréchet Audio Distance)**: Measures distribution distance between generated audio and a reference dataset (e.g., high-quality studio recordings).

### Tier 3: Human Evaluation (Subjective)
- **Blind Side-by-Side (A/B) Tests**: Compare OmniAudio vs Suno vs Human compositions.
- **Mean Opinion Score (MOS)**: Rate 1-5 on "Musicality", "Fidelity", "Emotion".

## 3. Benchmarking Suite Implementation Plan

The `benchmarks/` directory contains the harness.

```python
# Example Usage
from benchmarks.suite import BenchmarkSuite
from agents.composer import ComposerAgent

agent = ComposerAgent()
suite = BenchmarkSuite(agent)
results = suite.run(num_trials=50)
print(results.summary())
```

## 4. Reference Baselines
To be the "best", we compare against:
1.  **SOTA AI**: MusicGen-Large, AudioLDM-2, Suno AI (v3).
2.  **Human Virtuosos**: Dataset of isolated tracks from professional recordings.
