class BookStudy:
    def __init__(self, name, author, year):
        self.name = name 
        self.author = author
        self.year = year


    @classmethod
    def __validate(cls, var):
        return var.strip(' -,.?!:;').lower()


    def __hash__(self):
        return hash((self.__validate(self.name), self.__validate(self.author)))


    def __eq__(self, other):
        return hash(self) == hash(other)


    
lst_in = '''Python; Балакирев С.М.; 2020
Python ООП; Балакирев С.М.; 2021
Python ООП; Балакирев С.М.; 2022
Python; Балакирев С.М.; 2021'''

lst_in = [i for i in lst_in.split('\n')]
lst_bs = [BookStudy(*i.split('; ')) for i in lst_in]
unique_books = len(set(lst_bs))
print(unique_books)


