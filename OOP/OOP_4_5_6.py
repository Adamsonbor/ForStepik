from abc import ABC, abstractmethod

class Model(ABC):
    def get_info(self):
        return "Базовый класс Model"

    @abstractmethod
    def get_pk(self):
        """hello world"""


class ModelForm(Model):
    def __init__(self, login, password):
        self._id = id(self)
        self._login = login
        self._password = password

    def get_pk(self):
        return self._id


form = ModelForm("Логин", "Пароль")
print(form.get_pk())
