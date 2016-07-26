#!usr/bin/python3
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) #9600 is baudrate
ser.flush()

ser.write('ATD9003133734;\r')
print(ser.read(2))
time.sleep(10)
ser.write('ATH\r')
ser.close()
