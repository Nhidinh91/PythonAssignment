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


list_car = []
for num in range(1,11):
    registration_number = "ABC-" + str(num)
    car_number = Car(registration_number, (rd.randint(100,200)))
    list_car.append(car_number)

number_hours = 0
while True:
    number_hours += 1
    win = False
    for car in list_car:
        changed_speed = rd.randint(-10, 15)
        car.acceleration(changed_speed)
        car.drive(1)
        if car.travelled_distance >= 10000:
            win = True
            break

    if win == True:
        break


for car in list_car:
    print(f"The car with the registration number {car.registration_number} has: \n\tThe maximum speed: {car.maximum_speed} km/h.\n\tThe current speed: {car.current_speed} km/h.\n\tThe travelled distance: {car.travelled_distance} km")
