class Elevator:

    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor
    def floor_up(self, times):
        for num in range(0, times):
            self.current_floor += 1
            print(f"The Elevator is at {self.current_floor} floor")

    def floor_down(self,times):
        for num in range(0, times):
            self.current_floor -= 1
            print(f"The Elevator is at {self.current_floor} floor")

    def go_to_floor(self, destination_floor):
        if destination_floor > self.current_floor:
            self.floor_up((destination_floor - self.current_floor))
        else:
            self.floor_down((self.current_floor - destination_floor))

class Building:

    def __init__(self, bottom_floor, top_floor, number_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_elevators = number_elevators
        self.list_elevator = []
        for num in range(0, number_elevators):
            elevator = Elevator(self.bottom_floor, self.top_floor)
            self.list_elevator.append(elevator)
    def run_elevator(self, no_elevator, destination_floor):
        self.list_elevator[no_elevator-1].go_to_floor(destination_floor)

building1 = Building(-2, 9, 3)
building1.run_elevator(1, 5)
building1.run_elevator(3, 8)
building1.run_elevator(1,2)