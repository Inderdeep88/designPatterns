class Door:
    def unlock(self):
        print("Door unlocked")
    def lock(self):
        print("Door locked")

class Engine:
    def start(self):
        print("Engine started")

    def stop(self):
        print("Engine stopped")

class Gear:
    level=0
    cruiseEnabled=False

    def shiftUp(self):
        self.level = self.level+1
        print("Gear shift UP - ", self.level)

    def shiftDown(self):
        self.level = self.level-1
        if self.level==0:
            print("Gear shift Down - NEUTRAL")
        else:
            print("Gear shift Down - ", self.level)

    def cruiseOn(self):
        if ( self.cruiseEnabled == True ):
            print("Cruise control already Enabled")
        elif( self.level != 4 ):
            print("Cruise control Cannot be Enabled")
        else:
            self.cruiseEnabled = True
            print("Cruise control ON")

    def cruiseOff(self):
        if( self.cruiseEnabled == False ):
            print("Cruise control already OFF")
        else:
            self.cruiseEnabled = False
            print("Cruise control OFF")

class HandBreak:
    def release(self):
        print("Handbreak released")

    def pull(self):
        print("Handbreak pulled")

class Light:
    def switchOn(self):
        print("Head Lights ON")

    def switchOff(self):
        print("Head Lights OFF")


class AirConditioner:
    temp = 25
    def switchOn(self):
        self.temp = 20
        print("AC ON, temperature : ", self.temp)

    def switchOff(self):
        self.temp = 25
        print("AC OFF, temperature : ", self.temp)

class SeatBelt:
    def fasten(self):
        print("Seatbelt Fastened")

    def open(self):
        print("Seatbelt opened")
