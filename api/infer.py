import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()

# Configure API key for Google Generative AI
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise ValueError("Google API key not found. Check your .env file.")
genai.configure(api_key=GOOGLE_API_KEY)

# Function to get a summary or assessment from the Gemini model
def get_gemini_response(prompt):
    """Get response from the Gemini model for a given prompt."""
    model = genai.GenerativeModel('gemini-pro') 
    response = model.generate_content(prompt)
    return response.text

def infer_with_gemini(policy_text):
    """Perform inference on the input privacy policy text using Google Gemini."""
    # Create a prompt for summarizing or assessing the privacy policy
    prompt = f"Please summarize the following privacy policy:\n\n{policy_text}\n\nSummary:"
    
    # Get the response from Gemini
    result = get_gemini_response(prompt)
    
    return result

# Example of how to use the function (for testing purposes)
if __name__ == "__main__":
    # Test with a sample privacy policy text
    test_policy_text = """
    This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you visit our website.
    We may collect personal data such as your name, email address, and payment information. We use this information
    to provide services, communicate with you, and improve our offerings.
    """
    
    summary = infer_with_gemini(test_policy_text)
    print("Gemini Response - Policy Summary:", summary)
