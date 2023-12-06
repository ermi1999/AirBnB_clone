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

        def test_save(self):
        base = BaseModel()
        temp_date = base.updated_at
        base.save()
        self.assertNotEqual(base.updated_at, temp_date)

    def test_str(self):
        base = BaseModel()
        self.assertIsInstance(base.__str__(), str)


if __name__ == "__main__":
    unittest.main()


