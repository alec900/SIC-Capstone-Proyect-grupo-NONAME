import os
from groq import Groq
from dotenv import load_dotenv
from services.memory_service import agregar_mensaje, obtener_historial

# Cargar variables del .env
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("No se encontró GROQ_API_KEY en el archivo .env")

client = Groq(api_key=api_key)


# =====================================================
# 🔥 FUNCIÓN PRINCIPAL: Chat con historial
# =====================================================
def groq_text_response(user_id: int, prompt: str) -> str:
    """
    Envía texto a Groq manteniendo un historial por usuario.
    """
    # Obtener historial del usuario
    historial = obtener_historial(user_id)

    # Prompt del sistema — aquí definimos la personalidad del bot
    system_prompt = (
        "Sos Triviabot, un bot simpático especializado en trivia general. "
        "Siempre te presentás como Triviabot. "
        "Tu base de preguntas proviene de un archivo JSON interno, "
        "por lo tanto NO tenés categorías ni podés ofrecer elegir temas. "
        "Cuando alguien diga que está listo para jugar, respondé EXACTAMENTE: "
        "'¡Perfecto! Para empezar la trivia, usá el comando /trivia 🎯'. "
        "Si alguien te habla de algo que no sea trivia, respondé amablemente que solo sabés de trivia, "
        "con humor o simpatía, de forma breve y clara. "
        "Nunca inventes funcionalidades que el bot no posee."
    )

    # Construimos todos los mensajes que enviamos al modelo
    mensajes = [{"role": "system", "content": system_prompt}] + historial
    mensajes.append({"role": "user", "content": prompt})

    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=mensajes,
            temperature=0.3,
            max_tokens=300
        )

        respuesta = completion.choices[0].message.content

        # Guardar en historial
        agregar_mensaje(user_id, "user", prompt)
        agregar_mensaje(user_id, "assistant", respuesta)

        return respuesta

    except Exception as e:
        return f"Error IA: {e}"


def groq_transcribe(file_path: str) -> str:
    """
    Transcribe un archivo de audio usando Whisper.
    """
    try:
        with open(file_path, "rb") as f:
            resp = client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=f
            )
        return resp.text

    except Exception as e:
        return f"Error al transcribir: {e}"
    
    
