class Record:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


    def __len__(self):
        return len(self.__dict__)


    def __is_valid_key(self, key):
        if not (type(key) is int and 0 <= key < len(self)):
            raise IndexError('неверный индекс поля')


    def __getitem__(self, key):
        self.__is_valid_key(key)
        return list(self.__dict__.values())[key]


    def __setitem__(self, key, value):
        self.__is_valid_key(key)
        setattr(self, list(self.__dict__)[key], value)





r = Record(pk=1, title='Python ООП', author='Балакирев')
r[0] = 2 # доступ к полю pk
r[1] = 'Супер курс по ООП' # доступ к полю title
r[2] = 'Балакирев С.М.' # доступ к полю author
print(r[1]) # Супер курс по ООП
r[3] # генерируется исключение IndexError
