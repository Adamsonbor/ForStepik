class Thing:
    
    def __init__(self, name, price):
        self.id = id(self)
        self.name = name
        self.price = price
        self.weight = None
        self.dims = None
        self.memory = None
        self.frm = None


    def get_data(self):
        return tuple(self.__dict__.values())



class Table(Thing):

    def __init__(self, name, price, weight, dims):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims



class ElBook(Thing):

    def __init__(self, name, price, memory, frm):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm



a = Table('name', 390, 100, (100, 200, 300))
b = Table('name', 390, 100, (100, 200, 300))
c = ElBook('name', 390, 100, (100, 200, 300))
d = ElBook('name', 390, 100, (100, 200, 300))

print(c.id, b.id, d.id)

