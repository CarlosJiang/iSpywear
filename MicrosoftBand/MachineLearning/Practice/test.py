import pandas as pd
import numpy as np
from StringIO import StringIO
# file_loc = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/Wrist.xlsx'
# Ax_table = pd.read_excel(file_loc ,index_col=None, na_values=['NA'], parse_cols = [1])

# print Ax_table.head()

# file_loc = '/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/SensorDatatest.txt'
# Ax_table = pd.read_csv(file_loc, usecols=['Ax'])

# print Ax_table.head()

data = pd.read_excel('/Users/jianghe/Desktop/Mobile/iSpyWear2/MicrosoftBand/MachineLearning/DataSets/test.xlsx')
print data.info()