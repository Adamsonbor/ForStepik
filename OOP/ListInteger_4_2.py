class ListInteger(list):

    def __init__(self, lst):
        self._is_valid(*lst)
        super().__init__(lst)

    def __setitem__(self, idx, value):
        self._is_valid(value)
        super().__setitem__(idx, value)

    def append(self, value):
        self._is_valid(value)
        super().append(value)


    def _is_valid(self, *args):
        if any(not issubclass(type(i), int) for i in args):
            raise TypeError('можно передавать только целочисленные значения')


a = ListInteger((1, 2, 3))
a[0] = 10
a.append(5)
print(a[0])

