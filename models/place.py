#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    # Volver columnas
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    # Crear relacion con Review
    # Instance of SQLAlchemy Table called place_amenity

    # Condicional entre DBStorage y FileStorage
