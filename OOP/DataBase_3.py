class Record:
    __count = 0

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        return super().__new__(cls)


    def __init__(self, fio, descr, old):
        self.pk = self.__count
        self.fio = fio
        self.descr = descr
        self.old = int(old)


    def __hash__(self):
        return hash((self.fio.lower().strip(' -?!,.;:'), self.old))


    def __eq__(self, other):
        return hash(self) == hash(other)

    
    def __repr__(self):
        return str(self.fio) + str(self.pk)



class DataBase:
    def __init__(self, path):
        self.path = path
        self.dict_db = {}


    def write(self, record):
        if record in self.dict_db:
            self.dict_db[record].append(record)
        else:
            self.dict_db[record] = [record]


    def read(self, pk):
        for key in self.dict_db.keys():
            if key.pk == pk:

                return self.dict_db[key][-1]



lst = '''Балакирев С.М.; программист; 33
Кузнецов А.В.; разведчик-нелегал; 35
Суворов А.В.; полководец; 42
Иванов И.И.; фигурант всех подобных списков; 26
Балакирев С.М.; преподаватель; 37'''

lst_in = [i for i in lst.split('\n')]

db = DataBase("I am super Proger")

for row in lst_in:
    db.write(Record(*row.split('; ')))

print(db.dict_db)



