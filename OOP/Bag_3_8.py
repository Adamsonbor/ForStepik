class Thing:
    
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight



class Bag:

    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.current_weight = 0
        self.bag = []


    def add_thing(self, thing):
        self.__is_enough_space(thing)
        self.bag.append(thing)
        self.current_weight += thing.weight


    def __len__(self):
        return len(self.bag)


    def __is_valid_idx(self, idx):
        if idx >= len(self):
            raise IndexError('неверный индекс')


    def __is_enough_space(self, thing):
        if self.current_weight + thing.weight > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')


    def __getitem__(self, idx):
        self.__is_valid_idx(idx)
        return self.bag[idx]


    def __setitem__(self, idx, thing):
        self.__is_valid_idx(idx)
        self.current_weight -= self.bag[idx].weight
        self.__is_enough_space(thing)
        self.current_weight +=thing.weight
        self.bag[idx] = thing

    def __delitem__(self, idx):
        self.__is_valid_idx(idx)
        self.current_weight -= self.bag[idx].weight
        del self.bag[idx]

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

    
b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"


