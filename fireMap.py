import time
import main


class FireMap():

    def __init__ (self, main, lmcpObject):
        self.main = main
        self.width = int(lmcpObject.Boundary.Width)
        self.height = int(lmcpObject.Boundary.Height)
        self.center = lmcpObject.Boundary.CenterPoint

        print("Creating Map with dimensions %d/%d" % (self.width, self.height))
        millis = time.time()

        self.data = [0] * (self.width * self.height)

        print("Map created in %.3f seconds" % (time.time() - millis))

    def HandleAirVehicleState(self, msg):
        print(msg.Location)

    def LocationToCoord(self, location):
        pass

    def CoordToLocation(self, x, y):
        pass

    def getPoint(self, x, y):
        return self.data[y * self.width + y]

    def getTime(self, x, y):
        return self.main.time - getPoint(x, y)

    def setPoint(self, x, y, value):
        self.data[y * self.width + y] = value
