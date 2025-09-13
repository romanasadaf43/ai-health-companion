from groq import Groq
import os

# Initialize Groq client (API key auto-loaded from env var)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_text(text: str):
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",   # Groq's free large model
            messages=[
                {"role": "system", "content": "You are an AI Health Companion. Analyze clinical reports and explain results in clear, inclusive, and supportive language."},
                {"role": "user", "content": text}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error while analyzing: {str(e)}"

if __name__ == "__main__":
    sample_text = "HIV-1 RNA, PCR result: 885 copies/mL (Reference: <50)"
    print("🔎 Health Companion Analysis:\n")
    print(analyze_text(sample_text))
