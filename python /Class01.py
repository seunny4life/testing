class Flight:

  def __init__(self, origin, destination, duration):
    self.origin = origin
    self.destination = destination
    self.duration = duration


def main():

  f = Flight(origin='New York', destination='Lagos', duration=900)
  f2 = Flight(origin='Dubai', destination='Lagos', duration=700)

  f.duration += 20
  f2.duration -= 50

  print(f.origin)
  print(f.destination)
  print(f.duration)
  print()

  print(f2.origin)
  print(f2.destination)
  print(f2.duration)


if __name__ == '__main__':
      main()
