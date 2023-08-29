class strawhats:

    def __init__(self, name, age, power, gender, haki):
        self.name = name
        self.age = age
        self.power = power
        self.gender = gender
        self.haki = haki

    def call (self):
        print ("one piece bounty rush!!! kaizokuu")

class Monkey__D__Luffy (strawhats):
    def __init__(self, name, age, power, gender, haki, hometown):
        super().__init__(name, age, power, gender, haki)
        self.hometown = hometown

    def call (self):
        print (f"Hello my name is {self.name}, i am {self.age} years old my main power is {self.power}, i am a {self.gender}, and yes i have\
 {self.haki} all three, armament, observation and conquerors.")
        
    def origin (self):
        print (f"i live in {self.hometown}")

class Roronoa_Zoro (Monkey__D__Luffy):
    

    def call (self):
        print(f"Hello i am {self.name}, and i am {self.age} years old and i am a {self.gender}, my main power is that i am a {self.power} and my dream is to\
 become the strongest swordsman, {self.haki} i have haki same as luffy's.")
        
    def origin (self):
        print (f"i was born on {self.hometown}")

class Sanji (Monkey__D__Luffy):


    def call (self):
        print (f"Hi! my name is {self.name} and i am {self.age} years old, and i am a {self.gender}. My main power is that i am a {self.power},\
 {self.haki} but i only have armament and observational to be in fact my observational haki is one of my powerhouses.")
        
    def origin (self):
        print (f"i was born on {self.hometown}")

class Nami (Monkey__D__Luffy):


    def call (self):
        print (f"Hi! my name is {self.name} and i am {self.age} years old and i am a {self.gender}, my power is that {self.power}. I have {self.haki}.")

    def origin (self):
        print (f"i was born in {self.hometown}")

all = strawhats ("df", "sdd","ds", "dsd", "dsd")
all.call ()

p0 = Monkey__D__Luffy ("Monkey D. Luff", "19", "HITO HITO NO MI MODEL SUN GOD NIKA", "Male", "Haki", "east blue")
p0.call ()
p0.origin()

p1 = Roronoa_Zoro ("Roronoa Zoro", "21", "Swordsman", "Male", "Yes", "The Land of Wano")
p1.call ()
p1.origin()

p2 = Sanji ("Sanji", "21", "germa and my ephitet is the black foot", "Male", "I have Haki", "North Blue")
p2.call ()
p2.origin()

p3 = Nami ("Nami", "20", "i can sense climate changes and i can also draw sea charts", "Female", "No haki", "East Blue")
p3.call ()
p3.origin()
