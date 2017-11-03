import shutil
import glob
import csv
import numpy as np
import time
import os
import sys

input_pssm = sys.argv[1]
output_data = sys.argv[2]

start_time = time.time()
aminoAcid = ['A','R','N','D','C', 'Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
outputTXT= ''
print('generate PSSM feature, please wait ...')
reader = csv.reader(open(input_pssm), delimiter = '\t')
data = []
for row in reader:
    for col in row:
        rgb = col.split()
        data += [[str(x) for x in rgb]]
pssmOptimize = data[2:len(data)-5]
sequenceLength = int(pssmOptimize[len(pssmOptimize)-1][0])
result1 = []
result = []
for char in aminoAcid:
    for row in pssmOptimize:
        if(row[1] == char):
            result.append([round(float(x)/sequenceLength,6) for x in row[2:22]])
        else:
            result.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

    result1.append(np.sum(result, axis = 0))
result2 = np.array(result1, dtype=object)
for item in result2.flatten():
    outputTXT += str(item) + ','
outputTXT += '0'  + '\n'

f = open(output_data, 'w')
f.write(outputTXT)
f.close()
print("--- generating finished ---")
print("--- %s seconds ---" % (time.time() - start_time))
