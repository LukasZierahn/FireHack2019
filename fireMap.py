import time
import main
from Helper import *
from math import *
from cmath import *
from afrl.cmasi.Location3D import Location3D

class FireMap():

    def __init__ (self, main, lmcpObject):
        self.main = main
        self.width = int(lmcpObject.Boundary.Width)
        self.height = int(lmcpObject.Boundary.Height)
        self.middleWidth = self.width / 2.0
        self.middleHeight = self.height / 2.0
        self.center = lmcpObject.Boundary.CenterPoint

        print("Creating Map with dimensions %d/%d" % (self.width, self.height))
        millis = time.time()

        self.data = [0] * (self.width * self.height)

        print("Map created in %.3f seconds" % (time.time() - millis))

    def HandleAirVehicleState(self, msg):
        pass
        #print(msg.Location)

    def LocationToCoord(self, location):
        d = distance((self.center.Latitude, self.center.Longitude), (location.Latitude, location.Longitude))
        angle = calculate_initial_compass_bearing((self.center.Latitude, self.center.Longitude), (location.Latitude, location.Longitude))

        offsetx = cos(angle) * d
        offsety = sin(angle) * d

        return self.middleWidth + offsetx, self.middleHeight + offsety

    def CoordToLocation(self, x, y):
        #source https://stackoverflow.com/questions/7222382/get-lat-long-given-current-point-distance-and-bearing/7835325
        #this is heavily modified though

        middle = complex(self.middleWidth, self.middleHeight)
        pos = complex(x, y)
        print(middle, pos)
        d, angle = polar(middle - pos)

        angle = (angle + pi/2.0) % 2*pi

        print(d, degrees(angle), angle)

        d = d / 1000.0
        R = 6378.1 #Radius of the Earth

        lat1 = math.radians(self.center.Latitude)
        lon1 = math.radians(self.center.Longitude)

        result = Location3D()

        result.Latitude = math.asin(math.sin(lat1)*math.cos(d/R) +
             math.cos(lat1)*math.sin(d/R)*math.cos(angle))

        result.Longitude = lon1 + math.atan2(math.sin(angle)*math.sin(d/R)*math.cos(lat1),
             math.cos(d/R)-math.sin(lat1)*math.sin(result.Latitude))

        return result


    def getPoint(self, x, y):
        return self.data[y * self.width + y]

    def getTime(self, x, y):
        return self.main.time - getPoint(x, y)

    def setPoint(self, x, y, value):
        self.data[y * self.width + y] = value
