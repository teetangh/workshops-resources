#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 21:35:19 2018

@author: rohans
"""


from keras.models import load_model #To save and load model

classifier = load_model('cnn_model_3l_drp_128size.h5')

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('dataset/single_prediction/download/both1.jpg', target_size = (128, 128))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)
#training_set.class_indices
if result[0][0] == 1:
    prediction = 'Dog'
else:
    prediction = 'Cat'

print(prediction)