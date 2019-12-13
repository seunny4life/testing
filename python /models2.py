import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Flight(db.Model):
  __tablename__ = "flights"
  id = db.Column(db.Integer, primary_key=True)
  origin = db.Column(db.String, nullable=False)
  destination = db.Column(db.String, nullable=False)
  duration = db.Column(db.Text, nullable=False)

  def __init__(self, origin, destination, duration):
    self.origin = origin
    self.destination = destination
    self.duration = duration


class Traveller(db.Model):
  __tablename__ = "travellers"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)

  def __init__(self, name, flight_id):
    self.name = name
    self.flight_id = flight_id



if __name__ == '__main__':
  db.create_all()
