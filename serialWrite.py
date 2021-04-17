import serial
import os
import time

ser = serial.Serial()
ser.baudrate = 9600
ser.port='COM3'
time.sleep(2)

try:
    ser.open()
except Exception: 
    print("error open serial port: ")
    exit()

while True:
    data = "YEP"
    str1 = bytes(data, 'utf-8')
    ser.write(str1)
    ser.flush()
    time.sleep(0.5)

