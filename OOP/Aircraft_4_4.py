class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __is_valid_model(self, model):
        if type(model) != str:
            raise TypeError('неверный тип аргумента')

    def __setattr__(self, attr, value):
        if attr in ('_model',) and type(value) != str:
            raise TypeError('неверный тип аргумента')
        if attr in ('_top', '_mass', '_speed'):
            if type(value) not in (int, float) or value < 0:
                raise TypeError('неверный тип аргумента')
        super().__setattr__(attr, value)


class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        super().__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, attr, value):
        if attr == '_chairs':
            if type(value) != int or value < 0:
                raise TypeError('неверный тип аргумента')
        super().__setattr__(attr, value)


class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        super().__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, attr, value):
        if attr == '_weapons' and type(value) != dict:
            raise TypeError('неверный тип аргумента')
        super().__setattr__(attr, value)

planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
print(planes)
