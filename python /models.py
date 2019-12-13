from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()  

class Flight(db.Model):
  __tablename__ = "flights"
  id = db.Column(db.Integer, primary_key=True)
  origin = db.Column(db.String, nullable=False)
  destination = db.Column(db.String, nullable=False)
  duration = db.Column(db.Text, nullable=False)


class Traveller(db.Model):
  __tablename__ = "travellers"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  flight_id = db.Column(db.Integer, db.ForeignKey("flights.id"), nullable=False)
