class Furniture:
    maker = "Ikea"
    weight = 15

class Storage(Furniture):
    
    size = 100 * 200 * 30
    
    shelves = 4

    def add_thing(self, weight):
        self.weight += weight
    def remove_thing(self, weight):
        self.weight -= weight


class Support(Furniture):
    
    is_assembled = True
    square = 1
    

    def collect(self):
        self.is_assembled == True
    def disassemble(self):
        self.is_assembled == False


class Storage:
    weight = 20
    size = 100 * 200 * 30
    maker = "Ikea"
    shelves = 4

    def add_thing(self, weight):
        self.weight += weight
    def remove_thing(self, weight):
        self.weight -= weight


class Support:
    weight = 10
    is_assembled = True
    square = 1
    maker = "Ikea"

    def collect(self):
        self.is_assembled == True
    def disassemble(self):
        self.is_assembled == False

shelf = Storage()
print(shelf.weigth)