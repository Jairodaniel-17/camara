import serial
import time

arduino = serial.Serial(port="COM3", baudrate=9600)
time.sleep(2)
while True:
    accion = input("Desea encender (e) / apagar (a): ")
    if accion == "e":
        arduino.write(b"e")
    elif accion == "a":
        arduino.write(b"a")
arduino.close()
