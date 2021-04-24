from classes.formatter import Formatter
from classes.predicter import Predicter

# Mediator class (only point where the model can be called)
class Mediator:

    # Process the request for car brand guess
    # <param path> Path to the image
    @staticmethod
    def processUserInput(path):
        # Call the image formatter
        f = Formatter(path, "jpg")
        # Return the model prediction
        return Predicter.predict(f.getImage(), 1, 1)