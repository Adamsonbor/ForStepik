# здесь объявляйте декоратор и все что с ним связано
def log_func(func_name, func, vector_log):
    def wrapper(*args, **kwargs):
        vector_log.append(func_name)
        return func(*args, **kwargs)
    return wrapper


def class_log(vector_log):
    def wrapper(cls):
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, log_func(k, v, vector_log))
        return cls
    return wrapper


vector_log = []   


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


a = Vector(0, 1, 2)
print(a[0])
print(a.__dict__)
print(vector_log)
