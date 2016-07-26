#!usr/bin/python3
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) #9600 is baudrate

number = 9003133734
message = "Test Message"



ser.flush()

ser.write('AT+CMGF=1;\r')
ser.read(2)
time.sleep(2)

ser.write('AT+CSCS=\"GSM\";\r')
time.sleep(2)

ser.write('AT+CMGS=\"9003133734\";\r')
time.sleep(2)
ser.write(message)
ser.write('\x1A')
time.sleep(5)
ser.close()
