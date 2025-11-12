from services.groq_service import groq_transcribe

def transcribir_audio(file_bytes: bytes):
    try:
        return groq_transcribe(file_bytes)
    except:
        return None 
    

    