import os
import math
from os.path import splitext
from datetime import datetime
import csv
import sys

# initializing required variables and its value
window_size = 17

# define params
input_file_testing = sys.argv[1]
output_file_testing = sys.argv[2]


def generate_dataset(input_file_name, output_file_name):
    # writting the output file
    fout = open(output_file_name, 'w')

    # get the filenames
    try:
        # read the pssm file
        f = open(input_file_name, 'r')
        f.readline()
        f.readline()
        f.readline()
        arr_pssm_line = f.readlines()
        f.close()
        # generate the content of the pssm feature values for current file
        generate_content(fout, input_file_name, arr_pssm_line)
    except Exception as inst:
        print("Error : ", inst)
        print("The entire file is ignored. Program terminated.")

    fout.close()


def generate_content(fout, input_pssm, arr_pssm_line):
    try:
        s = ''
        dx = int(window_size / 2)
        print('Generate PSSM feature, please wait ...')
        reader = csv.reader(open(input_pssm), delimiter='\t')
        data = []
        for row in reader:
            for col in row:
                rgb = col.split()
                data += [[str(x) for x in rgb]]
        pssmOptimize = data[2:len(data) - 5]
        seq_length = int(pssmOptimize[len(pssmOptimize) - 1][0])
        bottom = seq_length - 1 - dx

        for cur in range(seq_length):
            no = 1
            pad_top = dx - cur
            if pad_top < 0:
                pad_top = 0
            pad_bottom = cur - bottom
            if pad_bottom < 0:
                pad_bottom = 0

            # top padding
            for row in range(pad_top):
                for col in range(1, 21):
                    s += '0' + ','
                    no += 1

            # no padding (inside)
            for row in range(-dx + pad_top, dx - pad_bottom + 1):
                # get one line of pssm feature values
                token_pssm_line = arr_pssm_line[cur + row].split(None, 22)
                for col in range(20):
                    # scaled value
                    v = 1 / (1 + math.exp(-float(token_pssm_line[col + 2])))
                    s += str(v) + ','
                    # original value
                    #s += str(no) + ":" + str(token_pssm_line[col+2]) + " "
                    no += 1

            # bottom padding
            for row in range(pad_bottom):
                for col in range(1, 21):
                    s += '0' + ','
                    no += 1

            s += '0' + '\n'

        fout.write(s)
    except Exception as inst:
        print("Error : ", inst)
        print("The entire file is ignored. Program terminated.")


''' MAIN PROGRAM '''
generate_dataset(input_file_testing, output_file_testing)
