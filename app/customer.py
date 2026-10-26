from app.car import Car


class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location[:]
        self.money = money
        self.car = Car(**car)
        self.fuel_price = 0

    def trip_cost(self, shop, fuel_price):
        product_cost = shop.purchase_cost(self.product_cart)
        if product_cost is None:
            return float("inf")

        distance = self.car.distance(self.location, shop.location)
        fuel_cost = self.car.fuel_cost(distance, fuel_price)
        return product_cost + fuel_cost * 2

    def go_to(self, shop, fuel_price):
        distance = self.car.distance(self.location, shop.location)
        self.money -= self.car.fuel_cost(distance, fuel_price)
        self.fuel_price = fuel_price
        self.location = shop.location[:]

    def go_home(self):
        distance = self.car.distance(self.location, self.home_location)
        self.money -= self.car.fuel_cost(distance, self.fuel_price)
        self.location = self.home_location[:]
