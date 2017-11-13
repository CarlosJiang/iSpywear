import pandas as pd
import numpy as np
from sklearn.externals import joblib
import xlrd
from collections import Counter

#Function: Convert string to float
def floatify(x):
    try:
        return float(x)
    except ValueError:
        return x



#Load trained model
# rf = joblib.load('Trained_Model_SVM.pkl')
rf = joblib.load('Trained_Model_RF.pkl')
file_loc = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/Feature_testsample4_30_overlap_10.xlsx'
book = xlrd.open_workbook(file_loc)
sheet = book.sheet_by_name('Sheet1')
testdata = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(1,sheet.nrows)]
testdata[0]
data = [[floatify(x) for x in row] for row in testdata]

#Prediction of testing data
example_measures = np.array(data)
prediction = rf.predict(example_measures) 


print(prediction)
# print len(prediction)/5


# #Calculate weight of each number and get the PIN
# temp = 0
# password = []
# startPoint = 0
# dataRange = len(prediction)/5-1
# for a in range(5):
# 	endPoint = startPoint + dataRange
# 	for i in range(9):
# 		counter = list(prediction[startPoint:endPoint]).count(i)
# 		if(counter>temp):
# 			temp = counter
# 			result = i
# 	print prediction[startPoint:endPoint]
# 	startPoint = endPoint + 1		
# 	password.append(result)
# 	counter = 0
# 	temp = 0
# print password		





# #Load prediction data


# # Load data from dataset file
# df = pd.read_excel(file_loc)
# print df.head()


#Predicting
# example_measures = np.array([[0.0199463	,0.7272217	,0.02908677,	0.0037353,	-0.1006593,	0.01466623,	0.0005616,	0.6892334,	0.01821053,	-1.5365854,	1.8414634,	6.49530801,	-7.3140248,	9.4908542,	24.93736733,	1.8993903,	-3.2286589,	8.23270613],
# 							[0.0214599	,0.6959717,	0.05208644,	0.0058594,	-0.1076172,	0.02554898,	-0.0116944,	0.6960206,	0.03632646,	-1.2621952,	-0.7012196,	4.84276513,	1.0182927,	0.7804879,	4.51207577,	-0.4207317,	-1.8963417,	2.84442575],
# 							[-0.0061524	,0.7101074,	0.0384277,	0.0111817,-0.1225099,	0.03230276,	-0.0007079,	0.7135499,	0.02299682,	0.2621953,	-1.7073173,	6.81159289,	1.2987803,	1.3231709,	2.53757459,	-1.1097561,	-3.1829269,	4.11084164],
# 							[-0.0121093	,0.7097655,	0.06276647,	-0.0159668,	-0.1447266,	0.05346044,	0.0038086,	0.7122558,	0.03443472,	-3.2408538,	1.2957318,	6.59273335,	1.8993902,	1.807927,	3.73004428,	-4.573171,	-2.8963416,	7.98467431],
# 							[-0.0134034	,0.6885498,	0.02212194,	-0.0417726,	-0.112329,	0.05552033,	0.0223876,	0.6845458,	0.04209857,	0.9786586,	-1.362805,	11.12968638,	3.0396341,	-0.2591465,	4.60501628,	-2.7530488,	0.9786586,	10.33583788],
# 							[0.0034666	,0.6975586,	0.04678824,	-0.0094971,	-0.1345947,	0.0272301,	0.0078613,	0.7260255,	0.0416811,	2.5670733,	1.2195123,	5.58418108,	-0.6920731,	0.4420731,	5.19101342,	-1.3871952,	-1.1798782,	4.04654954],
# 							[0.0121583	,0.7085937,	0.02812193,	0.0053223,	-0.0983887,	0.0297601,	-0.0012939,	0.6908935,	0.03580404,	3.6402438,	-0.347561,	4.51349677,	1.1067074,	1.5335366,	4.44743935,	3.6250002,	-0.8140246,	4.9883874],
# 							[0.010962	,0.6903076,	0.02213956,	0.0123779,	-0.1135499,	0.0606004,	0.0004638,  0.7110106,	0.02179665,	-1.6768294,	-1.4146342,	6.00562105,	1.2103658,	2.1615854,	3.95534952,	-2.6158538,	-3.5914634,	9.59192876]])
# prediction = rf.predict(example_measures) 

#Print out result
# print(prediction)