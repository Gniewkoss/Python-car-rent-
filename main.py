class Vehicle:
    def __init__(self, id):
        self.id = id


class Bike(Vehicle):
    pass


class Scooter(Vehicle):
    pass


class Rental:
    def __init__(self, vehicle: Vehicle, user: str) -> None:
        self.vehicle = vehicle
        self.user = user


vehicle_list: list[Vehicle] = []
rental_list: list[Rental] = []

while True:
    line = input("> ")

    if line == "quit":
        break

    elif line.startswith("add"):
        cmd, id, type_ = line.split()

        id = int(id)

        vehicle_list.append(Bike(id) if type_ == "bike" else Scooter(id))

        print("vehicle_list", vehicle_list)
        print("rental_list", rental_list)

    elif line.startswith("rent"):
        cmd, id, *user = line.split()

        username = " ".join(user)
        id = int(id)

        for vehicle in vehicle_list:
            if vehicle.id == id:
                rental_list.append(Rental(vehicle, username))

        print("vehicle_list", vehicle_list)
        print("rental_list", rental_list)

    elif line.startswith("return"):
        cmd, id = line.split()

        id = int(id)

        for rental in rental_list:
            if rental.vehicle.id == id:
                rental_list.remove(rental)

        print("vehicle_list", vehicle_list)
        print("rental_list", rental_list)

    elif line == "available":
        scooter = 0
        bike = 0

        for i in vehicle_list:
            if type(i) == Bike:
                bike += 1
            elif type(i) == Scooter:
                scooter += 1
        for i in rental_list:
            if type(i.vehicle) == Bike:
                bike -= 1
            elif type(i.vehicle) == Scooter:
                scooter -= 1




