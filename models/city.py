#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel  # Verificar importacion por Base


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    # Volverlos columnas
    state_id = ""
    name = ""

    # Crear relacion con Place
