<div align="center">

# 🎮 **TriviaBot**
### *El bot de trivia más inteligente, divertido y humano de Telegram*

🚀 Aprendé, competí y divertite con un bot que combina  
**preguntas dinámicas + IA + análisis emocional + multimedia.**

</div>

---

## ✨ **¿Qué es TriviaBot?**

**TriviaBot** transforma el clásico juego de preguntas y respuestas en una  
**experiencia interactiva** impulsada por *Inteligencia Artificial*.  
Aprende del usuario, adapta la dificultad, transcribe audios y hasta puede interpretar imágenes.

Una herramienta ideal para:
- Aprender jugando  
- Entrenar la memoria  
- Dinámicas educativas  
- Evaluaciones rápidas  
- ONG, escuelas y empresas que busquen innovación  

---

## 💡 **Nuestra propuesta**

### ❗ Problema  
Las personas buscan formas **divertidas, rápidas y accesibles** de aprender, practicar conocimientos y entrenar habilidades cognitivas.  
Las herramientas tradicionales suelen ser rígidas, aburridas o poco interactivas.

### ✅ Solución  
Creamos un **bot inteligente de Telegram** que combina:
- Preguntas dinámicas  
- Retroalimentación instantánea  
- Análisis emocional con IA  
- Transcripción de audio
- Adaptación del nivel según el animo descrito por el analisis emocional
- (Futuro) análisis de imágenes  
 

🎯 Todo desde un chat de Telegram, sin instalar nada extra.

---

## 🧠 **Características principales**

### 🎯 Modo Trivia
- Preguntas segun el estado del animo
- Dificultad adaptable  
- Evaluación automática  
- Puntuación y rachas  (en proceso)
- Rankings y progreso (ren proceso)

---

### 🤖 Inteligencia Artificial
- Respuestas empáticas y humorísticas  
- Reconocimiento de tono emocional   
- Personalidad propia (simpática y centrada en trivia)

---

### 🎤🎨 Procesamiento Multimedia
- **Audio → Texto (Speech-to-Text)**  
- **(Próximo)** Trivia visual a partir de imágenes  
- Soporte para texto, audio.

---

### 📊 Estadísticas (en proceso)
- Registro de aciertos  
- Historial básico  
- Progreso por categoría (en desarrollo)

---

## 🛠️ **Tecnologías utilizadas**

- **Python 3**
- **pyTelegramBotAPI**
- **Groq LLM** para IA conversacional
- **Transcripción de audio**
- JSON para el banco de preguntas
- Handlers modulares para escalabilidad
- dotenv

---


# 🧩 **Estructura del proyecto**

handlers/
audio_handler.py # Procesa audios y los transcribe
text_handler.py # Maneja /start y mensajes de texto
trivia_handler.py # Lógica del juego de trivia
services/
audio_service.py # Servicio de transcripción
groq_service.py # IA para respuestas
data/
preguntas.json # Banco de preguntas
main.py # Ejecución del bot

yaml
Copiar código

---

# 🚀 **Cómo usarlo**

### 1️⃣ Cloná el repositorio

```bash
git clone https://github.com/alec900/SIC-Capstone-Proyect-grupo-NONAME.git
cd SIC-Capstone-Proyect-grupo-NONAME
2️⃣ Instalá las dependencias
bash
Copiar código
pip install -r requirements.txt
3️⃣ Configurá tus variables de entorno
Crear archivo .env:

ini
Copiar código
BOT_TOKEN=TU_TOKEN_DE_TELEGRAM
GROQ_API_KEY=TU_API_KEY
4️⃣ Ejecutá el bot
bash
Copiar código
python main.py
Listo. Ya podés usar TriviaBot desde Telegram. 🎉

📁 Banco de preguntas
Puedes editar fácilmente el archivo:

/data/preguntas.json

Formato:

json
Copiar código
{
  "pregunta": "¿Cuál es la capital de Francia?",
  "respuesta": "paris"
}
Solo agregá más objetos en el arreglo y el bot los usará automáticamente.

RECOMENDACIONES IMPORTATES PARA LA UTILIZACION DEL BOT!
el bot inicial al escribirle hola
para iniciar la trivia se debe utilizar el comando /trivia
la dificultad se selecciona segun el estado de animo. si se esta feliz la dificultad es la maxima
si estas cansado la dificultad es minima

RECOMENDACIONES PARA EL CHAT DE VOZ
el chat de para iniciar el juego lo inicia con las siguientes palabras: quiero jugar
si el bot no escucha esa palabra la trivia no inicia.



🏛️ Aplicaciones prácticas
TriviaBot puede integrarse en:
Talleres educativos
Programas de formación
ONG orientadas a jóvenes
Actividades de gamificación
Evaluaciones rápidas
Equipos de trabajo
Eventos o concursos
Permite aprender de forma divertida y medir conocimientos sin estrés.

📌 Roadmap
-Modo multijugador
-Ranking global
-Logros y niveles
-Panel de administración
-Trivia visual con imágenes
-Modo “desafío diario”
-Base de datos + dashboard estadístico

👥 Autores

Proyecto desarrollado por:
-Alexis Fabian Nuñez
-Florencia Ferreyra Cadario
-Candela Magali Gallardo
