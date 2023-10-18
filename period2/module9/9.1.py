class Car:
    current_speed = 0
    travelled_distance = 0
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed

car1 = Car("ABC-123", 142)
print(f"The car with the registration number {car1.registration_number} has: \n\tThe maximum speed: {car1.maximum_speed} km/h.\n\tThe current speed: {car1.current_speed} km/h.\n\tThe travelled distance: {car1.travelled_distance} km")