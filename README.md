🎮 TriviaBot – Bot Inteligente de Trivia para Telegram

Entretenimiento, aprendizaje y análisis inteligente en un solo bot.

🧠 ¿Qué es TriviaBot?

TriviaBot transforma el clásico juego de preguntas y respuestas en una experiencia interactiva impulsada por Inteligencia Artificial.
Su objetivo es combinar diversión, aprendizaje, análisis emocional y accesibilidad multimedia, incentivando:

-La curiosidad

-El pensamiento crítico

-La memoria

-La competencia sana

-El aprendizaje autónomo


Es ideal tanto para usuarios casuales como para instituciones que quieran fomentar dinámicas educativas o evaluar conocimientos de forma innovadora.

Características principales

-Sistema de Trivia
Preguntas por categorías (Ciencia, Historia, Geografía, Cultura, Deportes, etc.).
Niveles de dificultad escalables.
Puntuación automática.
Rankings y progreso.
Selección aleatoria o adaptativa según desempeño.

-Inteligencia Artificial
Respuestas empáticas y simpáticas cuando se dialoga fuera del contexto de trivia.
Análisis de emociones a partir del texto.
Recomendación de categorías según intereses del usuario.
Ajuste dinámico de la dificultad (“aprender del usuario”).

-Procesamiento Multimedia
TriviaBot interpreta diferentes tipos de entrada:
Audio: transcripción automática (speech-to-text).
Imágenes (futuro): para “trivia visual”.
Texto:modo tradicional de preguntas y respuestas.

-Estadísticas & seguimiento
Registro de aciertos.
Historial de desempeño.
Progreso por categoría.
Niveles de usuario.

🧩 ¿Cómo funciona?

El usuario escribe /start → el bot se presenta.

El usuario envía /trivia → inicia una pregunta.

TriviaBot elige una pregunta aleatoria del banco (preguntas.json).

Guarda internamente la respuesta correcta.

El usuario responde por texto.

El bot evalúa:

Si es correcta: felicita.

Si es incorrecta: muestra la respuesta correcta.

Ofrece jugar otra.

También puede recibir audios y transcribirlos automáticamente.

🧠 Nuestra solución 

Las personas buscan una forma divertida, accesible e interactiva de aprender, entrenar la memoria y desafiarse con conocimientos de cultura general.
Además, muchas herramientas educativas son estáticas, rígidas y poco personalizadas.

✅ Solución

Creamos un bot inteligente de Telegram que combina:
-Preguntas dinámicas
-IA que detecta tono y genera respuestas simpáticas
-Adaptación del nivel de dificultad
-Interacción por texto, audio e imagen
-Experiencia accesible, rápida y gratuita

Incluye:
-Formulación de preguntas en múltiples categorías
-Evaluación automática
-Retroalimentación inmediata
-Detección emocional
-Personalización por desempeño
-Transcripción de audios
-(En desarrollo) Trivia visual desde imágenes

🏛️ Aplicaciones en gestión, educación y organizaciones

TriviaBot no es solo un juego:
Puede adaptarse para procesos de capacitación interna, onboarding, formación continua y evaluación rápida.

🛠️ Instalación y requisitos
📌 Requisitos previos

Python 3.9+
Token de Bot de Telegram
Librerías de IA (Groq u otra LLM)
Dependencias de transcripción (según audio_service)

📦 Instalación

Clonar el repositorio

git clone https://github.com/alec900/SIC-Capstone-Proyect-grupo-NONAME.git
cd SIC-Capstone-Proyect-grupo-NONAME


Instalar dependencias

pip install -r requirements.txt


Configurar variables de entorno

Crear un .env:

BOT_TOKEN=TU_TOKEN_DE_TELEGRAM
GROQ_API_KEY=TU_API_KEY


Estructura del proyecto

handlers/
    audio_handler.py
    text_handler.py
    trivia_handler.py
services/
    audio_service.py
    groq_service.py
data/
    preguntas.json
main.py


Ejecutar el bot

python main.py

📁 Handlers principales
-audio_handler.py
Recibe audios → los transcribe.

-text_handler.py
Maneja /start
Atiende mensajes que no sean trivia
Usa IA para respuestas simpáticas

-trivia_handler.py
Maneja /trivia
Selecciona preguntas del JSON
Evalúa respuestas
Lleva registro temporal por usuario

📚 Banco de preguntas

Todas las preguntas se encuentran en:

/data/preguntas.json

Formato:

{
  "pregunta": "¿Cuál es la capital de Francia?",
  "respuesta": "paris"
}


Podés agregar, borrar o modificar preguntas desde ahí.

👥 Autores

Proyecto desarrollado por:
-Alexis Fabian Nuñez
-Florencia Ferreyra Cadario
-Candela Magali Gallardo
