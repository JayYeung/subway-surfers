import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from util.my_utils import ACTIONS

def create_cnn_model(input_shape, num_actions):
    model = Sequential([
        Conv2D(32, (8, 8), strides=(4, 4), activation='relu', input_shape=input_shape),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (4, 4), strides=(2, 2), activation='relu'),
        MaxPooling2D(pool_size=(2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(num_actions, activation='softmax')
    ])
    return model

input_shape = (310, 570, 3)
num_actions = len(ACTIONS)  

cnn_model = create_cnn_model(input_shape, num_actions)

