import random
import random as rd


class Car:

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def acceleration(self, changed_speed):
        sum_speed = self.current_speed + changed_speed
        if 0 < sum_speed <= self.maximum_speed:
            self.current_speed = sum_speed
        elif sum_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = 0

    def drive(self, number_hours):
        self.travelled_distance += self.current_speed * number_hours
        print(f"The values of the kilometer counters: {self.travelled_distance} km")

class ElectricCar(Car):

    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):

    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume

list_car = []
list_car.append(ElectricCar("ABC-15", 180, 52.5))
list_car.append(GasolineCar("ACD-123", 165, 32.3))

for car in list_car:
    car.acceleration(random.randint(100, 150))
    car.drive(3)

