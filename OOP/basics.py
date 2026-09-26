class Archer:
# species is a class variable because it belongs to the class 
# rather than to a particular Archer. A class method can access
# it through cls:# Storing objects in the 
# class rather than in an instance - class variable
    species = "human"  

    def __init__(self,hp, mana, arrows): 
        # Initialize the properties
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    def shoot(self):
        if self.arrows > 0:
            self.arrows -=1
            print(f"Archer shot. {self.arrows} left")
        else:
            print("Archer cannot shoot, No arrows left")
    @classmethod
    def from_string(cls, data_string):
        hp, mana, arrows = map(int,data_string.split('-'))  
        return cls(hp,mana,arrows)

    @staticmethod
    def static():
        print("This is a static method")

archer1 = Archer(100,120,4)  #Create an instance of the class Archer

archer2 = Archer.from_string("100-120-4")
archer2.shoot()
