#!usr/bin/python3
import serial
import time


def main():
	global  ser
	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) #9600 is baudrate

	ser.flush()

	ser.write('AT\r')
	response()
	ser.write('AT+CMGF=1\r')
	response()
	ser.write('AT+CPMS=\"SM\",\"SM\",\"SM\"\r')
	response()
	
	ender = 'y'
	ch = 0
	while ender != 'n':
		print('1. List All')
		print('2. Delete All')	
		ch = input('Enter choice: ')
		if ch == 1:
			listall()
			ender = raw_input('(y/n)Continue? ')
		elif ch == 2:
			delall()
			ender = raw_input('(y/n)Continue? ')
		else:
			print('Please read properly')
	ser.close()

def listall():
	ser.write('AT+CMGL=\"ALL\"\r')
	response()

def delall():
	ser.write('AT+CMGD=1,1\r')
	response()
	listall()


def response():
	output = ' '
	output = ser.read(1000)
	print(output)
	ser.write('\r')


if __name__ == '__main__':
	main()
