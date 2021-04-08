import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense

# Singleton pour obtenir le model entrainé qu'une seule fois
class Model:
    __path = ""
    __model = None

    @staticmethod
    def __init__(path):
        Model.__path = path
        Model.__model = tf.keras.models.load_model(path)

    @staticmethod
    def getModel(path):
        if (Model.__model == None):
            Model.__init__(path)
        return Model.__model