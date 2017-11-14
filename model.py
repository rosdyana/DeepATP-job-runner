# from __future__ import division
# import os
# #from keras.models import load_model
# import pandas as pd
# import sys
#
# input_file = sys.argv[1]
# output_file = sys.argv[2]
#
# # model = load_model('model.h5')
# # print("Loaded model from disk")
# #
# # data_input = pd.read_csv(input_file)
#
# # -*- coding: utf-8 -*-
# """
# Created on Wed Oct  4 15:59:06 2017
#
# @author: Yang
# """
#
#
#
#
# # convert data in libsvm with any range into range [0,1]
# def change(inputFile, outputFile):
#     f = open(inputFile, "r")
#     print("file ", inputFile, " is processing")
#     lines = f.readlines()
#
#     # đoạn này để tìm max, min
#     valueList = []
#     for line in lines:
#         pairs = line[1:-1].split(" ")  # pairs là 1 list
#         # bỏ đi các phần tử trắng
#         pairs = list(filter(lambda x: x != '', pairs))
#         for pair in pairs:
#             #            print("pair : ",pair) #đã test ok
#             pos = pair.find(":")
# #            valueStr=pair[pos+1:]
# #            print("value after : ",valueStr) #đã test ok
#             value = int(pair[pos + 1:])
#             valueList.append(value)
#
#     maxValue = max(valueList)
#     minValue = min(valueList)
#     f.close()
#
#     # tiếp tục đọc lại file, vừa đọc, vừa convert vừa ghi qua file output
#     f = open(inputFile, "r")
#     lines = f.readlines()
#     f2 = open(outputFile, "a")
#     for line in lines:
#         classType = line[0]
#         f2.write(classType + " ")
#         numberOfFeature = 1
#
#         pairs = line[1:-1].split(" ")  # pairs là 1 list
# #        print("pairs: ", pairs) #đá test ok
#         pairs = list(filter(lambda x: x != '', pairs))
#         for pair in pairs:
#             f2.write(str(numberOfFeature) + ":")
#             numberOfFeature = numberOfFeature + 1
#             pos = pair.find(":")
#             value = int(pair[pos + 1:])
#             changedValue = "{:6.4f}".format(
#                 abs(value - minValue) / abs(maxValue - minValue))
#             f2.write(str(changedValue) + " ")
#         f2.write("\n")
#     f2.close()
#     f.close()
#
# change(input_file,output_file)
import numpy
from keras.utils import np_utils
from keras.models import load_model
import sys
import pandas as pd

def dataPreprocessing(dataFile,windowsize):
    #data pre-processing
    data = pd.read_csv(dataFile,header=None)
    X = data.iloc[:, 0:windowsize*20].values
    #y = data.iloc[:, windowsize*20].values
    X=X.reshape(len(X),windowsize,20,1)
    #changeLabel(y)
    return X#, y
#define params
#json_model = sys.argv[1]
h5_model = sys.argv[1]
test_file = sys.argv[2]
file_out = sys.argv[3]

# load testing dataset
X1 = dataPreprocessing(test_file, 19)

# load model
loaded_model = load_model(h5_model)
print("Loaded model from disk.")

predictions = loaded_model.predict(X1)
output = predictions#np_utils.categorical_probas_to_classes(predictions)
f = open(file_out,'w')
for x in output:
    f.write(str(x) + '\n')
f.close()
print("Result saved.")
