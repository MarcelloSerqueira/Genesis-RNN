#07/12/2018
import numpy as np
import pandas as pd

def csv_to_numpy_array(train_path, test_path):
	print("loading training data...")
	traindata = pd.read_csv(train_path, header= None, sep=',').values
	#traindata = np.genfromtxt(train_path, dtype=None)
	
	print("loading test data...")
	testdata = pd.read_csv(test_path, header= None, sep=',').values
	
	#testdata = np.genfromtxt(test_path, dtype=None)

	return transform_data(traindata, testdata)

def transform_data(x_train, x_test):
	[trainX, trainY] = np.hsplit(x_train,[x_train.shape[1]-1])
	num_classes = len(np.unique(trainY))
	
	trainY = np.int_(trainY.reshape(-1))
	trainY = np.eye(num_classes)[trainY] #one hot vector
	#print('\n', 'training data loaded successfully!')

	[testX, testY] = np.hsplit(x_test,[x_test.shape[1]-1])
	testY = np.int_(testY.reshape(-1))
	testY = np.eye(num_classes)[testY] #one hot vector
	#print('test data loaded successfully!', '\n')

	return trainX, trainY, testX, testY, num_classes
