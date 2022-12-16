class Animal:

    def __init__(self, name, old):
        self.name = name
        self.old = old


    def get_info(self):
        values = tuple(self.__dict__.values())
        return f"{values[0]}: {values[1]}, {values[2]}, {values[3]}"


class Cat(Animal):

    def __init__(self, name, old, color, weight):
        super().__init__(name, old)
        self.color = color
        self.weight = weight


class Dog(Animal):

    def __init__(self, name, old, breed, size):
        super().__init__(name, old)
        self.breed = breed
        self.size = size



a = Cat('cat', 5, 'white', 200)
print(a.get_info())
