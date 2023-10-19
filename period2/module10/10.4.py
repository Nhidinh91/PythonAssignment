import random as rd
class Car:
    current_speed = 0
    travelled_distance = 0


    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

    def acceleration(self, changed_speed):
        sum_speed = self.current_speed + changed_speed
        if sum_speed >0 and sum_speed <= self.maximum_speed:
            self.current_speed = sum_speed
        elif sum_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        else:
            self.current_speed = 0
    def drive(self, number_hours):
        self.travelled_distance += self.current_speed*number_hours

class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list
    def hour_passes(self):
        for car in self.car_list:
            changed_speed = rd.randint(-10, 15)
            car.acceleration(changed_speed)
            car.drive(1)

    def print_status(self):
        for car in self.car_list:
            print(f"The car with the registration number {car.registration_number} has: \n\tThe maximum speed: {car.maximum_speed} km/h.\n\tThe current speed: {car.current_speed} km/h.\n\tThe travelled distance: {car.travelled_distance} km")

    def race_finished(self):
        win = False
        for car in self.car_list:
            if car.travelled_distance >= self.kilometers:
                win = True
        return win

list_car = []
numbers_hour = 0
for num in range(1,11):
    registration_number = "ABC-" + str(num)
    car_number = Car(registration_number, (rd.randint(100,200)))
    list_car.append(car_number)

race1 = Race("Grand Demolition Derby",8000, list_car)

while True:
    numbers_hour += 1
    race1.hour_passes()
    if numbers_hour % 10 == 0:
        print(f"After {numbers_hour} minutes:")
        race1.print_status()

    if race1.race_finished():
        print("Finally, we found the winner!")
        race1.print_status()
        break
