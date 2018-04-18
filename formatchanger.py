# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:26:30 2016

@author: Yang
"""
import os
# os.chdir("E:\\YANG\\Semeter 3\\NAD Binder")
from os import listdir
from os.path import isfile, join
import sys
from pathlib import Path

input_file = sys.argv[1]
output_file = sys.argv[2]

# change from LIBSVM format to CSV
# định dạng của libsvm là
# classtype số_thứ_tự_feature1:data1 số_thứ_tự_feature2:data2,...
# cần đổi sang định dạng của csv
# định dạng của file csv là data1,data2,....,data_n,classtype


def removeExsitingfile(name):
    if(Path(name)).is_file():
        os.remove(name)

# def libsvmToCsv(scrFolder,desFolder):


def libsvmToCsv(filename, OutputFile):
    #onlyfiles = [f for f in listdir(scrFolder) if isfile(join(scrFolder, f))]
    # for filename in onlyfiles:
    print(filename + " is processing")
    f1 = open(filename, "r")
    f2 = open(OutputFile, "a")  # thay đuôi libsvm thành csv
    lines = f1.readlines()
    for line in lines:
        classtype = line[0]  # lấy giá trị class
        line = line[1:-1]  # ko lấy class vì đã lưu ở trên rồi, ko lấy enter
        values = line.split()

        # ghi thông tin lên file đích
        for pair in values:
            colonPosition = pair.find(":")
            valueToWriteToFile = pair[colonPosition + 1:]
            f2.write(valueToWriteToFile + ", ")
        # ghi giá trị class ở cuối dòng
        f2.write(classtype)
        f2.write("\n")  # hết 1 dòng thì xuống hàng
    f1.close()
    f2.close()


removeExsitingfile(output_file)
libsvmToCsv(input_file, output_file)
