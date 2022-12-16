import operator

class Vector:
    def __init__(self, *args):
        self.coords = self.__validate_coords(*args)


    def new_vector(self, coords, new):
        if new:
            return Vector(*coords)
        self.coords = coords
        return self



    def __validate_coords(cls, *args):
        out = []
        for i in args:
            if type(i) is str:
                out.append(float(i) if '.' in i else int(i))
            elif type(i) in (int, float):
                out.append(i)
            else:
                raise ValueError("Неверный тип данных")

        return out


    def operator(self, other, op):
        p = {'+':operator.add, '-':operator.sub, '*':operator.mul}
        if type(other) == type(self):
            self.__eq_dim(other)
            coords = [p[op](coord, other.coords[i]) for i, coord in enumerate(self.coords)]
        if type(other) == int:
            coords = [p[op](coord, other) for coord in self.coords]
        return coords


    def __eq_dim(self, other):
        if not len(self.coords) == len(other.coords):
            raise ArithmeticError('размерности векторов не совпадают')


    def __eq__(self, other):
        return all(coord == other.coords[i] for i, coord in enumerate(self.coords))


    def __add__(self, other, new=True):
        coords = self.operator(other, '+')
        return self.new_vector(coords, new)

    
    def __sub__(self, other, new=True):
        coords = self.operator(other, '-')
        return self.new_vector(coords, new)

    
    def __mul__(self, other, new=True):
        coords = self.operator(other, '*')
        return self.new_vector(coords, new)


    def __iadd__(self, other):
        return self.__add__(other, False)


    def __isub__(self, other):
        return self.__sub__(other, False)


    def __imul__(self, other):
        return self.__mul__(other, False)


    def __repr__(self):
        return ' '.join(map(str, self.coords))
            

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print((v1 + v2).coords)  # [5, 7, 9]
print((v1 - v2).coords)  # [-3, -3, -3]
print((v1 * v2).coords)  # [4, 10, 18]

v1 += 10
print(v1.coords)  # [11, 12, 13]
v1 -= 10
print(v1.coords)  # [1, 2, 3]
v1 += v2
print(v1.coords)  # [5, 7, 9]
v2 -= v1
print(v2.coords)  # [-1, -2, -3]

print(v1 == v2)  # False
print(v1 != v2)  # True

