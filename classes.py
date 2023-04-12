class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2

p = Point(2, 8)
print(f"({p.x}, {p.y})")

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = [] #empty list of passengers

    def add_passenger(self, name):
        if not self.open_seats(): #i.e. self.open_seats()==0, as in C
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Ginny"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")