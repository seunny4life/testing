import os

from flask import Flask, redirect, render_template, request, url_for
from models2 import *

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


def main():
  flights = Flight.query.filter_by(id=9).first()
  flight = Flight.query.get(9 )
  print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes")


if __name__ == '__main__':
    with app.app_context():
      main()
