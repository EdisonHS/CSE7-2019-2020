class Car(object):
    def __init__(self, color):
        self.engineOn = False
        self.color = color

    def turn_on_car(self):
        self.engineOn = True

    def drive_forward(self):
        if not self.engineOn:
            print("The Engine is off.")
        else:
            print("You drive forward")

myCar = Car("Blue")
yourCar = Car("Black")

myCar.turn_on_car()
myCar.drive_forward()
myCar.drive_forward()
myCar.drive_forward()
yourCar.drive_forward()