class Animal:
    def __init__(self, name, kind, old):
        self.__name = name
        self.__kind = kind
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, kind):
        self.__kind = kind

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.__old = old

    def __repr__(self):
        return ' '.join(map(str, self.__dict__.values()))

s = '''Васька; дворовый кот; 5
Рекс; немецкая овчарка; 8
Кеша; попугай; 3'''
animals = [Animal(*i.split('; ')) for i in s.split('\n')]
print(animals)
