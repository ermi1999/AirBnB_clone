#!/usr/bin/python3
"""
This program handles the test cases for amenity model.
"""
import models
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestState(unittest.TestCase):
    """
    This class handles the test cases for amenity model.
    """
    def test_attributes(self):
        amenity = Amenity()
        attributes = ["id", "created_at", "updated_at"]
        for attribute in attributes:
            self.assertIn(attribute, amenity.__dict__.keys())

    def test_type(self):
        self.assertEqual(Amenity, type(Amenity()))
        self.assertIn(Amenity(), models.storage.all().values())
        self.assertEqual(str, type(Amenity().id))
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))
        self.assertEqual(str, type(Amenity.name))
