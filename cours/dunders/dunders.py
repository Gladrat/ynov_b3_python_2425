class Car:
    def __init__(self, color, sku, speed):
        self.color = color
        self.sku = sku
        self.speed = speed

    # def compare_car(self, another_car):
    #     return self.sku == another_car.sku

    def __eq__(self, another_car: Car) -> bool:
        # votre code métier
        return self.sku == another_car.sku

    def __gt__(self, another_car: Car) -> bool:
        return self.__eq__(another_car)


c1 = Car("Red", 123, 230)
c2 = Car("Red", 123, 220)

print(c1 == c2)  # False
print(c1 > c2)