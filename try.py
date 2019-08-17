import sys
import math
import csv

import numpy as np

from rdp import rdp


wdif = sys.argv[1]
wdof = sys.argv[2]
epsilon = float(sys.argv[3])
#x_name = float(sys.argv[4])
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
            y.append(row[1])

    return x, y


x,y = readMyFile(wdif)

print(x)
print(y)

m = np.reshape([x,y],(1,1))
print(m)

matrix = np.asmatrix([np.transpose(x), np.transpose(y)])
print(matrix)
matrix = matrix.transpose()
matrix = np.delete(matrix,0,0)
print(matrix)

print("end matrix")
"""
if = open(wdinput)
if.next()
of = open(wdoutput,'w')


for line in input_file:

    attr = line.rstrip('\n\r').split(',') 
    time = float(attr[0])
    CH1 = float(attr[1])
"""

result = rdp([[1, 1], [1, 1.1], [2, 2]], epsilon)
print(result)
result = rdp(matrix,epsilon)
print(result)

