class DateString:
    def __init__(self, date_string):
        self._d, self._m, self._y = map(int, date_string.split('.'))
        if self._d <= 0 or self._d >= 32 or self._m <= 0 or self._m >= 13 or self._y <= 0:
            raise DateError

    def __str__(self):
        return f"{self._d:02}.{self._m:02}.{self._y}"

class DateError(Exception):
    pass

try:
   print(DateString('121.4.2022')) 
except DateError as d:
    print("Неверный формат даты")

