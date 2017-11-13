import pandas as pd
import numpy as np
from math import sqrt

# Calculate Standard Deviation and Mean
def cal_StdandMean(matrix):
	
	meanset = []
	stdset = []
	iqrset = []
	maxset = []
	minset = []
	varset = []
	a = 0
	b = 30
	for i in range(a, len(matrix)-1, b):
		if i != 0:
			i = i - 10
		subset = []
		subset_iqr_1 = []
		subset_iqr_3 = []
		subset.extend(matrix[i])
		subset.extend(matrix[i+1])
		subset.extend(matrix[i+2])
		subset.extend(matrix[i+3])
		subset.extend(matrix[i+4])
		subset.extend(matrix[i+5])
		subset.extend(matrix[i+6])
		subset.extend(matrix[i+7])
		subset.extend(matrix[i+8])
		subset.extend(matrix[i+9])
		subset.extend(matrix[i+10])
		subset.extend(matrix[i+11])
		subset.extend(matrix[i+12])
		subset.extend(matrix[i+13])
		subset.extend(matrix[i+14])
		subset_iqr_1 = subset
		subset.extend(matrix[i+15])
		subset.extend(matrix[i+16])
		subset.extend(matrix[i+17])
		subset.extend(matrix[i+18])
		subset.extend(matrix[i+19])
		subset.extend(matrix[i+20])
		subset.extend(matrix[i+21])
		subset.extend(matrix[i+22])
		subset.extend(matrix[i+23])
		subset.extend(matrix[i+24])
		subset.extend(matrix[i+25])
		subset.extend(matrix[i+26])
		subset.extend(matrix[i+27])
		subset.extend(matrix[i+28])
		subset.extend(matrix[i+29])
		subset_iqr_3.extend(matrix[i+15])
		subset_iqr_3.extend(matrix[i+16])
		subset_iqr_3.extend(matrix[i+17])
		subset_iqr_3.extend(matrix[i+18])
		subset_iqr_3.extend(matrix[i+19])
		subset_iqr_3.extend(matrix[i+20])
		subset_iqr_3.extend(matrix[i+21])
		subset_iqr_3.extend(matrix[i+22])
		subset_iqr_3.extend(matrix[i+23])
		subset_iqr_3.extend(matrix[i+24])
		subset_iqr_3.extend(matrix[i+25])
		subset_iqr_3.extend(matrix[i+26])
		subset_iqr_3.extend(matrix[i+27])
		subset_iqr_3.extend(matrix[i+28])
		subset_iqr_3.extend(matrix[i+29])
		iqr = float("{0:.8f}".format(np.mean(subset_iqr_3) - np.mean(subset_iqr_1)))
		mean = float("{0:.8f}".format(np.mean(subset)))
		std = float("{0:.8f}".format(np.std(subset)))
		max = float("{0:.8f}".format(np.max(subset)))
		min = float("{0:.8f}".format(np.min(subset)))
		var = float("{0:.8f}".format(np.var(subset)))
		meanset.append(mean)
		stdset.append(std)
		iqrset.append(iqr)
		maxset.append(max)
		minset.append(min)
		varset.append(var)


	return meanset, stdset, iqrset, maxset, minset, varset

# File Paths
file_loc = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/SensorDatatestsample4-F.txt'

# Load data from dataset file
Ax_table = pd.read_csv(file_loc, usecols=['Ax'])
Ay_table = pd.read_csv(file_loc, usecols=['Ay'])
Az_table = pd.read_csv(file_loc, usecols=['Az'])
Gx_table = pd.read_csv(file_loc, usecols=['Gx'])
Gy_table = pd.read_csv(file_loc, usecols=['Gy'])
Gz_table = pd.read_csv(file_loc, usecols=['Gz'])

# Change data into matrix
matrix_Ax = Ax_table.as_matrix(['Ax'])
matrix_Ay = Ay_table.as_matrix(['Ay'])
matrix_Az = Az_table.as_matrix(['Az'])
matrix_Gx = Gx_table.as_matrix(['Gx'])
matrix_Gy = Gy_table.as_matrix(['Gy'])
matrix_Gz = Gz_table.as_matrix(['Gz'])


# Calculate std, mean and iqr for Ax,Ay,Az,Gx,Gy,Gz
mean_Ax, std_Ax, iqr_Ax, max_Ax, min_Ax, var_Ax = cal_StdandMean(matrix_Ax)
mean_Ay, std_Ay, iqr_Ay, max_Ay, min_Ay, var_Ay = cal_StdandMean(matrix_Ay)
mean_Az, std_Az, iqr_Az, max_Az, min_Az, var_Az = cal_StdandMean(matrix_Az)
mean_Gx, std_Gx, iqr_Gx, max_Gx, min_Gx, var_Gx = cal_StdandMean(matrix_Gx)
mean_Gy, std_Gy, iqr_Gy, max_Gy, min_Gy, var_Gy = cal_StdandMean(matrix_Gy)
mean_Gz, std_Gz, iqr_Gz, max_Gz, min_Gz, var_Gz = cal_StdandMean(matrix_Gz)

# Store results in df
df = pd.DataFrame({'Ax_mean': mean_Ax, 'Ay_mean': mean_Ay, 'Az_mean': mean_Az,
                   'Gx_mean': mean_Gx, 'Gy_mean': mean_Gy, 'Gz_mean': mean_Gz, 
                   'Ax_std': std_Ax, 'Ay_std': std_Ay, 'Az_std': std_Az,
                   'Gx_std': std_Gx, 'Gy_std': std_Gy, 'Gz_std': std_Gz,
                   'Ax_iqr': iqr_Ax, 'Ay_iqr': iqr_Ay, 'Az_iqr': iqr_Az,
                   'Gx_iqr': iqr_Gx, 'Gy_iqr': iqr_Gy, 'Gz_iqr': iqr_Gz,
                   'Ax_max': max_Ax, 'Ay_max': max_Ay, 'Az_max': max_Az,
                   'Gx_max': max_Gx, 'Gy_max': max_Gy, 'Gz_max': max_Gz,
                   'Ax_min': min_Ax, 'Ay_min': min_Ay, 'Az_min': min_Az,
                   'Gx_min': min_Gx, 'Gy_min': min_Gy, 'Gz_min': min_Gz,
                   'Ax_var': var_Ax, 'Ay_var': var_Ay, 'Az_var': var_Az,
                   'Gx_var': var_Gx, 'Gy_var': var_Gy, 'Gz_var': var_Gz})

# Write features into a new excel file
writer = pd.ExcelWriter('/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/SensorDatatestsample4-F.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False, float_format='%.8f')
writer.save()