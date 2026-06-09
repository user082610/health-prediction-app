"""
ai_service.py - AI/ML integration for health predictions.

Uses Google Gemini API to analyze patient blood test results
(glucose, haemoglobin, cholesterol) and generate a health risk
assessment. This prediction is stored in the 'Remarks' field.
"""

import google.generativeai as genai
import os


def get_health_prediction(glucose, haemoglobin, cholesterol):
    """
    Calls the Google Gemini API to predict possible health conditions
    based on patient blood test results.

    Args:
        glucose (float): Blood glucose level in mg/dL
        haemoglobin (float): Haemoglobin level in g/dL
        cholesterol (float): Cholesterol level in mg/dL

    Returns:
        str: AI-generated health risk assessment
    """
    try:
        # Get API key from environment variables
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            return "AI prediction unavailable — API key not configured."

        # Configure the Gemini API client
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-flash-latest')

        # Build the prompt with blood test values and normal ranges
        prompt = f"""You are a medical AI assistant. Based on the following 
blood test results, provide a brief health risk assessment and mention 
any possible conditions to watch for.

Blood Test Results:
- Glucose: {glucose} mg/dL (Normal fasting range: 70–100 mg/dL)
- Haemoglobin: {haemoglobin} g/dL (Normal range: 12–17 g/dL)
- Cholesterol: {cholesterol} mg/dL (Desirable: below 200 mg/dL)

Instructions:
- Keep the response to 2–3 concise sentences.
- Mention if each value is normal, low, or high.
- Suggest any potential health risks if values are abnormal.
- Be professional and informative.
- Do NOT use markdown formatting."""

        # Call the Gemini API and return the response
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        # Return a user-friendly message if the API call fails
        return f"AI prediction unavailable — {str(e)}"
