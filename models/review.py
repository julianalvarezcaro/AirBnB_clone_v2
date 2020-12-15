#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    __tablename__ = 'reviews'
    
    # Volver columnas
    place_id = ""
    user_id = ""
    text = ""
