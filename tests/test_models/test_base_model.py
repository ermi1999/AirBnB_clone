#!/usr/bin/python3
"""
This program handles the test cases for base_model of airbnb clone.
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """
    This object handles the test cases for BaseModel object.
    """
    def test_id(self):
        base = BaseModel()
        self.assertIsInstance(base.id, str)

        def test_to_dict(self):
        base = BaseModel()
        self.assertIsInstance(base.to_dict(), dict)


