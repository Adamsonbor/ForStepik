class Person:
    __slots__ = ["_fio", "_old", "_job"]

    def __init__(self, fio, old, job):
        self._fio = fio
        self._old = old
        self._job = job

    def __repr__(self):
        return f"{self._fio} {self._old} {self._job}"

s = '''Суворов, 52, полководец
Рахманинов, 50, пианист, композитор
Балакирев, 34, программист и преподаватель
Пушкин, 32, поэт и писатель'''
persons = [Person(*i.split(', ', 2)) for i in s.split('\n')]
print(persons)
