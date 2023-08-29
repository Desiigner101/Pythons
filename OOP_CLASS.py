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

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False 

    def get_average_grade(self):
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
       
course = Course ("Fundamentals of Programming", 6)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)
course.add_student(s5)
course.add_student(s6)
print (course.get_average_grade())

 