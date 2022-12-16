class Note:
    __slots__ = ('_name', '_ton')
    __cyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')
    __ton_notes = (-1, 0, 1)

    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        if (key == '_name' and value not in self.__cyrillic_notes) or (key == '_ton' and value not in self.__ton_notes):
            raise ValueError('недопустимое значение аргумента')
        super().__setattr__(key, value)

    def __repr__(self):
        return self._name



class Singleton:
    __slots__ = ()
    __instance = None

    def __new__(cls, *args, **kwargs):
        cls.__instance = cls.__instance if cls.__instance else super().__new__(cls)
        return cls.__instance


class Notes(Singleton):
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __cyrillic_notes = ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си')

    def __init__(self):
        for i in range(len(self.__slots__)):
            setattr(self, self.__slots__[i], Note(self.__cyrillic_notes[i]))

    def _is_valid_id(self, idx):
        if type(idx) != int or idx < 0 or idx > 6:
            raise IndexError('недопустимый индекс')

    def __getitem__(self, key):
        self._is_valid_id(key)
        return getattr(self, self.__slots__[key])
    

        

notes = Notes()
notes.a = 5
notes[1]._ton = -1
print(notes[1]._ton)
