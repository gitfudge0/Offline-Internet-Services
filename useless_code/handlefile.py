#!/usr/bin/python3
#
#File Handler Module
#Gets input file
#Checks if process folder is not full
#If not full, store in process folder
#If full, store in input folder
#Once executed, move from process folder to output folder
#
#


import os
import time
import sys
import shutil

infolder = []
profolder = []
outfolder = []

def create(output):
    global infolder
    infolder = getList('in')
    profolder = getList('process')
    outfolder = getList('out')
    name = str(int(time.time()))
    infolder.append('' + name + '.txt')
    f = open('in/' + name + '.txt', 'w')
    f.write(output)
    moveToProcess()
    

def moveToProcess():
    global infolder
    global profolder
    infolder = getList('in')
    profolder = getList('process')
    outfolder = getList('out')
    if len(profolder) < 10:
        if infolder[0]:
            shutil.move('in/' + infolder[0], 'process/' + infolder[0])
            profolder.append(infolder[0])
            del infolder[0]
    else:
        print('Process Folder full')
    printList()
    
    
def moveToOutput():
    global infolder, profolder, outfolder
    infolder = getList('in')
    profolder = getList('process')
    outfolder = getList('out')
    shutil.move('process/' + profolder[0], 'out/' + profolder[0])
    outfolder.append(profolder[0])
    del profolder[0]
    printList()
    
    
    
def getList(foldername):
    return sorted(os.listdir('' + foldername + '/'))

def printList():
    global infolder, profolder, outfolder
    print('Infolder')
    print('Number of files: ' + str(len(infolder)))
    print(infolder)
    print('ProFolder')
    print('Number of files: ' + str(len(profolder)))
    print(profolder)
    print('OutFolder')
    print('Number of files: ' + str(len(outfolder)))
    print(outfolder)