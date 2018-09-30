from keras import Model, Sequential
from keras.applications import InceptionV3,VGG19
from keras.layers import Flatten, Dense,GlobalAveragePooling2D
from keras.preprocessing import image
from sklearn.model_selection import train_test_split
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import  pandas as pd
import os
import zipfile
from subprocess import check_output
from keras.models import load_model
from skimage.io import imread
train_dir = '../input/dataset3/train'
test_data1=open("../input/dataset1/submit.txt").readlines()
# print(test_data1)
# print(os.listdir("../input/dataset-test/dataseta_test/DatasetA_test"))
test_data2=open("../input/dataset-test/dataseta_test/DatasetA_test/image.txt").readlines()
l=len(test_data1)+len(test_data2)
print(os.listdir("../input/dataset2/test/test"))
data_test_x=np.zeros((l,64,64,3))
for index,i in enumerate(test_data1):
    temp=i.split('\t')[0]
    img=image.load_img("../input/dataset2/test/test/"+temp)
    data_test_x[index]=image.img_to_array(img)
rt=len(test_data1)
for index,i in enumerate(test_data2):
    i=i.strip('\n')
    img=image.load_img("../input/dataset-test/dataseta_test/DatasetA_test/test/"+i)
    data_test_x[rt+index]=image.img_to_array(img)
# model1=load_model("../input/models/my_model_1.h5")
# model2=load_model("../input/models/my_model_2.h5")
# model3=load_model("../input/models/my_model_3.h5")
# model4=load_model("../input/models/my_model_4.h5")
#
# res1=model1.predict(data_test_x)
# res2=model2.predict(data_test_x)
# res3=model3.predict(data_test_x)
# res4=model4.predict(data_test_x)
# data_label=pd.read_csv('../input/dataset1/test_1.csv')
# print(res1)
# print("\n")
# print(res2)

df=pd.read_csv("E:/results/pre1.csv")
print(df[:,0:6])


# print(len(data_test_x))
# train_image_dir ="../input/dataset3/train/train/"
# datagen = ImageDataGenerator(
#         rotation_range=40,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         fill_mode='nearest')
# img_width, img_height = 64, 64
# train_data=open("../input/dataset1/train.txt").readlines()
# train_=[]
# target_=[]
# for i in train_data:
#     train_.append(i.strip('\n').split('\t')[0])
#     target_.append(i.strip('\n').split('\t')[1])
# X_train,X_test,y_train,y_test=train_test_split(train_,target_,test_size=0.3)

# top_model_weights_path = 'bottleneck_fc_model.h5'
# train_data_dir = 'E:/DatasetA/train'
# validation_data_dir = 'E:/DatasetA/train'

# epochs = 50
# batch_size = 16

# base_model=VGG19(include_top=False,weights=None, input_shape=(64, 64, 3))

# x=base_model.output
# x = GlobalAveragePooling2D()(x)
# x=Dense(1024,activation='relu')(x)
# predictions_1=Dense(7,activation='softmax')(x)
# model_1=Model(inputs=base_model.input,outputs=predictions_1)
# for layer in base_model.layers:
#     layer.trainable=False
# model_1.compile(optimizer='rmsprop',loss='categorical_crossentropy')
# model_1.summary()

# data_label=pd.read_csv('../input/dataset1/test_1.csv')
# data_label=data_label.set_index('0')
# length=len(train_)
# train_x=np.zeros((length,64,64,3))
# train_y=np.zeros((length,25))
# for index,name in enumerate(train_):
#     rgb_path = os.path.join(train_image_dir, name)
#     img = imread(rgb_path)
#     train_x[index]=image.img_to_array(img)
#     train_y[index]=data_label.loc[target_[index]]


# base_model=VGG19(include_top=False,weights=None, input_shape=(64, 64, 3))
# class_obj=7
# x=base_model.output
# x=GlobalAveragePooling2D()(x)
# x=Dense(1024,activation='relu')(x)
# predictions_1=Dense(7,activation='softmax')(x)
# model_1=Model(inputs=base_model.input,outputs=predictions_1)
# for layer in base_model.layers:
#     layer.trainable=False
# model_1.compile(optimizer='rmsprop',loss='categorical_crossentropy')
# model_1.summary()
# h=model_1.fit(train_x,train_y[:,:7],epochs=50,validation_split=0.2)
# model_1.save('my_model_1.h5')

# base_model=VGG19(include_top=False,weights=None, input_shape=(64, 64, 3))
# x=base_model.output
# x = GlobalAveragePooling2D()(x)
# x=Dense(1024,activation='relu')(x)
# predictions_1=Dense(8,activation='softmax')(x)
# model_1=Model(inputs=base_model.input,outputs=predictions_1)
# for layer in base_model.layers:
#     layer.trainable=False
# model_1.compile(optimizer='rmsprop',loss='categorical_crossentropy')
# model_1.summary()
# h=model_1.fit(train_x,train_y[:,7:15],epochs=50,validation_split=0.2)
# model_1.save('my_model_2.h5')

# base_model=VGG19(include_top=False,weights=None, input_shape=(64, 64, 3))
# x=base_model.output
# x = GlobalAveragePooling2D()(x)
# x=Dense(1024,activation='relu')(x)
# predictions_1=Dense(4,activation='softmax')(x)
# model_1=Model(inputs=base_model.input,outputs=predictions_1)
# for layer in base_model.layers:
#     layer.trainable=False
# model_1.compile(optimizer='rmsprop',loss='categorical_crossentropy')
# model_1.summary()
# h=model_1.fit(train_x,train_y[:,15:19],epochs=50,validation_split=0.2)
# model_1.save('my_model_3.h5')

# base_model=VGG19(include_top=False,weights=None, input_shape=(64, 64, 3))
# x=base_model.output
# x = GlobalAveragePooling2D()(x)
# x=Dense(1024,activation='relu')(x)
# predictions_1=Dense(6,activation='softmax')(x)
# model_1=Model(inputs=base_model.input,outputs=predictions_1)
# for layer in base_model.layers:
#     layer.trainable=False
# model_1.compile(optimizer='rmsprop',loss='categorical_crossentropy')
# model_1.summary()
# h=model_1.fit(train_x,train_y[:,19:],epochs=50,validation_split=0.2)
# model_1.save('my_model_4.h5')


