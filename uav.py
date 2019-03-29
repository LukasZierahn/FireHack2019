
from main import *


class UAV():

    def __init__(self, main, msg):
        self.main = main
        self.x = 0
        self.y = 0 #TODO: fill me with proper info

        if (msg.EntityType.decode("utf-8") == "FixedWing"):
            self.fixedWing = True
        elif (msg.EntityType.decode("utf-8") == "Multi"):
            self.fixedWing = False
        else:
            print("Undefined EntityType: " + msg.EntityType.decode("utf-8"))

        print("Created UAV with:\nFixedWing %s" % (self.fixedWing))
