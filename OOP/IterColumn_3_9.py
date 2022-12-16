class IterColumn:

    def __init__(self, lst, col):
        self.lst = lst
        self.__col = col


    def __iter__(self):
        self.__idx = -1
        return self


    def __next__(self):
        try:
            self.__idx += 1
            return self.lst[self.__idx][self.__col]
        except:
            raise StopIteration


lst = [[5 * row + col for col in range(5)] for row in range(5)]
print(lst)
a = IterColumn(lst, 1)
for i in a:
    print(i)
