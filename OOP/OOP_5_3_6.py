class Test:
    def __init__(self, descr):
        if len(descr) < 10 or len(descr) > 10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self._descr = descr

    def run(self):
        raise NotImplementedError


class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit=0.01):
        super().__init__(descr)
        if not all(type(i) in (int, float) for i in (ans_digit, max_error_digit)) or max_error_digit < 0:
            raise ValueError('недопустимые значения аргументов теста')
        self._ans_digit = ans_digit
        self._max_error_digit = max_error_digit

    def run(self):
        ans = float(input()) # именно такой командой, ее прописывайте в методе run()
        return self._ans_digit - self._max_error_digit < ans < self._ans_digit + self._max_error_digit

try:
    descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
    # descr, ans = 'asdfsadsdsagasdg', '5'
    ans = float(ans) # здесь для простоты полагаем, что ans точно число и ошибок в преобразовании быть не может

    t = TestAnsDigit(descr, ans)
    print(t.run())
except Exception as e:
    print(e)

