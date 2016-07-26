#!/usr/bin/python3
import time
import re

def main():
    
    x = "Microsoft Corporation   is an American multinational technology company headquartered in Redmond, Washington, that develops, manufactures, licenses, supports and sells computer software, consumer electronics and personal computers and services."
    #global y
    #size = len(x)
    #split_size = 120
    #y = list(split_by_n(x,100))
    #for line in y:
    #    print line
    
    print(len(x))
    y = [1, 2, 3]
    for line in y:
        print line
    
def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]
        


    
    
if __name__ == '__main__':
    main()

