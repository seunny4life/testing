class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

     # Keep tract of id number.#
        self.id = Flight.counter
        Flight.counter += 1

        #keoo track of passangers#
        self.passengers = []

        # Detail about flight.
        self.origin = origin
        self.destination = destination
        self.duration = duration

    def print_info(self):
        print(f'Flight origin. {self.origin}')
        print(f'FLight destination. {self.destination}')
        print(f'Flight duration. {self.duration}')

        print()
        print("Passenger:")
        for passenger in self.passengers:
            print(f'{passenger.name}')

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id


class Passenger:

    def __init__(self, name):
        self.name = name


def main():

    f = Flight(origin='New York', destination='Lagos', duration=900)

    ali = Passenger(name='Ali')
    bob = Passenger(name="Bob")

    # add passengers.
    f.add_passenger(ali)
    f.add_passenger(bob)

    f.delay(20)
    f.print_info()

    print()


if __name__ == '__main__':
    main()
