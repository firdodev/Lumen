import openai
from Lumen.Resources.ConfigLoader import LoadConfig
import time


class OpenAIResponse:
    def __init__(self):
        # Set up your API key
        # You should keep your API key secret and possibly use environment variables or a config file.
        openai.api_key = LoadConfig().get('api', '')

    def get_response(self, prompt, retries=3, delay=10):
        for _ in range(retries):
            try:
                response = openai.Completion.create(
                    engine="davinci",
                    prompt=prompt,
                    max_tokens=150
                )
                return response.choices[0].text.strip()
            except openai.error.RateLimitError:
                print(f"Rate limit exceeded. Retrying in {delay} seconds...")
                time.sleep(delay)
        raise Exception("Exceeded maximum retries due to rate limiting.")

    def interactive_mode(self):
        while True:
            user_input = input("You: whats 2 + 2")
            if user_input.lower() in ["quit", "exit"]:
                print("Goodbye!")
                break
            response = self.get_response(user_input)
            print("AI:", response)