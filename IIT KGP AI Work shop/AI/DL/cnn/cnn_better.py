# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:05:05 2018

@author: Rohan
"""

#Convolutional Neural Network

# Part 1 - Building the CNN

# Importing the Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout

from keras.models import load_model #To save and load model

# Initializing the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(filters = 32, kernel_size = 3, data_format = "channels_last", input_shape = (128, 128, 3), activation = 'relu'))

# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a 2nd convolutional layer
classifier.add(Convolution2D(filters = 32, kernel_size = 3, data_format = "channels_last", activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

# Adding a third convolutional layer
classifier.add(Convolution2D(filters = 64, kernel_size = 3, data_format = "channels_last", activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Step 3 - Flattening
classifier.add(Flatten())

# Step 4 - Full Connection
classifier.add(Dense(64, activation = 'relu'))
classifier.add(Dropout(0.5))
classifier.add(Dense(1, activation = 'sigmoid'))
# used activation function soft max for non binary output, and siqmoid for binary output

# Compiling the CNN
classifier.compile('adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
# for binary outcome choose loss function as binary cross entropy, and for non binary use categorical cross entropy

# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory('dataset/training_set',
                                                 target_size=(128, 128),
                                                 batch_size=32,
                                                 class_mode='binary')

test_set = test_datagen.flow_from_directory('dataset/test_set',
                                            target_size=(128, 128),
                                            batch_size=32,
                                            class_mode='binary')

classifier.fit_generator(training_set,
                         steps_per_epoch=8000/32,
                         epochs=90,
                         validation_data=test_set,
                         validation_steps=2000/32)

# Save the model
classifier.save('cnn_model_3l_drp_128size.h5')  # creates a HDF5 file 'my_model.h5'

# Part 3 - Making new predictions

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('dataset/single_prediction/cat_or_dog_1.jpg', target_size = (128, 128))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
training_set.class_indices
if result[0][0] == 1:
    prediction = 'Dog'
else:
    prediction = 'Cat'

