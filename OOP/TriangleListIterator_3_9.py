class TriangleListIterator:
    
    def __init__(self, lst):
        self.lst = lst
        self.__iter_lst = [lst[j][i] for j in range(len(lst)) for i in range(j + 1)]
        self.__len = len(self.__iter_lst)


    def __iter__(self):
        self.__idx = -1
        return self

    
    def __next__(self):
        if self.__idx + 1 < self.__len:
            self.__idx += 1
            return self.__iter_lst[self.__idx]
        else:
            raise StopIteration


    def __repr__(self):
        for i in self:
            print(i)
        return ''



it = TriangleListIterator([[5 * j + i for i in range(5)] for j in range(5)])
print(it)


for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x)

# print([[5 * j + i for i in range(5)] for j in range(5)])
