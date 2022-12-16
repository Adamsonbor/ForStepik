
class MaxPooling:
    def __init__(self, step=(1, 1), size=(2, 2)):
        self.__step = step
        self.__size = size

    def is_valid(self, matrix):
        l = len(matrix)
        return all(len(i) == l for i in matrix) and all(type(j) in (int, float) for i in matrix for j in i)

    def __call__(self, matrix):
        if not self.is_valid(matrix):
            raise ValueError("Неверный формат для первого параметра matrix.")

        rows = len(matrix)
        cols = len(matrix[0])
        w, h = self.__size
        sw, sh = self.__step
        x_steps = (cols - w) // sw + 1 
        y_steps = (rows - h) // sh + 1
        out = [[0] * x_steps for _ in range(y_steps)] 

        for i in range(y_steps):
            for j in range(x_steps):
                win = (x for row in matrix[i * sh: i * sh + h] for x in row[j * sw: j * sw + w])
                out[i][j] = max(win)

        return out
                

mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

print(res1)
assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"
 
