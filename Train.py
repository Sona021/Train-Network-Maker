class Train:
    def __init__(self, speed=30):
        self.speed = speed
        self.passengers = 0
        self.capacity = 100

    def get_passengers(self):
        return self.passengers

    def add_passengers(self, num):
        self.passengers += num

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        return f"A train that goes {self.speed} mph"