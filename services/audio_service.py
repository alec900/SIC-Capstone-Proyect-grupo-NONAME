import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def transcribir_audio(ruta_archivo):
    """
    Envía un archivo de audio a Groq y devuelve la transcripción de voz a texto.
    """
    with open(ruta_archivo, "rb") as audio_file:
        response = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-large-v3"
        )
    return response.text
    

    