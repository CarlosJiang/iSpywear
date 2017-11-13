from __future__ import division
import pandas as pd
from scipy.spatial.distance import cosine
import numpy as np
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt



pd.set_option('display.float_format', lambda x: '%.3f' % x)
with open('/Users/jianghe/Desktop/Mobile/Datasets/HAPT Data Set/features.txt') as handle:
    features = handle.readlines()
    features = map(lambda x: x.strip(), features)

with open('/Users/jianghe/Desktop/Mobile/Datasets/HAPT Data Set/activity_labels.txt') as handle:
    activity_labels = handle.readlines()
    activity_labels = map(lambda x: x.strip(), activity_labels)

activity_df = pd.DataFrame(activity_labels)
activity_df = pd.DataFrame(activity_df[0].str.split(' ').tolist(),
                           columns = ['activity_id', 'activity_label'])
print activity_df

x_train = pd.read_table('/Users/jianghe/Desktop/Mobile/Datasets/HAPT Data Set/Train/X_train.txt',
             header = None, sep = " ", names = features)
print x_train.iloc[:10, :10].head()

y_train = pd.read_table('/Users/jianghe/Desktop/Mobile/Datasets/HAPT Data Set/Train/y_train.txt',
             header = None, sep = " ", names = ['activity_id'])
print y_train.head()

x_test = pd.read_table('/Users/jianghe/Desktop/Mobile/Datasets/HAPT Data Set/Test/X_test.txt',
             header = None, sep = " ", names = features)
y_test = pd.read_table('/Users/jianghe/Desktop/Mobile/Datasets/HAPT Data Set/Test/y_test.txt',
             header = None, sep = " ", names = ['activity_id'])