import pandas as pd
import numpy as np
from keras.preprocessing import image
from .models import Inception_v3,DenseNet
data_atten = pd.read_csv('test.csv')
data_atten = data_atten.set_index('0')
data_train = open('data/DatasetB/train.txt')
data_train = data_train.readlines()
path = 'data/DatasetB/train/'
length = len(data_train)
train_x = np.zeros((length, 64, 64, 3))
train_y = np.zeros((length, 25))
for i in range(length):
    m, n = data_train[i].split()
    img = image.load_img(path + m)
    train_x[i] = image.img_to_array(img)
    train_y[i] = data_atten.loc[n]

# np.save('abc.npy', train_x)
# train_x = np.load('abc.npy')
h = Inception_v3.model.fit(train_x, {'cla': train_y[:, :7], 'has': train_y[:, 15:19], 'for': train_y[:, 19:25]}, epochs=50,
              validation_split=0.2)

