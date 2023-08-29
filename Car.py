class Auto:
    
    def __init__(self, make, model, year, color, engine):

        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.engine = engine
        print (make, model, year, color, engine)
    
    def drive(self):
        print("this car is in motion")

    def stop(self):
        print("this car is immobilized")


car = Auto ("Honda", "CIVIC", 2000, "BLUE", "inline")
car.drive()



