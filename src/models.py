import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User  (Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), unique = True, nullable=False)
    email = Column(String(250), unique = True, nullable = False)
    password = Column(String(250), nullable = False)
    active = Column(Boolean, default=True)

class Favorit_Planet(Base):
    __tablename__ = 'favorites planets'
    id = Column(Integer, primary_key = True)
    planets_favorites = Column(String(1000))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', uselist = False, backref = 'favorites_planets')
    planet_id = Column(Integer, ForeignKey('planets.id'))
    planet = relationship('Planet', backref = 'favorites_planets')

class Favorit_People(Base):
    __tablename__ = 'favorites people'
    id = Column(Integer, primary_key = True)
    peoples_favorites = Column(String(1000))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref = 'favorites_people')
    people_id = Column(Integer, ForeignKey('people.id'))
    people = relationship('People', backref = 'favorites_people')

class Planet(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), unique = True, nullable=False)
    diameter = Column(String(250))
    climate = Column(String(250))
    terrain = Column(String(250))

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key = True)
    people_name = Column(String(200), unique = True, nullable = False)
    birth_year = Column(String(200))
    gender = Column(String(200))
    home_world = Column(String(200))
    user_id = relationship('User', uselist = True, backref = 'People')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
