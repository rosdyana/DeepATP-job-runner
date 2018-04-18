# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:26:47 2017

@author: Yang
"""

import os
import sys
from pathlib import Path

AMINO = ["A", "R", "N", "D", "C", "Q", "E", "G", "H",
         "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V"]
# doc file PSSM, tra ve list of list theo thu tu


def removeExsitingfile(name):
    if(Path(name)).is_file():
        os.remove(name)


def readPSSM(filename):
    listOfList = []
    f = open(filename, "r")
    lines = f.readlines()[3:-6]
    for line in lines:
        # split by space
        temp = line[:-1].split(" ")
        # remove all ''
        temp = list(filter(lambda x: x != '', temp))
        # if temp[1] in AMINO:  #ban dau lam cai này de loai bo X nhung lam vay thi vi tri cac NAD bi lech
        listOfList.append(temp[2:22])
    return listOfList  # neu co NAD o vi tri 18 trong NAD position file thi no se nam o index 17 trong listOfList duoc tra ve


#l = readPSSM("1a7a_A.pssm")
# print(l)
# print(len(l))


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

    # generate dataset according to window size
    # chu y padding roi thi index thay doi
    length = len(listOfListWithZeroPadding)
    start = 0
    end = start + windowSize - 1
    i = 0
    print("length of pssm list ", length)
    cont = True
    while i < length and cont:  # duyet theo list cac dong pssm
        listToWrite = []
        #print("start ",start, " end ",end)
        classType = ""
        for j in range(start, end + 1):
            if j == (end - numOfPadding):  # xet dong chinh giữa
                classType = "0"
            for k in listOfListWithZeroPadding[j]:
                listToWrite.append(k)

        featureNum = 1
        # ghi du lieu ra file ket qua
        f_result.write(classType + " ")
        for m in listToWrite:
            f_result.write(str(featureNum) + ":" + str(m) + " ")
            featureNum = featureNum + 1
        f_result.write("\n")

        i = i + 1
        start = start + 1
        end = start + windowSize - 1
        if start >= length or end >= length:
            cont = False
    # Ket thuc vong lap while
    f_result.close()


pssmFile = sys.argv[1]
windowSize = 17
resultFile = sys.argv[2]
removeExsitingfile(resultFile)
print("Generate PSSM to Libsvm in progress")
generateDatasetWithWindowSize(pssmFile, windowSize, resultFile)
print("Generate PSSM to Libsvm finished")
