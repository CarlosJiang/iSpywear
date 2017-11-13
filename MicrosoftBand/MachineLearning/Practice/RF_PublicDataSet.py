#Required Python Packages
import numpy as np
from sklearn import preprocessing, model_selection, cross_validation, neighbors, svm
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import time

# File Paths
file_loc = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/S_Feature_test.xlsx'
 
def main():
	#Load public data set
	train = pd.read_excel(file_loc ,index_col=None, na_values=['NA'], parse_cols = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])

	cols = ['Ax_mean', 'Ax_std', 'Ay_mean', 'Ay_std', 'Az_mean', 'Az_std',
            'Gx_mean', 'Gx_std', 'Gy_mean', 'Gy_std', 'Gz_mean', 'Gz_std'] 
	colsRes = ['Label']
	trainArr = train.as_matrix(cols) 
	trainRes = train.as_matrix(colsRes) 

	#Split train test data sets
	print 'Spliting training and testing data sets......'
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(trainArr, trainRes, test_size=0.2)


	#Training Random Forest Classifier
	print 'Training.......'
	rf = RandomForestClassifier(n_estimators=10) 
	rf.fit(X_train, y_train) 
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
