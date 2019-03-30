
from main import *
from afrl.cmasi.searchai.HazardSensorConfiguration import HazardSensorConfiguration


class UAV():

    def __init__(self, main, msg):
        self.main = main
        self.ID = msg.ID
        self.x = 0
        self.y = 0
        self.sensorRange = -1
        self.status = None

        for payload in msg.PayloadConfigurationList:
            if isinstance(payload, HazardSensorConfiguration):
                self.sensorRange = payload.MaxRange

        if (msg.EntityType.decode("utf-8") == "FixedWing"):
            self.fixedWing = True
        elif (msg.EntityType.decode("utf-8") == "Multi"):
            self.fixedWing = False
        else:
            print("Undefined EntityType: " + msg.EntityType.decode("utf-8"))

        print("Created UAV with:\n\tID: %d\n\tSensorRange: %d\n\tFixedWing: %s\n" % (self.ID, self.sensorRange, self.fixedWing))

    def UpdateUAV(self, msg):
        self.x, self.y = self.main.fireMap.LocationToCoord(msg.Location)
        percieved = self.main.fireMap.CoordToLocation(self.x, self.y)
        print((percieved.Latitude, percieved.Longitude), (msg.Location.Latitude, msg.Location.Longitude))
        self.status = msg
