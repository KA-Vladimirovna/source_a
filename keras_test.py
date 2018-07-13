import keras
from keras.layers import *
from keras.losses import *
from keras.optimizers import *
from keras.models import *
from keras.metrics import *

import numpy as np

model = Sequential()

model.add(GRU(16, input_shape=(None, 256)))
model.add(Dense(2, activation='softmax'))

model.compile(optimizer=RMSprop(), loss=categorical_crossentropy, metrics=[categorical_accuracy])

model.summary()

model.fit_generator()
