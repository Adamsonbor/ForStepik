from random import randint

# class Prop:
#     def __init__(self, data_type):
#         self.type = data_type


#     def __set_name__(self, owner, name):
#         self.name = f'__{name}'

    
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)


#     def __set__(self, instance, var):
#         if type(var) is self.type:
#             setattr(instance, self.name, var)
#         else:
#             raise ValueError("недопустимое значение атрибута")


class Cell:
    # is_mine = Prop(bool)
    # is_open = Prop(bool)
    # number  = Prop(int)

    __MIN_NUMBER = 0
    __MAX_NUMBER = 8

    def __init__(self):
        self.__is_mine = False
        self.__number  = 0
        self.__is_open = True


    @classmethod
    def is_valid(cls, var):
        if type(var) is int:
            return cls.__MIN_NUMBER <= var <= cls.__MAX_NUMBER
        if type(var) is bool:
            return True
        raise ValueError("недопустимое значение атрибута")

    @property
    def is_mine(self):
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, var):
        self.is_valid(var)
        self.__is_mine = var

    
    @property
    def is_open(self):
        return self.__is_open

    @is_open.setter
    def is_open(self, var):
        self.is_valid(var)
        self.__is_open = var


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, var):
        self.is_valid(var)
        self.__number = var


    def __bool__(self):
        return not self.is_open

    
    def __repr__(self):
        if self.is_open:
            return '*' if self.is_mine else str(self.number)
        else:
            return '#'


class GamePole:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super().__new__(cls)

        return cls.instance


    def __init__(self, N, M, total_mines):
        self.__rows = N
        self.__cols = M
        self.total_mines = total_mines
        self.__pole_cells = self.init_pole()


    @property
    def pole(self):
        return self.__pole_cells


    def show_pole(self):
        for row in self.pole:
            print('\n', end='\t')

            for col in row:
                print(col, end=' ')


    def init_pole(self):
        self.__pole_cells = [[Cell() for col in range(self.__cols)] for row in range(self.__rows)]
        self.fill_mines()
        self.fill_nums()


    def open_cell(self, i, j):
        if i > self.__rows or j > self.__cols:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

        self.pole[i][j].is_open = True


    def fill_mines(self):
        mines = self.total_mines
        while mines:
           cell =  self.pole[randint(0, self.__rows - 1)][randint(0, self.__cols - 1)]
           if not cell.is_mine:
               cell.is_mine = True
               mines -= 1


    def fill_nums(self):
        for row in range(self.__rows):
            for col in range(self.__cols):
                if not self.pole[row][col].is_mine:
                    self.pole[row][col].number = self.calc_mines(row, col)


    def get_coords(self, row, col):
        sr = 0 if row - 1 <= 0 else row - 1
        er = row + 1 if row + 1 >= self.__rows else row + 2
        sc = 0 if col - 1 <= 0 else col -1 
        ec = col + 1 if col + 1 >= self.__cols else col + 2
        
        return sr, er, sc, ec


    def calc_mines(self, row, col):
        sr, er, sc, ec = self.get_coords(row, col)
        num = 0
        for row in range(sr, er):
            for col in range(sc , ec):
                if self.pole[row][col].is_mine:
                    num += 1

        return num


        
        
        


pole = GamePole(10, 20, 40)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
pole.show_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
assert type(Cell.is_mine) == property and type(Cell.number) == property and type(Cell.is_open) == property




