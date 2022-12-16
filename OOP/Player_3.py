class Player:
    def __init__(self, name, old, score):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __len__(self):
        return self.score

    def __repr__(self):
        return self.name


s = '''Балакирев; 34; 2048
Mediel; 27; 0
Влад; 18; 9012
Nina P; 33; 0'''
lst_in = [i for i in s.split('\n')]
print(lst_in)

lst_in = [Player(*i.split(';')) for i in lst_in]
lst_in = list(filter(lambda x: x, lst_in))

