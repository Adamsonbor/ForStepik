import sys
from time import sleep
from random import randint


class GamePole:
    def __init__(self, size=10):
        self.is_valid_size(size)
        self._size = size
        self._ships = []
        Ship.__size = size

    def is_valid_size(self, size):
        if size < 8 or size > 25:
            raise ValueError

    def init(self):
        self._ships = [Ship(length=i, tp=randint(1, 2)) for i in range(4, 0, -1) for j in range(4, i - 1, -1)]
        for i, ship in enumerate(self._ships):
            out = True
            n = 0
            while out:
                ship.set_start_coords(randint(0, self._size - 1), randint(0, self._size - 1))
                if not ship.is_out_pole(self._size) and all(not ship.is_collide(j) for j in self._ships[:i]):
                    out = False
                n += 1
                if n > 100:
                    self.init()
                    out = False
        self.set_pole()

    def get_ships(self):
        return self._ships

    def move_ships(self):
        for ship in self._ships:
            ship.move(1)
            if ship.is_out_pole(self._size) or any(ship.is_collide(j) for j in self._ships if j != ship):
                ship._v *= -1
                ship.move(1)
        self.set_pole()

    def show(self):
        pole = self.get_colored_pole()
        self.print_chars_for_pole()
        for i, row in enumerate(pole):
            print()
            self.print_number_for_pole(i)
            for col in row:
                self.select_color(col)
                print('  ', end=' ')
                self.reset_config()
        print()

    def print_number_for_pole(self, indx):
        self.bold_font()
        if indx < 10:
            print(f" {indx}", end="")
        else:
            print(f"{indx}", end="")
        self.reset_config()

    def print_chars_for_pole(self):
        print("  ", end="")
        self.bold_font()
        for i in range(self._size):
            print(" ", end="")
            self.print_chars_by_indx(i)
            print(" ", end="")

    def get_pole(self):
        return tuple(tuple(0 if col == None else col[i - col._x if col._tp == 1 else j - col._y] for i, col in enumerate(row)) for j, row in enumerate(self._pole))

    def set_pole(self):
        self._pole = [[None for row in range(self._size)] for col in range(self._size)]
        for ship in self._ships:
            for i in range(ship._length):
                x = ship._x + i if ship._tp == 1 else ship._x
                y = ship._y + i if ship._tp == 2 else ship._y
                self._pole[y][x] = ship

    def get_colored_pole(self):
        pole = [[0 for row in range(self._size)] for col in range(self._size)]
        for ship in self._ships:
            for i in range(ship._length):
                x = ship._x + i if ship._tp == 1 else ship._x
                y = ship._y + i if ship._tp == 2 else ship._y
                cell = 5 if ship._cells[i] == 2 else ship._length
                pole[y][x] = cell
        return pole

    def print_chars_by_indx(self, indx):
        if indx > 25 or indx < 0:
            raise ValueError
        print(chr(65 + indx), end="")

    def bold_font(self):
        print("\033[1m", end="")

    def select_color(self, length):
        out = {5: "\033[40m", 4: "\033[44m", 3: "\033[42m", 2: "\033[43m", 1: "\033[41m", 0: ''}
        print(out[length], end='')

    def reset_config(self):
        print("\033[0m", end='')


class Ship:
    __size = 10

    def __init__(self, length=1, tp=1, x=None, y=None):
        self.is_valid_length(length)
        self.is_valid_tp(tp)
        self._x = x
        self._y = y
        self._v = 1
        self._tp = tp
        self._length = length
        self._is_move = True
        self._cells = [1 for i in range(length)]

    def is_valid_length(self, length):
        if length > 4 or length < 0:
            raise AttributeError

    def is_valid_tp(self, tp):
        if 1 > tp or tp > 2:
            raise AttributeError

    def is_valid_coords(self, *args):
        if any(0 > i >= self.__size for i in args):
            raise AttributeError

    def __getitem__(self, indx):
        return self._cells[indx]

    def __setitem__(self, indx, value):
        if 0 < value < 3:
            self._cells[indx] = value
        else:
            ValueError

    def set_start_coords(self, x, y):
        self.is_valid_coords(x, y)
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move:
            self._x = self._x + go * self._v if self._tp == 1 else self._x
            self._y = self._y + go * self._v if self._tp == 2 else self._y

    def is_collide(self, ship):
        out = False
        sp = [(1, 1), (1, 0), (1, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0)]
        if all(i != None for i in ship.get_start_coords()):
            for i in range(ship._length):
                x, y = ship.get_start_coords()
                x = x + i if ship._tp == 1 else x
                y = y + i if ship._tp == 2 else y
                for j in range(self._length):
                    sx = self._x + j if self._tp == 1 else self._x
                    sy = self._y + j if self._tp == 2 else self._y
                    for s in sp:
                        if sx + s[0] == x and sy + s[1] == y:
                            out = True
                            break
        return out

    def is_out_pole(self, size):
        ex = self._x + self._length if self._tp == 1 else self._x
        ey = self._y + self._length if self._tp == 2 else self._y
        return ex >= size or ey >= size or self._x < 0 or self._y < 0

    def __repr__(self):
        return f'x:{self._x} y:{self._y} L:{self._length}'


