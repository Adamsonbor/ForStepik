class StringDigit(str):
    def __init__(self, string):
        self._is_valid(string)
        super().__init__()

    def _is_valid(self, string):
        if any(not i.isdigit() for i in string):
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        return self.__class__(f"{self}{other}")

    def __radd__(self, other):
        return self.__class__(f"{other}{self}")





a = StringDigit('89222500313')
sd = StringDigit("123")
print(sd)       # 123
print(isinstance(sd, str))
sd = sd + "456" # StringDigit: 123456
sd = "789" + sd # StringDigit: 789123456
# print(sd)
# sd = sd + "12f" # ValueError
# print(sd)
