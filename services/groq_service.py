from groq import Groq

client = None  # Cliente global, se inicializa desde main

def init_client(api_key: str):
    """Inicializa el cliente Groq con la API Key"""
    global client
    if not api_key:
        raise ValueError("No se proporcionó la API Key para Groq")
    client = Groq(api_key=api_key)

def groq_text(prompt: str) -> str:
    """Ejemplo de función que usa el cliente"""
    if client is None:
        raise ValueError("Cliente Groq no inicializado")
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return completion.choices[0].message["content"]

def groq_transcribe(audio_path: str) -> str:
    """Ejemplo de transcripción de audio"""
    if client is None:
        raise ValueError("Cliente Groq no inicializado")
    return client.audio.transcriptions.create(file=audio_path) 
