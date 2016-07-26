#!usr/bin/python3
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) #9600 is baudrate
ser.flush()

ser.write('AT+CMGF=1\r')
print(ser.read(100))
ser.write('AT+CSCA?\r')
print(ser.read(100))
ser.write('AT+CPMS=\"SM\",\"SM\",\"SM\"\r')
print(ser.read(100))
ser.write('AT+CMGL=\"REC UNREAD\"\r')
print(ser.read(1000))
ser.close()
