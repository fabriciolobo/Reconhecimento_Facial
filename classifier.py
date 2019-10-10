from db_utils import *
from sklearn import svm
import ctypes
from cv2 import cv2

CONFIDENCE = 0

X, Y = create_database(load_database_image())
save_database(X, Y)

# To complete ---------------------------
classifier = svm.SVC()

X, Y = load_database()
labels = load_labels()

classifier.fit(X, Y)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # To complete ---------------------------
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        a = classifier.predict(frame)
        a = str(a)
        ctypes.windll.user32.MessageBoxW(0, a, 'Eu Digo que Você é:', 1)
        break

cap.release()
cv2.destroyAllWindows()
