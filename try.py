import sys
import math
import csv

import numpy as np

from rdp import rdp


wdif = sys.argv[1]
wdof = sys.argv[2]
epsilon = float(sys.argv[3])
columN = int(sys.argv[4])
#y_name = float(sys.argv[5])

print(" ")
print("Parameters:" + " "+ wdif + " " + wdof + " " + str(epsilon))
print(" ")

def readMyFile(filename):
    x = []
    y = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            x.append(row[0])
            y.append(row[columN])

    return x, y

def writeData(data_,wdof):  
    with open(wdof, 'w') as csvf:
        f = csv.writer(csvf)
        #for row in :
        f.writerows(data_)

x,y = readMyFile(wdif)
open(wdof, 'w').close

#print(x)
#print(float(y[1]))

matrix = []
for i in range(1,len(x)):
    matrix.append([float(x[i]),float(y[i])])

#print(matrix)

#print("end matrix")
"""
if = open(wdinput)
if.next()
of = open(wdoutput,'w')


for line in input_file:

    attr = line.rstrip('\n\r').split(',') 
    time = float(attr[0])
    CH1 = float(attr[1])
"""

#result = rdp([[1, 1], [1, 1.1], [2, 2]], epsilon)
#print(result)
result = rdp(matrix,epsilon)
#print(result)
writeData(result,wdof)
