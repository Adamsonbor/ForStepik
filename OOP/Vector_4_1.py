class Vector:
    _allow_types = (int, float)

    def __init__(self, *args):
        self._is_valid_coords(args)
        self.__coords = args


    def get_coords(self):
        return self.__coords


    def _is_valid_coords(self, coords):
        if not all(type(coord) in self._allow_types for coord in coords):
            raise ValueError('coord type is not int or float')


    def _is_valid_dim(self, coords):
        if len(self) != len(coords):
            raise TypeError('размерности векторов не совпадают')


    def _is_valid(self, coords):
        self._is_valid_dim(coords)
        self._is_valid_coords(coords)


    def __new_obj(self, coords):
        try:
            return self.__class__(*coords)
        except ValueError:
            return Vector(*coords)


    def __add__(self, other):
        self._is_valid_dim(other.get_coords())
        return self.__new_obj([self.__coords[i] + coord for i, coord in enumerate(other.get_coords())])


    def __sub__(self, other):
        self._is_valid_dim(other.get_coords())
        return self.__new_obj([self.__coords[i] - coord for i, coord in enumerate(other.get_coords())])


    def __len__(self):
        return len(self.__coords)


    def __str__(self):
        return ' '.join(map(str, self.__coords))



class VectorInt(Vector):
    _allow_types = (int, )
    


a = VectorInt(1, 2, 3, 4, 5) + Vector(1, 2, 3, 4, 5)
a = a - Vector(1, 1, 1, 1, 1) 

print(a.get_coords())





