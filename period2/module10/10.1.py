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

elevator1 = Elevator(-1, 10)
elevator1.go_to_floor(6)
elevator1.go_to_floor(-1)