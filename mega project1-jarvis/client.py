# client_gemini_api_key.py
from google import genai

# The client will automatically look for the key in the GEMINI_API_KEY
# environment variable.
client = genai.Client()

resp = client.models.generate_content( # Use models.generate_content for modern client
    model="gemini-2.5-flash",
    contents='command'
)

# Print text output
print(resp.text)