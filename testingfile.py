import calendar

yy = 2023
mm = 8
print (calendar.month(yy,mm))

# OOP BASIC

class profile:

    def __init__(self, name, age, sy, course):
        self.name = name
        self.age = age
        self.sy = sy
        self.course = course

    def introduce_campus (self):
        print ("My campus is in Cebu Institute of Technology - University")

class student (profile):

    def __init__(self, name, age, sy, course, favorite):
        super().__init__(name, age, sy, course)
        self.favorite = favorite

    def introduce (self):
        print (f"Hi i am {self.name}, as of now i am {self.age} years old and i am in my {self.sy} and im also taking {self.course}.")

    def fave (self):
        print (f"My favorite major as of now is {self.favorite}")


p1 = profile ("Gino Sarsonas", 19, "Freshman year", "BSIT")
p1.introduce_campus()

p2 = student ("Gino Sarsonas", 19, "Freshman year", "BSIT", "Fundamentals of Programming")
p2.introduce()

# OOP intermediate

class student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name (self):
        return self.name
    
    def get_age (self):
        return self.age
    
    def get_grade (self):
        return self.grade
    
class Course:

    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.is_active = False

    def add_student(self,student):

        if len(self.students) < self.max_students:
         self.students.append(student)
         return True
        return False
    
    def get_average_grade (self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len (self.students)
    
s1 = student ("Gino", 19, 4.5) 
s2 = student ("Cesario", 21, 4.0)
s3 = student ("ashley", 18, 4.6)
s4 = student ("geund", 18, 4.4)
s5 = student ("khailla", 18, 4.3)
s6 = student ("lyca", 18, 4.6)
s7 = student ("Kervin", 19, 4.8)
       
course = Course ("Fundamentals of Programming", 6)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)
course.add_student(s5)
course.add_student(s6)
course.add_student(s7)
print (course.get_average_grade())  
