
# import formatter
# import predicter

# import formatter as form
from classes import formatter
from classes import predicter


# Mediator class (only point where the model can be called)


class Mediator:

    # Process the request for car brand guess
    # <param path> Path to the image
    @staticmethod
    def processUserInput(path):
        # Call the image formatter
        f = formatter.Formatter(path, "jpg")
        # Return the model prediction
        return predicter.Predicter.predict(f.getImage(), 1, 1)
