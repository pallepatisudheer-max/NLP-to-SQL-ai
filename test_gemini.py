import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
print("API Key Found:", os.getenv("GEMINI_API_KEY") is not None)
print("API Key:", os.getenv("GEMINI_API_KEY")[:10] + "...")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

response = model.generate_content(
    "Convert to SQL: Show all employees"
)

print(response.text)