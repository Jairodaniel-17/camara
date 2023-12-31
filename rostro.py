import cv2
import serial
import time

arduino = serial.Serial("COM3", 9600)
time.sleep(2)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
video = cv2.VideoCapture("video.mp4")  # droidcam
while video.isOpened():
    ret, frame = video.read()  # captura de l fotograma, frame ==> .jpg
    if frame is not None:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hh, ww = gray.shape
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.line(frame, (int(ww / 2), 0), (int(ww / 2), hh), (0, 0, 255))
            if x < ww / 2:
                mostrar = "I (" + str(x) + "," + str(y) + ")"
                arduino.write(b"e")
            else:
                mostrar = "D (" + str(x) + "," + str(y) + ")"
                arduino.write(b"a")
            cv2.putText(
                frame,
                mostrar,
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.4,
                (0, 0, 255),
                1,
                cv2.LINE_AA,
            )

            roi_gray = gray[y : y + h, x : x + w]
            roi_color = frame[y : y + h, x : x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for ex, ey, ew, eh in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
                cv2.rectangle(roi_gray, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
        cv2.imshow("Video", frame)
    ##        cv2.imshow('Video gris', gray)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
arduino.close()
