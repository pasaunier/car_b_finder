import pandas as pd
import numpy as np
import cv2
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

import os

nameconv = {0: 'AM General', 1: 'Acura', 2: 'Aston', 3: 'Audi', 
             4: 'BMW', 5: 'Bentley', 6: 'Bugatti', 7: 'Buick', 
             8: 'Cadillac', 9: 'Chevrolet', 10: 'Chrysler', 
             11: 'Daewoo', 12: 'Dodge', 13: 'Eagle', 14: 'FIAT', 
             15: 'Ferrari', 16: 'Fisker', 17: 'Ford', 18: 'GMC', 
             19: 'Geo', 20: 'HUMMER', 21: 'Honda', 22: 'Hyundai', 
             23: 'Infiniti', 24: 'Isuzu', 25: 'Jaguar', 26: 'Jeep', 
             27: 'Lamborghini', 28: 'Land', 29: 'Lincoln', 30: 'MINI', 
             31: 'Maybach', 32: 'Mazda', 33: 'McLaren', 34: 'Mercedes-Benz', 
             35: 'Mitsubishi', 36: 'Nissan', 37: 'Plymouth', 38: 'Porsche', 
             39: 'Ram', 40: 'Rolls-Royce', 41: 'Scion', 42: 'Spyker', 
             43: 'Suzuki', 44: 'Tesla', 45: 'Toyota', 46: 'Volkswagen', 
             47: 'Volvo', 48: 'smart'}

model = tf.keras.models.load_model("overfit.h5")
model.summary()

img = plt.imread("img/audi.jpg", format="jpeg")
res = cv2.resize(img, dsize=(244, 244), interpolation=cv2.INTER_AREA)
res = res.reshape((1, 244, 244, 3))

pred = model.predict(res, batch_size=1, verbose=1)
indice_pred=np.argmax(pred,axis=1)

print("Result : ", nameconv[indice_pred[0]])