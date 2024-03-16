import base64
import aiohttp
import asyncio

def encode_image(image_path):
    """
    Encode l'image spécifiée en base64.

    :param image_path: Chemin vers le fichier image à encoder.
    :return: Chaîne de caractères représentant l'image encodée en base64.
    """
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

async def send_image_to_vision_api(image_path, api_key):
    """
    Envoie une image à l'API Vision d'OpenAI de manière asynchrone et retourne la réponse.

    :param image_path: Chemin vers le fichier image à analyser.
    :param api_key: Clé API d'OpenAI.
    """
    print("Envoi de l'image à l'API Vision...")
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Je suis une personne aveugle, pouvez-vous me décrire cette image qui vient d'être prise devant moi par mon dispositif de prise de vue accrochée à mon harnais ?"
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 750
    }

    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload) as response:
            if response.status == 200:
                return await response.json()
            else:
                print("Erreur lors de l'envoi de l'image à l'API Vision:", response.status, await response.text())
                return None
