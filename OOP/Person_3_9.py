class Person:
    def __init__(self, fio, job, old, salary, year_job):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self.__attrs = tuple(self.__dict__)
        self.__len = 5

    
    def __is_valid_idx(self, idx):
        if idx >= self.__len or idx < 0:
            raise IndexError('неверный индекс')


    def __getitem__(self, idx):
        self.__is_valid_idx(idx)
        return list(self.__dict__.values())[idx]


    def __setitem__(self, idx, value):
        self.__is_valid_idx(idx)
        setattr(self, self.__attrs[idx], value)


    def __iter__(self):
        self.__idx = -1
        return self


    def __next__(self):
        if self.__idx + 1 < self.__len:
            self.__idx += 1
            self.__value = list(self.__dict__.values())[self.__idx]
            return self.__value
        else:
            raise StopIteration



a = Person("sdsf", 'adsgdfg', 61, 1000, 41)
for i in a:
    print(i)

pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for v in pers:
    print(v)
pers[5] = 123 # IndexError
