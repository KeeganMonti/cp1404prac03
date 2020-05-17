from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, reliability={}".format(super().__str__(), self.reliability)

    def drive(self, distance):
        if randint(1, 100) < self.reliability:
            super().drive(distance)
        else:
            return 0
