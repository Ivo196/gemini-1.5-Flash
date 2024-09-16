import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

response = model.generate_content("Dime algo que no sepa?")

print(response.text) 