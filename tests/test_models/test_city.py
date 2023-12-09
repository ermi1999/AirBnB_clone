#!/usr/bin/python3
"""
This program handles the test cases for city model.
"""
import models
import unittest
from datetime import datetime
from models.city import City


class TestState(unittest.TestCase):
    """
    This class handles the test cases for city model.
    """
    def test_attributes(self):
        city = City()
        attributes = ["id", "created_at", "updated_at"]
        for attribute in attributes:
            self.assertIn(attribute, city.__dict__.keys())

    def test_type(self):
        self.assertEqual(City, type(City()))
        self.assertIn(City(), models.storage.all().values())
        self.assertEqual(str, type(City().id))
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))
        self.assertEqual(str, type(City.state_id))
        self.assertEqual(str, type(City.name))
