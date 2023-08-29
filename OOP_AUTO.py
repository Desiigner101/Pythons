from Car import Auto

car_1 = Auto("HONDA", "CIVIC", 2000, "BLUE", "V8")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print(car_1.engine)

car_1.drive()
car_1.stop()

#----------------------------------------------------------------------------------------------------------

from person import Person

human = Person ("19", "Gino Sarsonas", "Male", 177.75, \
                "Bachelor of Science In Information Technology")

print  (human.age)
print  (human.name)
print  (human.gender)
print  (human.height)
print  (human.course)

human.introduce()