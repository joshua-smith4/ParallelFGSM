import os
import argparse

import tensorflow as tf
tf.enable_eager_execution()

from tensorflow import keras
import numpy as np
from keras.models import load_model
from keras.datasets import mnist

from cleverhans.attacks import FastGradientMethod
from cleverhans.utils_keras import KerasModelWrapper

parser = argparse.ArgumentParser()
parser.add_argument('-m','--modelfile', required=True)

args = parser.parse_args()

(x_train, y_train), (x_test, y_test) = mnist.load_data()

model_keras = load_model(args.modelfile)

score = model_keras.evaluate(x_test, y_test, verbose=0)
print('model test loss:', score[0])
print('model test accuracy:', score[1])

model_clever = KerasModelWrapper(model_keras)
fgsm = FastGradientMethod(model_clever)