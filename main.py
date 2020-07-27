import cv2
from PIL import Image
import numpy as np
import time
from play import *


mask_source = "mask.png"
cascade = "/home/kuba/.local/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_alt.xml"
mask = Image.open(mask_source)

face_cascade = cv2.CascadeClassifier(cascade)

def thug_life(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.15)
    background = Image.fromarray(image)

    for (x, y, w, h) in faces:
        resized_mask = mask.resize((w, h), Image.ANTIALIAS)
        offset = (x, y)
        background.paste(resized_mask, offset, mask=resized_mask)
    return np.asarray(background)


capture = cv2.VideoCapture(cv2.CAP_ANY)

while True:
    ret, frame = capture.read()

    if ret:
        cv2.imshow("Thug Life", thug_life(frame))

        if cv2.waitKey(1) == 27:
            break


capture.release()
cv2.destroyAllWindows()

play_music()
