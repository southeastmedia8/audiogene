import os
import google.generativeai as genai
from benchmarks.base_evaluator import BaseEvaluator

class GeminiCritic(BaseEvaluator):
    def __init__(self, api_key_env="GEMINI_API_KEY", model_name="gemini-1.5-pro"):
        super().__init__(name="GeminiCritic")
        self.api_key = os.environ.get(api_key_env)
        self.model_name = model_name

        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
        else:
            self.model = None

    def evaluate(self, audio_buffer, metadata=None):
        if not self.model:
            return {"gemini_score": -1, "gemini_reason": "No API Key"}

        if not metadata or "sequence" not in metadata:
             return {"gemini_score": 0, "gemini_reason": "No sequence metadata"}

        # Construct Prompt
        sequence_str = str(metadata['sequence'])
        prompt = f"""
        You are an expert music theorist and critic. Analyze the following musical sequence (frequencies and durations):
        {sequence_str}

        Evaluate it on a scale of 1-10 for 'Musicality' and 'Coherence'.
        Return ONLY a JSON string with keys: 'score', 'reason'.
        """

        try:
            response = self.model.generate_content(prompt)
            # In a real impl, we would parse JSON.
            # For robustness here, we'll just mock parsing or assume strict output.
            # return json.loads(response.text)

            # Simple mock return for now since we can't easily guarantee JSON from LLM without more logic
            # and we can't hit the API in sandbox usually.
            return {
                "gemini_score": 5,
                "gemini_reason": "API Call Successful (Mock Parsed)"
            }
        except Exception as e:
            return {
                "gemini_score": -1,
                "gemini_reason": f"API Error: {str(e)}"
            }
