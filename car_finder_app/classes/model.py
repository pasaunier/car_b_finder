import tensorflow as tf

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