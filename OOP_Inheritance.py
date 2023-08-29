class Muzan:

    def __init__ (self, name, rank, year_old, demon_art):
        self.name = name
        self.rank = rank
        self.year_old = year_old
        self.demon_art = demon_art


    def introduce (self):
        print (f"Hello! i am the demon king {self.name}, and i am the demon {self.rank} with me being the oldest at {self.year_old} \
and at last my demon art is {self.demon_art}")
        
class kokushibo (Muzan):

    def __init__ (self, name, rank, year_old, demon_art, gender):
        super().__init__ (name, rank, year_old, demon_art)
        self.gender = gender

    def introduce (self):
        print (f"Hello! i am {self.name}, and i am the {self.rank} with my age at {self.year_old}, \
and at last my art is {self.demon_art}")
        
    def xandy (self):
        print (self.gender)
        
class duoma (kokushibo):

    def introduce (self):
        print (f"Hello! i am {self.name}, and i am the {self.rank} with my age at {self.year_old}, \
and at last my art is {self.demon_art}")
    
    def xandy (self):
        print (self.gender)

class akaza (duoma):

    def introduce (self):
        print (f"Hello! i am {self.name}, and i am the {self.rank} with my age at {self.year_old}, \
and at last my art is {self.demon_art}")
    
    def xandy (self):
        print (self.gender)


class hantengu (akaza):

    def introduce (self):
        print (f"Hello! i am {self.name}, and i am the {self.rank} with my age at {self.year_old}, \
and at last my art is {self.demon_art}")
    
    def xandy (self):
        print (self.gender)

class gyokko (hantengu):

    def introduce (self):
        print (f"Hello! i am {self.name}, and i am the {self.rank} with my age at {self.year_old}, \
and at last my art is {self.demon_art}")
    
    def xandy (self):
        print (self.gender)
    
class kaigaku (gyokko):

    def introduce (self):
        print (f"Hello! i am {self.name}, and i am the {self.rank} with my age at {self.year_old}, \
and at last my art is {self.demon_art}")
    
    def xandy (self):
        print (self.gender)

p = Muzan ("Muzan", "PROGENITOR", 1000, "biokenesis")
p.introduce()

p1= kokushibo ("Kokushibo", "1st kizuki", "480 years old", "moon breathing", "MALE")
p1.introduce()
p1.xandy()
#space
p2 = duoma ("Duoma", "2nd kizuki", "133 years old", "ice", "MALE", )
p2.introduce()
p2.xandy()
#space
p3 = akaza ("Akaza", "3rd kizuki", "269 years old", "compass", "MALE")
p3.introduce()
p3.xandy()
#space
p4 = hantengu ("Hantengu", "4th kizuki", "290 years old", "emotion split", "MALE")
p4.introduce()
p4.xandy()
#space
p5 = gyokko ("Gyokko", "5th kizuki", "113 years old", "CONTROL MARINE LIFE", "MALE")
p5.introduce()
p5.xandy()
#space
p6 = kaigaku ("Kaigaku", "6th kizuki", "17 years old", "thunder breathing", "MALE")
p6.introduce()
p6.xandy()     



    

        

