
import os
from dotenv import load_dotenv

from llm_client import (
    GeminiProvider,
    OllamaProvider,
    LLMClient
)

load_dotenv()

provider_name = input("Choose provider (gemini/ollama): ").lower()

if provider_name == "gemini":
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file")

    provider = GeminiProvider(api_key)

elif provider_name == "ollama":
    provider = OllamaProvider()

else:
    raise ValueError("Invalid provider selected")

client = LLMClient(provider)

prompt = input("Enter your prompt: ")

response = client.generate(prompt)

print("\nAI Response:")
print(response)
