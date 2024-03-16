import cv2

# Essayez d'ouvrir la webcam par défaut
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Impossible d'ouvrir la caméra")
else:
    # Capturez une image
    ret, frame = cap.read()
    if ret:
        # Affichez l'image capturée dans une fenêtre
        cv2.imshow('Test Webcam', frame)
        cv2.waitKey(0)  # Attendez que l'utilisateur appuie sur une touche
        cv2.destroyAllWindows()
    else:
        print("Impossible de recevoir l'image de la caméra")
    cap.release()
