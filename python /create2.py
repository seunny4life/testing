import csv
import os

from flask import Flask, redirect, render_template, request, url_for
from models2 import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



def main():
  f = open("flights.csv")
  reader = csv.reader(f)
  for origin, destination, duration in reader:
      flight = Flight(origin=origin, destination=destination, duration=duration)
      db.session.add(flight)
      print(f'{origin}, {destination}, {duration}')
  db.session.commit()


if __name__ == '__main__':
    main()
