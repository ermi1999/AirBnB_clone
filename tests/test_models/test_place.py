#!/usr/bin/python3
"""
This program handles the test cases for place model.
"""
import models
import unittest
from datetime import datetime
from models.place import Place


class TestState(unittest.TestCase):
    """
    This class handles the test cases for place model.
    """
    def test_attributes(self):
        place = Place()
        attributes = ["id", "created_at", "updated_at"]
        for attribute in attributes:
            self.assertIn(attribute, place.__dict__.keys())

    def test_type(self):
        self.assertEqual(Place, type(Place()))
        self.assertIn(Place(), models.storage.all().values())
        self.assertEqual(str, type(Place().id))
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(datetime, type(Place().updated_at))
        self.assertEqual(str, type(Place.user_id))
        self.assertEqual(str, type(Place.name))
        self.assertEqual(str, type(Place.description))
        self.assertEqual(int, type(Place.number_rooms))
        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertEqual(int, type(Place.max_guest))
        self.assertEqual(int, type(Place.price_by_night))
        self.assertEqual(float, type(Place.latitude))
        self.assertEqual(float, type(Place.longitude))
        self.assertEqual(list, type(Place.amenity_ids))
