#!/usr/bin/python3
"""
This program handles the test cases for review model.
"""
import models
import unittest
from datetime import datetime
from models.review import Review


class TestState(unittest.TestCase):
    """
    This class handles the test cases for review model.
    """
    def test_attributes(self):
        review = Review()
        review.place_id = "something"
        review.text = "nice place"
        review.user_id = "something"
        attributes = ["id", "created_at", "updated_at",
                      "place_id", "user_id", "text"]
        for attribute in attributes:
            self.assertIn(attribute, review.__dict__.keys())

    def test_type(self):
        self.assertEqual(Review, type(Review()))
        self.assertIn(Review(), models.storage.all().values())
        self.assertEqual(str, type(Review().id))
        self.assertEqual(str, type(Review().place_id))
        self.assertEqual(str, type(Review().user_id))
        self.assertEqual(str, type(Review().text))
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))
