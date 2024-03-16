import cv2
import pygame
import numpy
from ultralytics import YOLO
from ultralytics.solutions import object_counter
from ultralytics.utils.plotting import Annotator, colors

DESIRED_WIDTH = 640
DESIRED_HEIGHT = 520
desired_width_rect = 300
desired_height_rect = 300

model = YOLO("../modelsAI/yolov8x-seg.pt")
names = model.model.names

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

# Configurer la résolution souhaitée et les FPS
desired_fps = 25
cap.set(cv2.CAP_PROP_FPS, desired_fps)  # FPS
cap.set(cv2.CAP_PROP_FRAME_WIDTH, DESIRED_WIDTH)  # Largeur
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, DESIRED_HEIGHT)  # Hauteur

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("SensorSound.wav")
is_playing = False

while True:
    ret, im0 = cap.read()
    if not ret:
        print("Impossible de lire la frame de la webcam.")
        break

    im0_small = cv2.resize(im0, (DESIRED_WIDTH, DESIRED_HEIGHT))

    results = model.predict(im0_small, conf=0.5)
    annotator = Annotator(im0_small, line_width=2)

    height, width = im0_small.shape[:2]
    x_center = width // 2
    y_start = 0
    y_end = height

    x_line = width // 3
    x_line_2 = 2 * width // 3

    y_line = 2*height // 3
    y_line_2 = height
    x_end = width

    zone_free = True

    for r in results:
        for box in r.boxes:
            b = box.xyxy[0]
            if (b[2]> x_line and b[0] < x_line_2) and (b[3] > y_line and b[1] < y_line_2):
                c = box.cls
                annotator.box_label(b, f"{r.names[int(c)]} {float(box.conf):.2}")
                zone_free = False

    cv2.line(im0_small, (x_line, y_start), (x_line, y_end), (0, 255, 0), 2)
    cv2.line(im0_small, (x_line_2, y_start), (x_line_2, y_end), (0, 255, 0), 2)
    cv2.line(im0_small, (0, y_line), (width, y_line), (0, 255, 0), 2)
    cv2.line(im0_small, (0, y_line_2), (width, y_line_2), (0, 255, 0), 2)
    cv2.imshow("instance-segmentation", annotator.result())

    txt_zone_free = "Oui" if zone_free else "Non"
    print("Zone libre : ", txt_zone_free)

    if not zone_free:
        if not is_playing:
            sound.play(loops=-1)  # Jouer en boucle
            is_playing = True
    else:
        if is_playing:
            sound.stop()  # Arrêter la lecture si la zone est libre
            is_playing = False

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
