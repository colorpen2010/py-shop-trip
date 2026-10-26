from math import hypot


class Car:
    def __init__(self, brand, fuel_consumption):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def fuel_cost(self, distance, fuel_price):
        return distance * self.fuel_consumption / 100 * fuel_price

    @staticmethod
    def distance(first_location, second_location):
        return hypot(
            first_location[0] - second_location[0],
            first_location[1] - second_location[1],
        )
