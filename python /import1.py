import csv
import os

from flask import Flask, redirect, render_template, request, url_for
from models2 import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


def main():
  f = open("travellers.csv")
  reader = csv.reader(f)
  for name, flight_id in reader:
      travellers = Traveller(name=name, flight_id=flight_id)
      db.session.add(travellers)
      print(f'{name}, {flight_id}')
  db.session.commit()


if __name__ == '__main__':
    main()
