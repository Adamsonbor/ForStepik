class TupleLimit(tuple):
    def __new__(cls, lst, *args, **kwargs):
        return super().__new__(cls, lst)

    def __init__(self, lst, max_length):
        super().__init__()
        if len(lst) > max_length:
            raise ValueError('число элементов коллекции превышает заданный предел')

    def __repr__(self):
        return ' '.join(map(str, self))

t = TupleLimit([1,2,3,4,5], 5)
print(t)


