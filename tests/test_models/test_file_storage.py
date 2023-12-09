#!/usr/bin/python3
"""
This program handles the test cases for file_storage of airbnb clone.
"""
from models.base_model import BaseModel
from models import storage
import unittest


class TestBaseModel(unittest.TestCase):
    """
    This class handles the test cases for file_storage of airbnb clone.
    """

    def setUp(self):
        self.new_model = BaseModel()
        self.new_model.my_num = 24
        self.new_model.name = "Ermiyas"
        self.new_model.save()
        self.id = "{}.{}".format(self.new_model.__class__.__name__,
                                 self.new_model.id)
        self.all_objs = storage.all()

    def test_storage(self):
        self.assertIn(self.id, self.all_objs.keys())

    def test_values(self):
        loaded_model = self.all_objs[self.id]
        self.assertEqual(loaded_model.id, self.new_model.id)
        self.assertEqual(loaded_model.created_at, self.new_model.created_at)
        self.assertEqual(loaded_model.name, self.new_model.name)
        self.assertEqual(loaded_model.my_num, self.new_model.my_num)

    def test_type(self):
        loaded_model = self.all_objs[self.id]
        self.assertNotIsInstance(
            type(loaded_model), type(self.new_model))
