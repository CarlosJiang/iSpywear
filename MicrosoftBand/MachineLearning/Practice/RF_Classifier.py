#Required Python packages
import numpy as np
from sklearn import preprocessing, model_selection, cross_validation, neighbors, svm
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import time
from sklearn.externals import joblib

# File paths
file_loc = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/test_30_ML_kalman_10_overlap.xlsx'
 
def main():
	#Load public data set
	train = pd.read_excel(file_loc ,index_col=None, na_values=['NA'], parse_cols = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36])

	cols = ['Ax_iqr','Ax_max','Ax_mean','Ax_min','Ax_std','Ax_var','Ay_iqr','Ay_max','Ay_mean','Ay_min','Ay_std','Ay_var','Az_iqr','Az_max','Az_mean','Az_min','Az_std','Az_var',
            'Gx_iqr','Gx_max','Gx_mean','Gx_min','Gx_std','Gx_var','Gy_iqr','Gy_max','Gy_mean','Gy_min','Gy_std','Gy_var','Gz_iqr','Gz_max','Gz_mean','Gz_min','Gz_std','Gz_var']
	colsRes = ['Label']
	trainArr = train.as_matrix(cols) 
	trainRes = train.as_matrix(colsRes) 

	#Split train test data sets
	print 'Spliting training and testing data sets......'
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(trainArr, trainRes, test_size=0.2)


	#Training Random Forest classifier
	print 'Training.......'
	rf = RandomForestClassifier(n_estimators=100) 
	rf.fit(X_train, y_train) 

	#Save trained model
	print 'Saving Model......'
	joblib.dump(rf, 'Trained_Model_RF.pkl') 


	#Start prediction
	predictions = rf.predict(X_test)
	

	# Evaluation
	print 'Testing.......'
	accuracy = rf.score(X_test, y_test)
	print 'Accuracy : ', accuracy

	f1score = f1_score(y_test, predictions, average='macro')
	print 'F1 Score : ', f1score 


if __name__ == "__main__":
	start_time = time.time()
	main()
	print("--- %s seconds ---" % (time.time() - start_time))
