#!/usr/bin/python3
"""
This class serializes instances to a JSON file and deserializes JSON file to instances.
"""
import json


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes JSON
    file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects.
        """
        return self.__objects

    def new(self, obj):
        """
        updates the dictionary __objects with (obj).
        Args:
            obj: The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        data = {}
        for value in self.__objects.values():
            id = "{}.{}".format(value.__class__.__name__, value.id)
            value = value.to_dict()
            data[id] = value
        data = json.dumps(data)
        with open(self.__file_path, "w",) as f:
            f.write(data)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path)
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(self.__file_path, 'r') as f:
                data = json.loads(f.read())
            for value in data.values():
                class_name = value["__class__"]
                del value["__class__"]
                self.new(eval(class_name) (**value))
        except FileNotFoundError:
            pass

