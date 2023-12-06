#!/usr/bin/python3
"""
This class defines the Place model for hbnb
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    This class defines the Place model for hbnb
    """
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

