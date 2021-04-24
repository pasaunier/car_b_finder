import cv2
import matplotlib.pyplot as plt

# Image formatter class (for preprocessing)
class Formatter:
    # Path to the image
    __path = ""
    # Image
    __img = None
    # Image preprocessed
    __res = None

    # Constructor : open and preprocess the image
    # SUPPORT ONLY JPEG AS FORMAT (format="jpg")
    def __init__(self, path, format):
        self.__path = path
        self.__img = plt.imread(self.__path, format=format)
        self.__res = cv2.resize(self.__img, dsize=(244, 244), interpolation=cv2.INTER_AREA)
        self.__res = self.__res.reshape((1, 244, 244, 3))

    # Function to return the preprocessed image
    def getImage(self):
        return self.__res