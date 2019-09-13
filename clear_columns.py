import sys
import math
import csv

import numpy as np

from rdp import rdp


wdif = sys.argv[1]
wdof = sys.argv[2]
epsi = float(sys.argv[3])
columN = int(sys.argv[4])
#y_name = float(sys.argv[5])

print(" ")
print("Parameters:" + " "+ wdif + " " + wdof)
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

def clear_same(m,epsi):
    sub_cnt = 0
    for i in range(1, (len(m)-4)): # len(m)-4):
        if(float(m[i+2-sub_cnt][1]) <= 0.0000001):
            #m=np.delete(m,i-sub_cnt+1,0)
            #sub_cnt = sub_cnt + 1
            m[i-sub_cnt+2][1] = 0

        if((float(m[i-sub_cnt][1])-epsi <= float(m[i-sub_cnt+1][1])) and (float(m[i-sub_cnt][1])+epsi >= float(m[i-sub_cnt+1][1]))):
            if(m[i-sub_cnt][1] == m[i-sub_cnt+2][1]):
                #print(i, m[i][1])
                m=np.delete(m,i-sub_cnt+1,0)
                sub_cnt = sub_cnt + 1
            elif(m[i-sub_cnt][1] == m[i-sub_cnt+3][1]):
                m=np.delete(m,i-sub_cnt+1,0)
                sub_cnt = sub_cnt + 1
    return m

x,y = readMyFile(wdif)
open(wdof, 'w').close

#print(x)
#print(float(y[1]))

matrix = []
matrix.append([x[0],y[0]])

for i in range(1,len(x)):
    matrix.append([float(x[i]),float(y[i])])

m = []
m = clear_same(matrix,epsi)
writeData(m,wdof)
