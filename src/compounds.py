
class Compound:
    
    def __init__(self, name, map, pos_x, pos_y):
        self.name = name
        self.map = map
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __eq__(self, other):
        return self.name == other.name
    
    def __repr__(self):
        return f"Compound: {self.name}, Map: {self.map}, Position: {self.pos_x} : {self.pos_y}"