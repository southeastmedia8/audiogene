# Required API Keys & Tools

To unlock the full potential of the OmniAudio ecosystem and achieve "Best Musician Ever" status, the following API keys and tools are recommended. These enable advanced reasoning, state-of-the-art generation, and rigorous benchmarking.

## 1. Intelligence & Reasoning (Agents)
These keys power the "brain" of the agents (Composer, Producer, Conductor).

| Service | Env Variable | Usage | Reason |
| :--- | :--- | :--- | :--- |
| **Google Gemini** | `GEMINI_API_KEY` | `Gemini 1.5 Pro` | Primary intelligence engine for music theory critique, code generation, and multi-modal analysis. |
| **OpenAI** | `OPENAI_API_KEY` | `GPT-4o` | Fallback reasoning for composition structure, lyrics generation, and music theory critique. |
| **Anthropic** | `ANTHROPIC_API_KEY` | `Claude 3.5 Sonnet` | Excellent at code generation (CSound/SuperCollider scripts) and complex logic. |

## 2. Audio Generation Models (The "Instruments")
These keys provide access to massive, pre-trained generative audio models.

| Service | Env Variable | Usage | Reason |
| :--- | :--- | :--- | :--- |
| **Hugging Face** | `HF_TOKEN` | `MusicGen`, `AudioLDM` | Access to gated models and Inference API for running open-source SOTA models without local GPUs. |
| **Stability AI** | `STABILITY_API_KEY` | `Stable Audio` | High-fidelity texture and sound effect generation. |
| **ElevenLabs** | `ELEVEN_API_KEY` | `Speech/Singing` | Best-in-class voice synthesis for singing agents. |
| **Replicate** | `REPLICATE_API_TOKEN` | Cloud GPUs | Running massive models (e.g., MusicGen-Large) via API if local compute is insufficient. |

## 3. Benchmarking & Analysis (The "Critics")
These tools are used to evaluate the quality of the output.

| Service | Env Variable | Usage | Reason |
| :--- | :--- | :--- | :--- |
| **Weights & Biases**| `WANDB_API_KEY` | Experiment Tracking | Logging metrics for thousands of generations to track improvements over time. |
| **Spotify** | `SPOTIFY_CLIENT_ID` | Reference Analysis | Fetching audio features of hit songs to use as baselines/targets. |
| **Freesound** | `FREESOUND_API_KEY` | Data Sourcing | Downloading training/reference samples for physical models. |

## Setup
Copy the template to a local env file (DO NOT COMMIT):

```bash
cp setup/env.example .env
```
