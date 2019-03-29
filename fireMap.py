import time
import main


class FireMap():

    def __init__ (self, main, x, y):
        self.main = main
        self.width = x
        self.height = y

        print("Creating Map with dimensions %d/%d" % (self.width, self.height))
        millis = time.time()

        self.data = [0] * (self.width * self.height)

        print("Map created in %.3f seconds" % (time.time() - millis))

    def getPoint(self, x, y):
        return self.data[y * self.width + y]

    def getTime(self, x, y):
        return self.main.time - getPoint(x, y)
