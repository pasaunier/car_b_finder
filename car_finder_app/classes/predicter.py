import tensorflow as tf
import numpy as np

from classes.model import Model

# Predicter class (predict the car brand)


class Predicter:
    # All car brands available
    __nameconv = {0: 'AM General', 1: 'Acura', 2: 'Aston', 3: 'Audi',
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

    # Predict the car brand from preprocessed image
    @staticmethod
    def predict(img_processed, batch_size, verbose):
        # Get the model and predict the car brand of the image
        pred = (Model.getModel(r"models\sequential_custom.h5")).predict(
            img_processed, batch_size=batch_size, verbose=verbose)
        # Get the index of the car brand predicted
        indice_pred = np.argmax(pred, axis=1)
        # Return the car brand string associated with the index predicted
        return Predicter.__nameconv[indice_pred[0]]
