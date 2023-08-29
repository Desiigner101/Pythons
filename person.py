class Person:

    def __init__(self, age, name, gender, height, course): 
        
        self.age = age
        self.name = name
        self.gender = gender
        self.height = height
        self.course = course
        print (age, name, gender, height, course)

    def introduce(self):
        print ("Hi! below are my details to let you know who i am")

    def exit_out(self):
        print("that's all thank you")

x = Person("gino", "18 ", "SDSDD", "DSDD", "SDS")
x.introduce()
