import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


# Tabla intermedia para la relación muchos a muchos entre Users y sus favoritos
favorites_table = Table('favorites', Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('characters.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planets.id'), primary_key=True),
    Column('starship_id', Integer, ForeignKey('starships.id'), primary_key=True)
)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    registration_date = Column(String(50), nullable=True)
    password = Column(String(100), nullable=False)
    
    # Relación muchos a muchos con la tabla intermedia 'favorites'
    favorites = relationship("Favorites", secondary=favorites_table, backref="users", lazy=True)

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
    
    # Relación con la tabla 'Planets'
    planet = relationship('Planets', backref='characters', lazy=True)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    
    # Relación con la tabla 'Characters'
    characters = relationship('Characters', backref='planet', lazy=True)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    
    # Relación con la tabla 'Characters'
    character = relationship('Characters', backref='starships', lazy=True)

# class Favorites(Base):
#     __tablename__ = 'favorites'
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
#     character_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
#     planet_id = Column(Integer, ForeignKey('planets.id'), nullable=False)
#     starship_id = Column(Integer, ForeignKey('starships.id'), nullable=False)


# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
