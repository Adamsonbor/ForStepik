class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        

class Lib:
    def __init__(self):
        self.book_list = []
        
    def __add__(self, other):
        self.book_list.append(other)
        return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, int):
            del self.book_list[other]
        else:
            self.book_list.remove(other)
        return self

    def __isub__(self, other):
        return self - other

    def __len__(self):
        return len(self.book_list)


