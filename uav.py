
from main import *


class UAV():

    def __init__(self, main, msg):
        self.main = main
        self.ID = msg.ID
        self.x = 0
        self.y = 0
        self.status = None

        if (msg.EntityType.decode("utf-8") == "FixedWing"):
            self.fixedWing = True
        elif (msg.EntityType.decode("utf-8") == "Multi"):
            self.fixedWing = False
        else:
            print("Undefined EntityType: " + msg.EntityType.decode("utf-8"))

        print("Created UAV with:\n\tID: %d\n\tFixedWing: %s\n" % (self.ID, self.fixedWing))

    def UpdateUAV(self, msg):
        self.x, self.y = self.main.fireMap.LocationToCoord(msg.Location)
        self.status = msg
