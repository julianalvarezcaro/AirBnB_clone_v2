#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Comment"""
    __tablename__ = 'users'

    # Volver columnas 
    name = ""

    # Crear relacion Many-to-Many place_amenities
