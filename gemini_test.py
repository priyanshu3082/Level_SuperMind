import google.generativeai as genai

# Set up the Gemini API key
GENAI_API_KEY = "AIzaSyDXCLamwsN4DjpoL2KN0by503BfP04h7Yw"  # Replace with your actual key

# Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)

# Test the API Connection
try:
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content("Hello, Gemini! Can you process text?")
    print("API is working! Response:", response.text)
except Exception as e:
    print("Error:", e)
