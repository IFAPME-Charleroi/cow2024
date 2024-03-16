import os
from dotenv import load_dotenv
import asyncio
from concurrent.futures import ThreadPoolExecutor
from services.camera_service import capture_image
from services.vision_service import send_image_to_vision_api
from utils.speech_synthesis import text_to_speech

executor = ThreadPoolExecutor()

async def async_speak(text):
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(executor, text_to_speech, text)

async def main():
    load_dotenv()
    image_path = "../images/test_image.jpg"
    capture_image(image_path, 0)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("La clé API OPENAI n'est pas définie dans les variables d'environnement.")
        return

    # Lancement asynchrone de la synthèse vocale sans attendre sa fin pour continuer
    speak_task = asyncio.create_task(async_speak("L'image est en cours de traitement, veuillez patienter."))

    # Envoi de l'image à l'API de manière asynchrone
    response = await send_image_to_vision_api(image_path, api_key)

    # Assurez-vous que la tâche de parole a fini avant de continuer
    await speak_task

    if response:
        # Lecture synchrone de la réponse car votre système ne gère probablement pas bien la lecture concurrente de texte
        text_to_speech(response['choices'][0]['message']['content'])


if __name__ == "__main__":
    asyncio.run(main())
