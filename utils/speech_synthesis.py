import pyttsx3


def text_to_speech(text):
    """
    Convertit le texte en parole.

    :param text: Texte à convertir en parole.
    """
    engine = pyttsx3.init()  # Initialise le moteur de synthèse vocale
    engine.say(text)  # Ajoute le texte à la file d'attente du moteur de parole
    engine.runAndWait()  # Bloque pendant que le texte est en train d'être lu

# Exemple d'utilisation (peut être supprimé ou commenté dans le code final)
# text_to_speech("Bonjour, ceci est un test de synthèse vocale.")
