from classes.formatter import Formatter
from classes.predicter import Predicter

class Mediator:

    @staticmethod
    def processUserInput(path):
        f = Formatter(path, "jpg")
        return Predicter.predict(f.getImage(), 1, 1)