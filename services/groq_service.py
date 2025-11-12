import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("No se encontró GROQ_API_KEY en el .env")

client = Groq(api_key=api_key)

def groq_text_response(prompt: str) -> str:
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error IA: {e}"

def groq_transcribe(file_path: str) -> str:
    try:
        with open(file_path, "rb") as f:
            transcription = client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=f
            )
        return transcription.text
    except Exception as e:
        return f"Error al transcribir: {e}"
