class BasePlayer:

    def __init__(self, hp):
        self.hp = hp

    def walk(self):
        print("I am walking")

class Wizard(BasePlayer):
    def walk(self): #Overriding
        print("I am Flying now")

class Archer(BasePlayer):

    def __init__(self, hp,arrows): 
        super().__init__(hp=hp) #Inherit the hp from base class
        self.arrows = arrows

    def shoot(self):  
        self.arrows -=1
        print(f"Archer shoots...{self.arrows} arrows left")

# wizard = Wizard(45)
# wizard.walk()

# archer = Archer(100,5)
# archer.walk()
# archer.shoot()
# archer.shoot()


class NoUpdateDictionary(dict):

    def __setitem__(self, key, value):

        if key in self:
            raise KeyError('Key already Present')
        return super().__setitem__(key, value) #Use the normal dict behavior for adding this item
x = NoUpdateDictionary()
x["test"] = 123
x["test"] = 12233
print(x)