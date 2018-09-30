import numpy as np

f = open('../../../data/DatasetB/attributes_per_class.txt')
data_per_class = f.readlines()

data = []
head = list(['lable',
    'animal',
'transportation',
'clothes',
'plant',
'tableware',
'device',
'black',
'white',
'blue',
'brown',
'orange',
'red',
'green',
'yellow',
'has_feathers',
'has_four_legs',
'has_two_legs',
'has_two_arms',
'for_entertainment',
'for_business',
'for_communication',
'for_family',
'for_office use',
'for_personal',
'gorgeous',
'simple',
'elegant',
'cute',
'pure',
'naive'])
for line in data_per_class:
    data.append(line.split())
print(data)
import pandas as pd

data = pd.DataFrame(data, columns=head)
# data = data.set_index('lable')

data_1 = data.loc[:, 'animal':'device']
data_2 = data.loc[:, 'black':'yellow']
data_3 = data.loc[:, 'has_feathers':'has_two_arms']
data_4 = data.loc[:, 'for_entertainment':'for_personal']

data_1 = (data_1 >= '1') & 1
data_1['non_1'] = 1 - data_1.sum(axis=1)

data_2.sum(axis=1)

data_3 = (data_3 >= '1') & 1
data_3.sum(axis=1)

data_4 = (data_4 >= '1') & 1
data_4.sum(axis=1)

data_new = pd.DataFrame(data['lable'])
data_new = pd.DataFrame(np.hstack((data_new, data_1, data_2, data_3, data_4)))
data_new.to_csv("test_mid.csv", index=None)
