from keras.datasets import fashion_mnist
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Dense, Flatten
from keras.utils import np_utils
from keras.optimizers import SGD
from keras.callbacks import TensorBoard
import random
import pickle

#Import wandb libraries
import wandb
from wandb.keras import WandbCallback

# Initialize wandb and save hyperparameters
wandb.init(
  project="asi-ml-autocarml",
  config={
    "dropout": 0.2,
    "hidden_layer_size": 128,
    "layer_1_size": 16,
    "layer_2_size": 32,
    "learn_rate": 0.01,
    "decay": 1e-6,
    "momentum": 0.9,
    "epochs": 8 }
)
config = wandb.config


##tutaj import podzielonych danych


# load modelu wyrzuconego wcześniej przez optimę
model = pickle.load(open("..\\data\\03_models\\optuna_best_lr_model.pkl", 'rb'))

#Add Keras WandbCallback
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(X_train, y_train,  validation_data=(X_test, y_test), epochs=config.epochs,
    callbacks=[WandbCallback(data_type="image", labels=labels)])
