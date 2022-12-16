class RadiusVector:

    def __init__(self, *args):
        self.coords = list(args)


    def __getitem__(self, keys):
        if type(keys) is slice:
            return tuple(self.coords[keys])
        return self.coords[keys]


    def __setitem__(self, keys, values):
        self.coords[keys] = values


    def __repr__(self):
        return ' '.join(map(str, self.coords))


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[::2] == (1, 3))
v[:3] = 2, 3, 4
# v[0] = 1
print(v)
# print(v[2]) # 3
# print(v[1:]) # (2, 3, 4)
# v[0] = 10.5
