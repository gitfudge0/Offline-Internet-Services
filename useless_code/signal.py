#!/usr/bin/python3

import serial
import sys
import time
import os

import handlefile


def main():
    isSignalTrue()
    
def signalTrue(number, query):
    ch = 0
    #signal = False
    global infolder, profolder, outfolder
    infolder = handlefile.getList('in')
    profolder = handlefile.getList('process')
    outfolder = handlefile.getList('out')
    print(profolder)
    print('Signal Activator')

    #Create file
    #Check if you can directly call the working_search.py
    #and working_nav.py to work on the query and send it back
    
    #
    #searchmatch = re.search('', query)
    #navmatch = re.search('', query)
    #
    #if
    #
    #
    #
    #
    4#
    #
    
    handlefile.create(output)
#   execute process  
#   handlefile.moveToOutput()
#   handlefile.moveToProcess()
    

if __name__ == '__main__': main()