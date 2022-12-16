class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.coords = [0 for i in range(args[0])]
        else:
            self.coords = args
            
    def set_coords(self, *args):
        min_len = len(args) if len(args) < len(self) else len(self)
        self.coords[0:min_len] = args[0:min_len]
        
    def get_coords(self):
        return tuple(self.coords)

    def __len__(self):
        return len(self.coords)

    def __abs__(self):
        return sum(i**2 for i in self.coords)**0.5

vector3D = RadiusVector(3)
vector3D.set_coords(3, -5.6, 8)
a, b, c = vector3D.get_coords()
print(vector3D.get_coords())
vector3D.set_coords(3, -5.6, 8, 10, 11) # ошибки быть не должно, последние две координаты игнорируются
print(vector3D.get_coords())
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты
print(vector3D.get_coords())
res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
