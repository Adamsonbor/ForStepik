from abc import ABC, abstractmethod

class CountryInterface(ABC):
    @property
    @abstractmethod
    def name(self):
        """Countrys name"""

    @property
    @abstractmethod
    def population(self):
        """Countrys population"""

    @property
    @abstractmethod
    def square(self):
        """Countrys square"""

    @abstractmethod
    def get_info(self):
        """Country information"""



class Country(CountryInterface):
    def __init__(self, name, population, square):
        self._name = name
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise ValueError
        self._name = value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, value):
        if type(value) != int or value < 0:
            raise ValueError
        self._population = value

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        if value < 0:
            raise ValueError
        self._square = value

    def get_info(self):
        return f"{self._name}: {self._population}, {self._square}"

country = Country("Россия", 140000000, 324005489.55)
name = country.name
pop = country.population
country.population = 150000000
country.square = 354005483.0
print(country.get_info()) # Россия: 354005483.0, 150000000
