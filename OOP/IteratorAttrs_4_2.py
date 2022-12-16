class IteratorAttrs:
    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key, value)


class SmartPhone(IteratorAttrs):
    def __init__(self, model, size, memory):
        self.model = model
        self.size = size
        self.memory = memory


a = SmartPhone('a', 'b', 'c')
for attr, value in a:
    print(attr, value)

i = iter(a)
print(next(i))
