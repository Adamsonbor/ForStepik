class Body:
    def __init__(self, name, ro, volume):
        self.name = name
        self.ro = ro
        self.volume = volume
        self.M = ro * volume

    
    @classmethod
    def is_child(cls, other):
        return type(other) is cls

    @staticmethod
    def mass(func):
        def wrapper(instance, other, *args):
            if type(other) == type(instance):
                return func(instance.M, other.M)
            else:
                return func(instance.M, other)
        return wrapper


    @mass
    def __eq__(self, other): return self == other
    @mass
    def __lt__(self, other): return self < other
    @mass
    def __gt__(self, other): return self > other
    @mass
    def __le__(self, other): return self <= other


body1 = Body('name', 100, 12)
body2 = Body("name", 200, 30)
body1 > body2  # True, если масса тела body1 больше массы тела body2
body1 == body2 # True, если масса тела body1 равна массе тела body2
body1 < 10     # True, если масса тела body1 меньше 10
body2 == 5     # True, если масса тела body2 равна 5
    

