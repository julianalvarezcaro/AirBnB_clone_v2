#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""

    __tablename__ = 'users'

    # Volver columnas
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    # Crear relacion con Place
    # Crear relacion con Review
