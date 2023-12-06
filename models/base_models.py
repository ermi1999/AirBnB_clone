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
                    else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        returns the string representation of the base_model object.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the base model.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns the dictionary representation of the base model.
        """
        result = {}

        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                result[key] = value.isoformat()
            else:
                result[key] = value
        result["__class__"] = self.__class__.__name__
        return result
