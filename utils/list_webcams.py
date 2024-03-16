import cv2


def list_and_test_webcams(max_webcams=5):
    """
    Liste et teste les webcams disponibles jusqu'à un maximum spécifié.

    :param max_webcams: Nombre maximum de webcams à tester.
    """
    available_webcams = []
    for index in range(max_webcams):
        cap = cv2.VideoCapture(index, cv2.CAP_DSHOW)
        if cap.isOpened():
            ret, frame = cap.read()
            if ret:
                available_webcams.append(index)
                print(f"Webcam {index} fonctionne et est disponible.")
                # Optionnel : Sauvegarder une image test pour chaque webcam détectée
                cv2.imwrite(f"webcam_test_{index}.jpg", frame)
            cap.release()
        else:
            print(f"Webcam {index} n'est pas disponible.")

    if not available_webcams:
        print("Aucune webcam disponible.")
    else:
        print(f"Webcams disponibles : {available_webcams}")
    return available_webcams


# Exécuter la fonction pour lister et tester les webcams
# list_and_test_webcams()
