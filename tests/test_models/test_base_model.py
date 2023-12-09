#!/usr/bin/python3
"""
This program handles the test cases for base_model of airbnb clone.
"""
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """
    This object handles the test cases for BaseModel object.
    """
    def setUp(self):
        self.base = BaseModel()

    def test_id(self):
        self.assertIsInstance(self.base.id, str)

    def test_to_dict(self):
        self.assertIsInstance(self.base.to_dict(), dict)

    def test_save(self):
        temp_date = self.base.updated_at
        self.base.save()
        self.assertNotEqual(self.base.updated_at, temp_date)

    def test_str(self):
        self.assertIsInstance(self.base.__str__(), str)

    def test_assign(self):
        self.base.name = "Ermiyas"
        self.assertEqual(self.base.name, "Ermiyas")

    def test_toDict(self):
        available_keys = ["name", "__class__",
                          "updated_at", "id", "created_at"]
        my_dict = self.base.to_dict()
        for key in my_dict.keys():
            self.assertIn(key, available_keys)

    def test_fromDict(self):
        my_dict = self.base.to_dict()
        new_model = BaseModel(**my_dict)
        self.assertEqual(self.base.id, new_model.id)
        self.assertEqual(self.base.id, new_model.id)
        self.assertEqual(self.base.created_at, new_model.created_at)
        self.assertEqual(self.base.updated_at, new_model.updated_at)
        self.assertEqual(
            type(self.base.created_at), type(new_model.created_at))


if __name__ == "__main__":
    unittest.main()
