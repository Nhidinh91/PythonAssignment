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


car1 = Car("ABC-123", 142)
car1.acceleration(+60)
car1.drive(1.5)
car1.drive(2)


print(f"The car with the registration number {car1.registration_number} has: \n\tThe maximum speed: {car1.maximum_speed} km/h.\n\tThe current speed: {car1.current_speed} km/h.\n\tThe travelled distance: {car1.travelled_distance} km")


