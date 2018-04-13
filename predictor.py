import numpy
from keras.utils import np_utils
from keras.models import load_model
import sys
from sklearn import metrics

# define params
h5_model = sys.argv[1]
test_file = sys.argv[2]
file_out = sys.argv[3]
window_sizes = 17

# load testing dataset
ds = numpy.loadtxt(test_file, ndmin=2, delimiter=",")
X1 = ds[:, 0:window_sizes * 20].reshape(len(ds), window_sizes, 20, 1)
Y1 = ds[:, window_sizes * 20]
true_labels = numpy.asarray(Y1)

loaded_model = load_model(h5_model)
print("Loaded model from disk.")

# write out the prediction results
predictions = loaded_model.predict_classes(X1)
print(predictions)

f = open(file_out, 'w')
for x in predictions:
    f.write(str(x))
f.close()
