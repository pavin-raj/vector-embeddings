from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set the GENAI_API_KEY environment variable.")

client = genai.Client(api_key=api_key)

result = client.models.embed_content(
        model="gemini-embedding-001",
        contents= "Pavin Raj"
)

for embedding in result.embeddings:
    print(embedding)