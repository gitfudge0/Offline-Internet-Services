#!/usr/bin/python3

import re

def main():
    counter = 0
    print('Searching for number and message...')
    f = open('regex.txt')
    for line in f:

        match = re.search('(\+\d{1,12})', line)
        match2 = re.search('.*', line)
        match3 = re.search('\s*', line)
        if counter == 0:
            
            counter += 1
            continue
        elif match:
            #print('Match found')
            print('Number: ' + match.group())
            counter += 1
        elif match2:
            if counter == 1:
                counter += 1
                continue
            elif counter == 2:
                print('Message: ' + match2.group())
                counter += 1
            else:
                break




if __name__ == '__main__':
	main()
