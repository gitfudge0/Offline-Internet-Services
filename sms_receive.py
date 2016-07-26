#!usr/bin/python3
import serial
import time
import re
import sms_send
import handlequery

def main():

	portopener()
	ender = 'y'
	ch = 0
	while ender != 'n':
		print('1. List All')
	#	print('2. Delete All')	
		ch = input('Enter choice: ')
		if ch == 1:
			listall()
			ender = raw_input('(y/n)Continue? ')
		elif ch == 2:
			delall()
			ender = raw_input('(y/n)Continue? ')
		else:
			print('Please read properly')
	#ser.close()

def listall():
    result = ''
    #while(1): #While loop to check messages
    signalValue = False
    #portopener()
    #time.sleep(9)
    ser.write('AT+CMGL=\"ALL\"\r')
    global output
    output = ser.read(1000)
    if len(output) >= 30 :
        signalValue = True
        print('Message receieved')
        print(output)
        f = open('new.txt', 'w')
        f.write(output)
        f.close()
        number, query = response() #getting the number and query
        
        result = handlequery.handle(query)
        
        #print("Calling signal.py")
        #signal.signalTrue(number, query)
        
        #response()
        ser.close()
        f = open('output.txt', 'w')
        result_list = list(split_by_n(result,155))
        for list_item in result_list:
            f.write(list_item + '\n')
        f.close()
        
        sms_send.sender(number) #sending SMS automatically
        portopener()
    else:
        ser.close()
        print('No messages received')

 
def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]


def delall():
    portopener()
    ser.write('AT+CMGD=1,1\r')
    print(ser.read(1000))
    listall()


def response():
    global number, query
    number = ''
    query = ''
    counter = 0
    f = open('new.txt', 'r')
    p  = open('process.txt', 'w')
    for line in f:
        match = re.search('(\+\d{1,12})', line)
        match2 = re.search('.*', line)
        if counter == 0:
            counter += 1
            continue
        elif match:
            number = match.group()
            p.write(match.group())
            counter += 1
        elif match2:
            if counter == 1:
                counter += 1
                continue
            elif counter == 2:
                query = match2.group()
                p.write(match2.group())
                counter += 1
            else:
                break
    print('num: '+ number)
    print('query: ' + query)
    f.close()
    p.close()
    return number, query


def portopener():
    global ser
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout = 1) #9600 is baudrate
    ser.flush()
    ser.write('AT\r')
    print(ser.read(1000))
    ser.write('AT+CMGF=1\r')
    print(ser.read(1000))
    ser.write('AT+CPMS=\"SM\",\"SM\",\"SM\"\r')
    print(ser.read(1000))
    

    
if __name__ == '__main__':
	main()
