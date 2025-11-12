import json
import random
from telebot import TeleBot, types

def register_trivia(bot: TeleBot):
    @bot.message_handler(commands=["trivia"])
    def start_trivia(message):
        try:
            with open("data/preguntas.json", "r", encoding="utf-8") as f:
                preguntas = json.load(f)

            pregunta = random.choice(preguntas)
            texto_pregunta = pregunta["pregunta"]

            # Guardamos la respuesta correcta en user_data
            bot.user_data = getattr(bot, "user_data", {})
            bot.user_data[message.chat.id] = pregunta["respuesta"].lower()

            bot.send_message(message.chat.id, f"🧠 Trivia:\n\n{texto_pregunta}")
            bot.send_message(message.chat.id, "✍️ Escribí tu respuesta:")

            bot.register_next_step_handler(message, verificar_respuesta)
        except Exception as e:
            bot.send_message(message.chat.id, f"❌ Error al cargar la trivia: {e}")

    def verificar_respuesta(message):
        respuesta_usuario = message.text.lower().strip()
        correcta = bot.user_data.get(message.chat.id)

        if not correcta:
            bot.send_message(message.chat.id, "⚠️ No hay una trivia activa. Escribí /trivia para comenzar.")
            return

        if respuesta_usuario == correcta:
            bot.send_message(message.chat.id, "🎉 ¡Correcto! ✅")
        else:
            bot.send_message(message.chat.id, f"❌ Incorrecto. La respuesta correcta era: {correcta.capitalize()}")

        # Limpia la trivia actual
        bot.user_data.pop(message.chat.id, None)

        # Ofrece jugar otra
        bot.send_message(message.chat.id, "¿Querés jugar otra? Escribí /trivia para continuar 🎯") 


