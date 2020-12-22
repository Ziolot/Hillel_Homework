from random import randint


class House:
    def __init__(self, number):
        self.population = randint(1, 100)
        self.number = number


class Street:
    def __init__(self, number):
        self.number = number
        self.houses = []
        for i in range(1, randint(5, 20)):
            self.houses.append(House(i))


class City:
    def __init__(self, name):
        self.name = name
        self.streets = []
        self.populate()

    def populate(self):
        for i in range(1, randint(2, 5)):
            self.streets.append(Street(i))

    def print_city(self):
        for street in self.streets:
            print(f'Street#:{street.number}')
            for house in street.houses:
                print(f'Street #{street.number} - House #{house.number} - population {house.population}')


my_city = City('City 17')
my_city.print_city()