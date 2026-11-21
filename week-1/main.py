
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

# Get API key
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API key not found in .env file!")

# Create OpenAI client
client = OpenAI(api_key=api_key)

# Send a question to the AI model
response = client.responses.create(
    model="gpt-6-luna",
    input="What is Artificial Intelligence? Explain in simple words."
)

# Display the answer
print("\n========== LLM RESPONSE ==========")
print(response.output_text)
print("=================================")
