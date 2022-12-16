class ValidatorString:
    def __init__(self, min_len, max_len, chars=''):
        self.__min_len = min_len
        self.__max_len = max_len
        self.__chars = set(chars)

    def chars_in_string(self, string):
        if len(self.__chars) == 0:
            return True
        return len(self.__chars.intersection(string))

    def is_valid(self, string):
        if self.__min_len > len(string) or self.__max_len < len(string) or not self.chars_in_string(string):
            raise ValueError('недопустимая строка')

    def __call__(self, string):
        self.is_valid(string)
        return string


class LoginForm:
    def __init__(self, login_validator, password_validator):
        self.__login_validator = login_validator
        self.__password_validator = password_validator

    def form(self, request):
        try:
            login = request['login']
            password = request['password']
        except:
            raise TypeError('в запросе отсутствует логин или пароль')
        else:
            self._login = self.__login_validator(login)
            self._password = self.__password_validator(password)


login_v = ValidatorString(4, 50, "")
password_v = ValidatorString(10, 50, "!$#@%&?")
lg = LoginForm(login_v, password_v)
login, password = 'sergey balakirev!'.split()
try:
    lg.form({'login': login, 'password': password})
except (TypeError, ValueError) as e:
    print(e)
else:
    print(lg._login)
    print(lg._password)
