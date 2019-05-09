#!/usr/bin/env Python

#open txt file
with open('AP.txt') as f:

    #split the LLDP file
    data = f.read().split()

    #create output file for the print
    y = open('output.txt', 'w')

    #print every 5th line and seperate but a new line, then output to file
    print("\n".join(data[::5]), file=y)
