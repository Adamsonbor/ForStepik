class Tuple(tuple):
    def __init__(self, lst=[]):
        super().__init__()

    
    def __add__(self, other):
        return Tuple(tuple(self[:]) + tuple(other))


a = Tuple([1, 2, 3])
a = a + (1, 2, 3, 4)

print(a)
