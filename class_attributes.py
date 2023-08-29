class person:
    number_of_people = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        person.add_person ()

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person (cls):
        cls.number_of_people += 1 
    
    
p1 = person ("GINO")
p2 = person ("sarsonas")
p3 = person ("aljun")
print (person.number_of_people_())


