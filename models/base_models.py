#!/usr/bin/python3
"""
This is the base model of the for airbnb clone given as a task by ALX.
"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """
    This is the base model for the airbnb clone.
    """
    def __init__(self, *args, **kwargs):
        """
        initializes the base model object.
        """
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
