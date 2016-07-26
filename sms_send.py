#!usr/bin/python3
import serial
import time

def main(): sender('+919003133734')

def sender(number):
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) #9600 is baudrate
    

    #number = raw_input('Enter the number: ')
    
    message = []
    f = open('output.txt')
    for line in f:
        message.append(line)

    #message = result
    #print('length: ' + str(len(result)))
    ser.flush()
    ser.write('AT+CMGF=1;\r') #set text mode
    time.sleep(2)
    ser.write('AT+CSCS=\"GSM\";\r') #set GSM mode
    time.sleep(2)
    for line in message:
        ser.write('AT+CMGS=\"' + number + '\";\r') #set number
        time.sleep(2)
        #if len(result) < 5:
         #   message = "No results."
        ser.write(line) #write message
        time.sleep(2)
        ser.write('\x1A')
        time.sleep(10)
    ser.close()
    f.close()
    


if __name__ == '__main__': main()
