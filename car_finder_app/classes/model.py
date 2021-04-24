import tensorflow as tf

# Singleton Class model (to instantiate the tensorflow model only one time)
class Model:
    # Path to the model
    __path = ""
    # Prediction model
    __model = None

    # Constructor (instanciate the model, should normally be private but it's Python for you)
    @staticmethod
    def __init__(path):
        Model.__path = path
        Model.__model = tf.keras.models.load_model(path)

    # If the model is already instanciated return the model
    # Else instanciate it with the constructor and return it 
    @staticmethod
    def getModel(path):
        if (Model.__model == None):
            Model.__init__(path)
        return Model.__model