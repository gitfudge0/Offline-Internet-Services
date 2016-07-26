#!/usr/bin/python3
import re
import time
from googlemaps import Client

def Nav(source, destination):

    # Add you API key here
    mapService = Client(key='AIzaSyARs7fiMx3bU3uRt-PuCIcUFy339IpCiYY')

    directions = mapService.directions(source, destination)
    directions = directions[0]
    time.sleep(30)
    i=1
    result = ''
    while len(result) < 5:
        for leg in directions['legs']:
            startAddress = leg['start_address']
            print "Start Address:", startAddress
            endAddress = leg['end_address']
            print "End Address:", endAddress
            result = "Start: " + startAddress + "\nEnd: " + endAddress + '\n'
            for step in leg['steps']:
                html_instructions = step['html_instructions']
                html_instructions = re.sub('<.*?>', '', html_instructions)
                html_instructions = re.sub('<\/.*?>', '', html_instructions)
                html_instructions = re.sub('&nbsp;', ' ', html_instructions)
                html_instructions = re.sub('&amp;', '&', html_instructions)
                result += "STEP {} {}".format(i ,html_instructions) + '\n'
                #print "STEP {} {}".format(i ,html_instructions)
                i = i+1

        return result

            
def main():
    source = raw_input("Source: ")
    destination = raw_input("Destination: ")
    print(Nav(source, destination))
    

if __name__ == '__main__':
    main()