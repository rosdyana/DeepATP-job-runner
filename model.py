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
