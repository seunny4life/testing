import requests

def main():
  res = requests.post("http://www.google.com/")
  print(res)


if __name__ == '__main__':
  main()