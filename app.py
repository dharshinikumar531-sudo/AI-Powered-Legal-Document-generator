import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)

st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.write(
    "Enter your legal document below and LegalEase will provide "
    "a simple explanation of the document."
)

# Check API key
if not api_key:
    st.error("Gemini API key not found. Please check your .env file.")
    st.stop()

# Create Gemini client
client = genai.Client(api_key=api_key)

# Document input
document_text = st.text_area(
    "📄 Enter your legal document text:",
    height=300,
    placeholder="Paste your legal document here..."
)

# Analyze button
if st.button("🔍 Analyze Document", type="primary"):

    if not document_text.strip():
        st.warning("Please enter a legal document first.")

    else:
        with st.spinner("Analyzing your document..."):

            prompt = f"""
You are a legal document analysis assistant.

Analyze the following legal document in simple language.

Provide:

1. Simple Summary
2. Key Points
3. Important Obligations
4. Dates and Deadlines
5. Potential Concerns
6. Important Terms

Do not provide legal advice. Clearly mention that the result
is for general informational purposes only.

Legal Document:

{document_text}
"""

            try:
                response = client.models.generate_content(
                model="gemini-3.8-flash",
                 contents=prompt
        )

                st.success("Document analyzed successfully!")

                st.subheader("📋 LegalEase Analysis")
                st.write(response.text)

                st.info(
                    "⚠️ This analysis is for general informational "
                    "purposes only and is not a substitute for advice "
                    "from a qualified legal professional."
                )

            except Exception as e:
                st.error(f"Error while analyzing document: {e}")