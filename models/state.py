#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel  # Verificar importacion por Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    # Volver columna
    name = ""

    # Crear relacion con City
