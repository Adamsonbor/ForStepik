class Protists:
    def __init__(self, name, weight, old):
        self.name = name
        self.weight = weight
        self.old = old

    def __repr__(self):
        return self.name


class Plants(Protists):
    pass

class Mosses(Plants):
    pass

class Flowering(Plants):
    pass

class Animals(Protists):
    pass

class Worms(Animals):
    pass

class Mammals(Animals):
    pass

class Human(Mammals):
    pass

class Monkeys(Mammals):
    pass


s = '''Monkey: "мартышка", 30.4, 7
Monkey: "шимпанзе", 24.6, 8
Person: "Балакирев", 88, 34
Person: "Верховный жрец", 67.5, 45
Flower: "Тюльпан", 0.2, 1
Flower: "Роза", 0.1, 2
Worm: "червь", 0.01, 1
Worm: "червь 2", 0.02, 1'''

def cr(type_, line):
    _, body = line.split(": ")
    name, weight, old = body.split(", ")
    return type_(name, weight, old)

lst_objs = []
for line in s.split("\n"):
    if 'Monkey' in line:
        lst_objs.append(cr(Monkeys, line))
    if 'Person' in line:
        lst_objs.append(cr(Human, line))
    if 'Flower' in line:
        lst_objs.append(cr(Flowering, line))
    if 'Worm' in line:
        lst_objs.append(cr(Worms, line))

lst_animals = list(filter(lambda x: isinstance(x, Animals), lst_objs))
lst_plants = list(filter(lambda x: isinstance(x, Plants), lst_objs))
lst_mammals = list(filter(lambda x: isinstance(x, Mammals), lst_objs))
print(lst_animals)







