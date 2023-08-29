class demon_slayer:
    
    def __init__ (self,name,last_name, gender, favorite_food):
        self.name = name
        self.last_name = last_name
        self.gender =gender
        self.favorite_food = favorite_food

    def show_master (self):
        print ("Hello guys my name is kagaya ubayashiki, below are my students and are an uprising demon slayers")
        
class Tanjiro (demon_slayer):

    def __init__(self, name, last_name, gender, favorite_food, breathing_style):
        super().__init__ (name,last_name, gender, favorite_food)
        self.breathing_style = breathing_style

    def introduce (self):
        print (f"Wassup my name is {self.name} {self.last_name}, i am a {self.gender}, my favorite food is {self.favorite_food} \
and the breathing that i use to slay demons is {self.breathing_style}")
        
    def show_weapon (self):
        print ("Katana (black)")

class Nezuko (Tanjiro):

    def __init__(self, name, last_name, gender, favorite_food, breathing_style, weapon):
        super().__init__ (name, last_name, gender, favorite_food, breathing_style)
        self.weapon = weapon

    def introduce(self):
        print (f"Hi! my name is {self.name}, i am the younger sister of Tanjiro Kamado and i am a {self.gender},\
my favorite food is {self.favorite_food}, i dont have a breathing style because i have {self.breathing_style}")
        

    def Show_weapon (self):
        print (self.weapon)
    
    
class zenitsu (Nezuko):

    def introduce(self):
        print (f"Wassup my name is {self.name} {self.last_name}, i am a {self.gender}, my favorite food is {self.favorite_food} \
and the breathing that i use to slay demons is {self.breathing_style}")
    
    def Show_weapon(self):
        print (self.weapon)
        
    
    
class Inosuke (Nezuko) :

    def introduce(self):
        print (f"Wassup my name is {self.name} {self.last_name}, i am a {self.gender}, my favorite food is {self.favorite_food} \
and the breathing that i use to slay demons is {self.breathing_style}")
    
    def Show_weapon(self):
        print (self.weapon)
    

d1 = Tanjiro ("Tanjiro", "Kamado", "MALE", "Rice balls", "Sun breathing")
d1.introduce()
d1.show_weapon()

d2 = Nezuko ("Nezuko", "Kamado", "FEMALE", "HUMAN FLESH", "Demon powers", "claws")
d2.introduce()
d2.Show_weapon()

d3 = zenitsu ("Zenitsu", "Agatsuma", "MALE", "high quality eel", "Thunder breathing", "Yellow Katana")
d3.introduce()
d3.Show_weapon()

d4 = Inosuke ("Inosuke", "Hashibira", "MALE", "tempura", "Beast Breathing", "Dual Katana")
d4.introduce()
d4.Show_weapon()