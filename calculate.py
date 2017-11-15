# -*- coding: utf-8 -*-
import os
import sys
import time
import csv

input_file = sys.argv[1]
win_size = int(sys.argv[2])
output_file = sys.argv[3]

start_time = time.time()
# AMINO = ["A", "R", "N", "D", "C", "Q", "E", "G", "H",
#          "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
#

def readPSSM(filename):
    aminoAcid = ['A','R','N','D','C', 'Q','E','G','H','I','L','K','M','F','P','S','T','W','Y','V']
    outputTXT= ''
    print('generate PSSM feature, please wait ...')
    reader = csv.reader(open(filename), delimiter = '\t')
    data = []
    for row in reader:
        for col in row:
            rgb = col.split()
            data += [[str(x) for x in rgb]]
    pssmOptimize = data[2:len(data)-5]
    sequenceLength = int(pssmOptimize[len(pssmOptimize)-1][0])
    return pssmOptimize


zero_padding = ['0', '0', '0', '0', '0', '0', '0', '0', '0',
                '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']


def generateDatasetWithWindowSize(pssmFile, windowSize, resultFile):
    print(pssmFile, " is processing")
    listOfList = readPSSM(pssmFile)
    listOfListWithZeroPadding = []

    numOfPadding = int((windowSize - 1) / 2)
    # zero padding at the beginning of pssm list of list
    for i in range(numOfPadding):
        listOfListWithZeroPadding.append(zero_padding)
    # next copy value after zero padding
    for l in listOfList:
        listOfListWithZeroPadding.append(l)
    # zero padding at the end of pssm list of list
    for i in range(numOfPadding):
        listOfListWithZeroPadding.append(zero_padding)

    f_result = open(resultFile, "a")
    length = len(listOfListWithZeroPadding)
    start = 0
    end = start + windowSize - 1
    i = 0
    print("length of pssm list ", length)
    cont = True
    while i < length and cont:
        listToWrite = []
        classType = ""
        for j in range(start, end + 1):
            #if j == (end - numOfPadding):
                #classType = ""
            for k in listOfListWithZeroPadding[j]:
                listToWrite.append(k)

        featureNum = 1
        f_result.write(classType + " ")
        for m in listToWrite:
            #f_result.write(str(featureNum) + ":" + str(m) + " ")
            f_result.write(str(featureNum) + ":" + str(m) + " ")
            featureNum = featureNum + 1
        f_result.write("\n")

        i = i + 1
        start = start + 1
        end = start + windowSize - 1
        if start >= length or end >= length:
            cont = False
    f_result.close()


generateDatasetWithWindowSize(input_file, win_size, output_file)

print("--- generating finished ---")
print("--- %s seconds ---" % (time.time() - start_time))
