class Cell:
    __s = {0: ' ', 1: 'X', 2: 'O'}
    
    def __init__(self):
        self.value = 0


    def __bool__(self):
        return not self.value


    def __str__(self):
        return self.__s[self.value]



class TicTacToe:
    FREE_CELL = 0
    HUMAN_X = 1
    COMPUTER_O = 2

    def __init__(self):
        self.init()


    @property
    def is_human_win(self):
        self.__is_human_win = self.__is_win()
        return self.__is_human_win


    @property
    def is_computer_win(self):
        self.__is_computer_win = self.__is_win(2)
        return self.__is_computer_win


    @property
    def is_draw(self):
        if all((any(self[i, i] == 2 for i in range(3)),\
                any(self[i, i] == 2 for i in range(2, -1, -1)),\
                any(2 in self.pole[row] for row in range(3)),\
                any(2 in [self[row, col] for row in range(3)] for col in range(3)))):
            self.__is_draw = True
        return self.__is_draw


    def __is_win(self, player=1):
        if all(self[i, i] == player for i in range(3)):
            return True
        if all(self[i, i] == player for i in range(2, -1, -1)):
            return True
        for row in range(3):
            if all(self[row, col] == player for col in range(3)):
                return True
        for col in range(3):
            if all(self[row, col] == player for row in range(3)):
                return True
        return False


    def __step(self, player=1):
        for row in range(3):
            for col in range(3):
                if not self[row, col]:
                    self[row, col] = player
                    return


    def show(self):
        for i, row in enumerate(self.pole):
            print()
            print('\t', '-'*11, end='\n\t|')
            for j, col in enumerate(row):
                print(f' {col} ', end='|')
        print()
        print('\t', '-'*11)


    def __is_valid_idx(self, *idxs):
        if any(type(i) not in (int, float) or i < 0 or i > 2 for i in idxs):
            raise IndexError('некорректно указанные индексы')


    def human_go(self):
        self.__step(self.HUMAN_X)
    

    def computer_go(self):
        self.__step(self.COMPUTER_0)


    def init(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.__is_human_win = False
        self.__is_computer_win = False
        self.__is_draw = False


    def __getitem__(self, idxs):
        self.__is_valid_idx(*idxs)

        return self.pole[idxs[0]][idxs[1]].value


    def __setitem__(self, idxs, value):
        self.__is_valid_idx(*idxs)
        self.__is_valid_idx(value)
        self.pole[idxs[0]][idxs[1]].value = value


    def __bool__(self):
        return not (self.is_human_win or self.is_computer_win or self.is_draw)


cell = Cell()
assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
cell.value = 1
assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"

assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"

game = TicTacToe()
assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
game[1, 1] = TicTacToe.HUMAN_X
assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game[0, 0] = TicTacToe.COMPUTER_O
assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"

game.init()
assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"

try:
    game[3, 0] = 4
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

game.init()
assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"

game[0, 0] = TicTacToe.HUMAN_X
game[1, 1] = TicTacToe.HUMAN_X
game[2, 2] = TicTacToe.HUMAN_X
assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"

game.init()
game[0, 0] = TicTacToe.COMPUTER_O
game[1, 0] = TicTacToe.COMPUTER_O
game[2, 0] = TicTacToe.COMPUTER_O
assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
