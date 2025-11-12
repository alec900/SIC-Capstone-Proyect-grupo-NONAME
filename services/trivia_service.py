import json
import random
import os

# Ruta al archivo JSON de preguntas
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "preguntas.json")

# Cargar preguntas
with open(DATA_PATH, "r", encoding="utf-8") as f:
    PREGUNTAS = json.load(f)

# Estado en memoria por usuario
usuario_preguntas = {}

def obtener_pregunta(user_id: int) -> dict:
    """
    Devuelve una pregunta aleatoria para un usuario.
    Mantiene un historial para no repetir preguntas inmediatamente.
    """
    if user_id not in usuario_preguntas:
        usuario_preguntas[user_id] = []

    disponibles = [p for p in PREGUNTAS if p not in usuario_preguntas[user_id]]

    if not disponibles:
        # Si ya se acabaron todas, reiniciamos el historial
        usuario_preguntas[user_id] = []
        disponibles = PREGUNTAS.copy()

    pregunta = random.choice(disponibles)
    usuario_preguntas[user_id].append(pregunta)
    return pregunta

def verificar_respuesta(pregunta_obj: dict, respuesta_usuario: str) -> bool:
    """
    Verifica si la respuesta del usuario es correcta.
    """
    correcta = pregunta_obj["respuesta"].strip().lower()
    return respuesta_usuario.strip().lower() == correcta