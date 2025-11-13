historial_usuarios = {}

def agregar_mensaje(user_id: int, rol: str, contenido: str):
    """
    Guarda los mensajes del usuario y del bot en memoria.
    rol: "user" o "assistant"
    """
    if user_id not in historial_usuarios:
        historial_usuarios[user_id] = []
    
    historial_usuarios[user_id].append({"role": rol, "content": contenido})
    
    # Limitamos el historial a los últimos 10 mensajes para evitar sobrecarga
    if len(historial_usuarios[user_id]) > 10:
        historial_usuarios[user_id] = historial_usuarios[user_id][-10:]

def obtener_historial(user_id: int):
    """Devuelve el historial de conversación del usuario."""
    return historial_usuarios.get(user_id, []) 