class Thing:
    def __init__(self, name , mass):
        self.name = name.lower().strip(' -!?,.;:')
        self.mass = mass

    def __eq__(self, other):
        return self.name == other.name and self.mass == other.mass


class Box:
    def __init__(self):
        self.lst = []

    def add_thing(self, obj):
        self.lst.append(obj)

    def get_things(self):
        return self.lst

    def __len__(self):
        return len(self.lst)

    def __eq__(self, other):
        if len(self) == len(other):
            return all(i in other.lst for i in self.lst)
        else:
            return False


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2 # True
print(res)
