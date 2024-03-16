import cv2


def capture_image(image_path='images/lightinnight.jpg',camera_index=0):
    """
    Capture une image à partir de la webcam et la sauvegarde à l'emplacement spécifié.

    :param image_path: Chemin où sauvegarder l'image capturée. La valeur par défaut est 'captured_image.jpg'.
    """
    cap = cv2.VideoCapture(
        camera_index, cv2.CAP_DSHOW)  # Initialise la capture vidéo. '0' est généralement l'identifiant de la première webcam disponible.

    # Vérifie si la webcam a été correctement initialisée
    if not cap.isOpened():
        print("Erreur : la webcam ne peut pas être ouverte.")
        return

    # Capture un seul frame
    ret, frame = cap.read()

    # Vérifie si le frame a été capturé correctement
    if ret:
        # Sauvegarde l'image dans le fichier spécifié
        cv2.imwrite(image_path, frame)
        print(f"Image capturée et sauvegardée à {image_path}")
    else:
        print("Erreur : échec de la capture de l'image.")

    # Libère la capture vidéo
    cap.release()

# Exemple d'utilisation (peut être supprimé ou commenté dans le code final)
capture_image("test_image.jpg")