class SeaBattle:
    def __init__(self):
        self.first_window()
        self.p1_pole = GamePole(self._size)
        self.p1_pole.init()
        self.computer_pole = GamePole(self._size)
        self.computer_pole.init()

    def game_loop(self):
        game = True
        self.clear_screen()
        self.p1_pole.show()
        while game:
            a = input()
            if len(a) == 2 and a[0].isalpha() and a[1].isdigit():
                self.clear_screen()
                x, y = ord(a[0]) - 97, int(a[1])
                if x > self._size or y > self._size:
                    self.print_attack(False)
                else:
                    self.print_attack(self.attack(self.computer_pole._pole, x, y))
                self.clear_screen()
                self.attack(self.p1_pole._pole, randint(0, self._size - 1), randint(0, self._size - 1))
                self.move_ships()
                self.p1_pole.show()
                if self.is_lose(self.p1_pole):
                    self.print_lose()
                    game = False
                elif self.is_lose(self.computer_pole):
                    self.print_win()
                    game = False
            elif a == 'q' or a == 'Q':
                game = False
            else:
                print("Please enter chars like a5 or d4:")

    def is_lose(self, player):
        out = True 
        for ship in player._ships:
            for cell in ship._cells:
                if cell == 1:
                    out = False
                    break
        return out

    def clear_screen(self):
        print("\033[2J\033[0;0H")

    def print_win(self):
        self.clear_screen()
        print("\n\n\n\n")
        print("\t\t\033[1m\033[42m   You Won!!!  \033[0m")
        print("\n\n\n\n")

    def print_lose(self):
        self.clear_screen()
        print("\n\n\n\n")
        print("\t\t\033[1m\033[42m   You Lose  \033[0m")
        print("\n\n\n\n")

    def move_ships(self):
        self.p1_pole.move_ships()
        self.computer_pole.move_ships()

    def print_attack(self, attack):
        print("\033[2J\033[0;0H\033[1m\n\n\n\n", end="")
        if attack:
            print("\t\tSuccessfully!")
        else:
            print("\t\tMiss.")
        print("\n\n\t\tpress enter")
        input()


    def attack(self, pole, x, y):
        success = False
        cell = pole[y][x]
        if cell != None and cell[y - cell._y if cell._tp == 2 else x - cell._x] != 2:
            cell[y - cell._y if cell._tp == 2 else x - cell._x] = 2
            cell._is_move = False
            success = True
        return success


    def first_window(self):
        self.print_game_rules()
        print("\n\n")
        self.read_field_size()
        print("\033[0m")

    def read_field_size(self):
        print("field size (10): ", end="")
        size = input()
        if size.isalpha():
            self.first_window()
        else:
            if len(size) == 0:
                self._size = 10
            else:
                self._size = int(size)

    def print_game_rules(self):
        print("\033[2J\033[0;0H")
        print("\033[1m", end="")
        text = ["Neo!\n", "Field size must be greater than 7 and less than 25!\n", "Coords must be [a-z][0-size]\n", "q - quit\n"]
        for line in text:
            for char in line:
                sys.stdout.write(char)
                sys.stdout.flush()
                sleep(0.05)
            sleep(0.3)


game = SeaBattle()
game.game_loop()

ship = Ship(2)
ship = Ship(2, 1)
ship = Ship(3, 2, 0, 0)

assert ship._length == 3 and ship._tp == 2 and ship._x == 0 and ship._y == 0, "неверные значения атрибутов объекта класса Ship"
assert ship._cells == [1, 1, 1], "неверный список _cells"
assert ship._is_move, "неверное значение атрибута _is_move"

ship.set_start_coords(1, 2)
assert ship._x == 1 and ship._y == 2, "неверно отработал метод set_start_coords()"
assert ship.get_start_coords() == (1, 2), "неверно отработал метод get_start_coords()"

ship.move(1)
s1 = Ship(4, 1, 0, 0)
s2 = Ship(3, 2, 0, 0)
s3 = Ship(3, 2, 0, 2)

assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 0)"
assert s1.is_collide(s3) == False, "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 0, 2)"

s2 = Ship(3, 2, 1, 1)
assert s1.is_collide(s2), "неверно работает метод is_collide() для кораблей Ship(4, 1, 0, 0) и Ship(3, 2, 1, 1)"

s2 = Ship(3, 1, 8, 1)
assert s2.is_out_pole(10), "неверно работает метод is_out_pole() для корабля Ship(3, 1, 8, 1)"

s2 = Ship(3, 2, 1, 5)
assert s2.is_out_pole(10) == False, "неверно работает метод is_out_pole(10) для корабля Ship(3, 2, 1, 5)"

s2[0] = 2
assert s2[0] == 2, "неверно работает обращение ship[indx]"
p = GamePole(10)
p.init()
for nn in range(5):
    for s in p._ships:
        assert s.is_out_pole(10) == False, "корабли выходят за пределы игрового поля"

        for ship in p.get_ships():
            if s != ship:
                assert s.is_collide(ship) == False, "корабли на игровом поле соприкасаются"
    p.move_ships()
    
gp = p.get_pole()
assert type(gp) == tuple and type(gp[0]) == tuple, "метод get_pole должен возвращать двумерный кортеж"
assert len(gp) == 10 and len(gp[0]) == 10, "неверные размеры игрового поля, которое вернул метод get_pole"

pole_size_8 = GamePole(8)
pole_size_8.init()
