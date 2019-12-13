class Flight:

  def __init__(self, origin, destination, duration):
    self.origin = origin
    self.destination = destination
    self.duration = duration

  def print_info(self):
    print(f'Flight origin. {self.origin}')
    print(f'FLight destination. {self.destination}')
    print(f'Flight duration. {self.duration}')

  def delay(self, amount):
    self.duration += amount

def main():

  f = Flight(origin='New York', destination='Lagos', duration=900)

  f.delay(20)
  f.print_info()
 
  print()

  f2 = Flight(origin='Dubai', destination='Lagos', duration=700)
  f2.delay(100)
  f2.print_info()


if __name__ == '__main__':
      main()
