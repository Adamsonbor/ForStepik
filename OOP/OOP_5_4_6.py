class PrimaryKeyError(Exception):
    def __init__(self, **kwargs):
        if kwargs == {}:
            self._message = "Первичный ключ должен быть целым неотрицательным числом"
        elif 'id' in kwargs:
            self._message = f"Значение первичного ключа id = {kwargs['id']} недопустимо"

        elif 'pk'in kwargs:
            self._message = f"Значение первичного ключа pk = {kwargs['pk']} недопустимо"

    def __str__(self):
        return self._message

try:
    raise PrimaryKeyError(id=-10.5)
except PrimaryKeyError as p:
    print(p)


