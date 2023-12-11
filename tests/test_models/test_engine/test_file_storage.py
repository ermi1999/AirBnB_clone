#!/usr/bin/python3
"""
This program handles the test cases for file_storage of airbnb clone.
"""
from models.base_model import BaseModel
from models import storage
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
import models


class TestBaseModel(unittest.TestCase):
    """
    This class handles the test cases for file_storage of airbnb clone.
    """
    def test_file_storage_initiation(self):
        self.assertEqual(type(FileStorage()), FileStorage)
        self.assertEqual(type(models.storage), FileStorage)
        with self.assertRaises(TypeError):
            FileStorage(True)

    def test_new(self):
        user = User()
        state = State()
        base = BaseModel()
        amn = Amenity()
        city = City()
        place = Place()
        rview = Review()
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(base)
        models.storage.new(amn)
        models.storage.new(city)
        models.storage.new(place)
        models.storage.new(rview)
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())
        self.assertIn("Amenity." + amn.id, models.storage.all().keys())
        self.assertIn(amn, models.storage.all().values())
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())
        self.assertIn("Review." + rview.id, models.storage.all().keys())
        self.assertIn(rview, models.storage.all().values())

    def test_save(self):
        state = State()
        place = Place()
        base = BaseModel()
        user = User()
        city = City()
        review = Review()
        amenity = Amenity()
        models.storage.new(base)
        models.storage.new(place)
        models.storage.new(user)
        models.storage.new(amenity)
        models.storage.new(state)
        models.storage.new(review)
        models.storage.new(city)
        models.storage.save()
        with open("file.json", "r") as f:
            save = f.read()
            self.assertIn("User." + user.id, save)
            self.assertIn("BaseModel." + base.id, save)
            self.assertIn("Place." + place.id, save)
            self.assertIn("State." + state.id, save)
            self.assertIn("Amenity." + amenity.id, save)
            self.assertIn("City." + city.id, save)
            self.assertIn("Review." + review.id, save)

    def test_reload(self):
        base = BaseModel()
        state = State()
        user = User()
        place = Place()
        amenity = Amenity()
        city = City()
        review = Review()
        models.storage.new(user)
        models.storage.new(base)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(state)
        models.storage.new(review)
        models.storage.new(amenity)
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn("User." + user.id, objects)
        self.assertIn("BaseModel." + base.id, objects)
        self.assertIn("Place." + place.id, objects)
        self.assertIn("State." + state.id, objects)
        self.assertIn("City." + city.id, objects)
        self.assertIn("Review." + review.id, objects)
        self.assertIn("Amenity." + amenity.id, objects)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)
