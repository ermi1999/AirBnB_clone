#!/usr/bin/python3
"""
This class defines the user model for Airbnb clone.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This class defines the user model for Airbnb clone.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

