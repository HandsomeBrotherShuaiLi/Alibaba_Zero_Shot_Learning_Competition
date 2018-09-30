from keras.applications.inception_v3 import InceptionV3
from keras.preprocessing import image
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D,Flatten
from keras import backend as K

# create the base pre-trained model
base_model = InceptionV3(weights=None, include_top=False)
classes = {
    'cla' : 6+1,
   'clo' : 8,
    'has' : 4,
    'for' : 6,
   'is' : 6
}
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(200, activation='softmax')(x)
x = base_model.output
x = Flatten()(x)
x = Dense(1024, activation='relu')(x)
predictions = [Dense(n, activation='softmax', name=m)(x) for m, n in classes.items()]

model = Model(inputs=base_model.input, outputs=predictions)
model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
model.summary()