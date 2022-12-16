class Dimensions:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = self.__validate(a, b, c)
    

    @classmethod
    def __validate(cls, *args):
        out = [var if type(var) in (int, float) else float(var) if '.' in var else int(var) for var in args] 
        if all(i <= 0 for i in out):
            raise ValueError("габаритные размеры должны быть положительными числами")

        return out      


    def __hash__(self):
        return hash((self.a, self.b, self.c))


    def __lt__(self, other):
        return hash(self) < hash(other)


    def __repr__(self):
        # return ' '.join(map(str, self.__dict__.values()))
        return str(hash(self))

s_inp = "1 2 3; 4 5 6.78; 1 2 3; 0 1 2.5"

lst_dim = [Dimensions(*i.split()) for i in s_inp.split('; ')]
lst_dim = sorted(lst_dim)

