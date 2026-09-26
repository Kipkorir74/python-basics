class Bow:
    
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

bow_a = Bow("Big Bow", 100, 10)
print(bow_a.__dict__)