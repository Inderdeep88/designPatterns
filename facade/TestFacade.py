from facade.Component import Door, Engine, Light, SeatBelt, Gear, HandBreak, AirConditioner


class DriveCarFacade:
    door = Door()
    engine = Engine()
    lights = Light()
    seatBelt = SeatBelt()
    gear = Gear()
    handBreak = HandBreak()
    ac = AirConditioner()

    def cityDrive(self):
        print("\nGo for drive")
        self.door.unlock()
        self.seatBelt.fasten()
        self.engine.start()
        self.lights.switchOn()
        self.ac.switchOn()
        self.handBreak.release()
        for i in range(1,4):
            print("Wait for 1 min")
            self.gear.shiftUp()

    def cityPark(self):
        print("\nGo for parking")
        for i in range(1,4):
            print("Wait for 1 min")
            self.gear.shiftDown()
        self.handBreak.pull()
        self.ac.switchOff()
        self.lights.switchOff()
        self.engine.stop()
        self.seatBelt.open()
        self.door.lock()


    def highwayDrive(self):
        print("\nGo for drive")
        self.door.unlock()
        self.seatBelt.fasten()
        self.engine.start()
        self.lights.switchOn()
        self.ac.switchOn()
        self.handBreak.release()
        for i in range(1,5):
            print("Wait for 1 min")
            self.gear.shiftUp()
        self.gear.cruiseOn()

    def highwayPark(self):
        print("\nGo for parking")
        self.gear.cruiseOff()
        for i in range(1,5):
            print("Wait for 1 min")
            self.gear.shiftDown()
        self.handBreak.pull()
        self.ac.switchOff()
        self.lights.switchOff()
        self.engine.stop()
        self.seatBelt.open()
        self.door.lock()


def main():
    dcf = DriveCarFacade()

    print("On a weekday..\n")
    dcf.cityDrive()
    print("Short drive")
    dcf.cityPark()

    print("\n\nOn a weekend..\n")
    dcf.highwayDrive()
    print("Long drive")
    dcf.highwayPark()

if __name__ == "__main__":
    main()