import numpy as np
from keras.utils import np_utils
from keras.models import load_model
import sys
# from sklearn import metrics

# define params
h5_model = sys.argv[1]
test_file = sys.argv[2]
file_out = sys.argv[3]
window_sizes = 17
threshold = 0.149
# load testing dataset
ds = np.loadtxt(test_file, ndmin=2, delimiter=",")
X1 = ds[:, 0:window_sizes * 20].reshape(len(ds), window_sizes, 20, 1)
# Y1 = ds[:, window_sizes * 20]
# true_labels = numpy.asarray(Y1)

loaded_model = load_model(h5_model)

# write out the prediction results
predictions = loaded_model.predict(X1)
for i in range(len(predictions)):
    # print(predictions[i])
    if predictions[i][0] >= threshold:
        predictions[i] = np.array([1, 0])
    else:
        predictions[i] = np.array([0, 1])
predictions = np.argmax(predictions, axis=1)
print(predictions)

f = open(file_out, 'w')
for x in predictions:
    f.write(str(x))
f.close()
