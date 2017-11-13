from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import urllib
import csv
import numpy as np
import tensorflow as tf
import codecs
import xlrd

SENSORDATA_TRAINING = "/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/test_30_ML_kalman_10_overlap.csv"
SENSORDATA_TEST = "/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/Feature_testsample4_30_overlap_10.csv"

#Function: Convert string to float
def floatify(x):
    try:
        return float(x)
    except ValueError:
        return x

def main():
	
	# Load datasets.
	training_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=SENSORDATA_TRAINING,
      target_dtype=np.int,
      features_dtype=np.float64)
  	test_set = tf.contrib.learn.datasets.base.load_csv_with_header(
      filename=SENSORDATA_TEST,
      target_dtype=np.int,
      features_dtype=np.float64)

  	# Specify that all features have real-value data
	feature_columns = [tf.feature_column.numeric_column("x", shape=[36])]

	# Build 3 layer DNN with 10, 20, 10 units respectively.
	classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                        hidden_units=[20],
                                        n_classes=10,
                                        model_dir="/tmp/dnn_model")

	# Define the training inputs
	train_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": np.array(training_set.data)},
    y=np.array(training_set.target),
    num_epochs=None,
    shuffle=True)

    # Train model.
	classifier.train(input_fn=train_input_fn, steps=2000)

	# Define the test inputs
	test_input_fn = tf.estimator.inputs.numpy_input_fn(
    x={"x": np.array(test_set.data)},
    y=np.array(test_set.target),
    num_epochs=1,
    shuffle=False)

	# Evaluate accuracy.
	accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]

	print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

	# Classify two new flower samples.

	file_loc = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/Feature_testsample4_30_overlap_10.xlsx'
	book = xlrd.open_workbook(file_loc)
	sheet = book.sheet_by_name('Sheet1')
	testdata = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(1,sheet.nrows)]
	testdata[0]
	data = [[floatify(x) for x in row] for row in testdata]
	new_samples = np.array(data)

	predict_input_fn = tf.estimator.inputs.numpy_input_fn(
	    x={"x": new_samples},
	    num_epochs=1,
	    shuffle=False)

	predictions = list(classifier.predict(input_fn=predict_input_fn))
	predicted_classes = [p["class_ids"] for p in predictions]

	print(predicted_classes)

if __name__ == "__main__":
    main()