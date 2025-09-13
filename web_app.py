import streamlit as st
import base64
import os
from groq import Groq

# --- Load API Key (first from secrets.toml, then environment variable) ---
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("⚠️ No API key found. Please set GROQ_API_KEY in .streamlit/secrets.toml or as an environment variable.")
else:
    client = Groq(api_key=api_key)

# Page setup
st.set_page_config(page_title="AI Health Companion", page_icon="🩺", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        background-color: #f9fafc;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #2b547e;
        margin-bottom: 20px;
    }
    .subtitle {
        text-align: center;
        font-size: 1rem;
        color: #555;
        margin-bottom: 30px;
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App header
st.markdown("<div class='title'>🩺 AI Health Companion</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Upload your lab report and get AI-powered analysis</div>", unsafe_allow_html=True)

# File upload
uploaded_file = st.file_uploader("Upload your lab report (image)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None and api_key:
    # Convert to base64 for Groq
    img_bytes = uploaded_file.read()
    img_base64 = base64.b64encode(img_bytes).decode("utf-8")
    img_url = f"data:image/png;base64,{img_base64}"

    # Two-column layout
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📄 Uploaded Report")
        st.image(uploaded_file, caption="Your Lab Report", use_container_width=True)
        
    with col2:
        st.markdown("### 🤖 AI Analysis")
        with st.spinner("Analyzing your report..."):
            try:
                chat_completion = client.chat.completions.create(
                    model="meta-llama/llama-4-scout-17b-16e-instruct",  # ✅ Updated model
                    messages=[
                        {
                            "role": "system",
                            "content": "You are a helpful AI health assistant. Explain the lab report in simple terms for the patient."
                        },
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "Please analyze this medical report."},
                                {"type": "image_url", "image_url": {"url": img_url}}
                            ]
                        }
                    ],
                )

                ai_response = chat_completion.choices[0].message.content
                st.markdown(f"<div class='card'>{ai_response}</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"⚠️ Error during AI analysis: {str(e)}")
