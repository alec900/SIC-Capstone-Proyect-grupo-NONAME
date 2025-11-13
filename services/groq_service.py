import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("No se encontró GROQ_API_KEY en el .env")

client = Groq(api_key=api_key)

def groq_text_response(prompt: str) -> str:
    """
    Envía texto a Groq y devuelve la respuesta generada.
    El bot se comporta como Triviabot: solo habla sobre trivia general,
    sin ofrecer categorías ni temas, y responde de forma simpática pero breve.
    """
    try:
        system_prompt = (
            "Sos Triviabot, un bot simpático especializado en trivia general. "
            "Tu base de preguntas proviene de un archivo JSON interno, por lo tanto NO tenés categorías "
            "ni podés ofrecer elegir temas. "
            "Si alguien pregunta por categorías o temas, explicá que todas las preguntas son aleatorias "
            "Respondé de forma breve, amable y profesional. "
            "Si el mensaje no tiene que ver con trivia, respondé con humor que solo sabés de trivia."
        )

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=500
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
    
