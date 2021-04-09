import cv2
import matplotlib.pyplot as plt

class Formatter:
    __path = ""
    __img = None
    __res = None

    # SUPPORT ONLY JPEG (JPG)
    def __init__(self, path, format):
        self.__path = path
        self.__img = plt.imread(self.__path, format=format)
        self.__res = cv2.resize(self.__img, dsize=(244, 244), interpolation=cv2.INTER_AREA)
        self.__res = self.__res.reshape((1, 244, 244, 3))

    def getImage(self):
        return self.__res