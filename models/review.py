#!/usr/bin/python3
"""
This class defines the Review model for hbnb
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This class defines the Review model for hbnb
    """
    place_id = ""
    user_id = ""
    text = ""

