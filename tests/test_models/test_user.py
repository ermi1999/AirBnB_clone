#!/usr/bin/python3
"""
This program handles the test cases for user model of airbnb clone.
"""
from models.base_model import BaseModel
from models import storage
from models.user import User
import unittest


class TestBaseModel(unittest.TestCase):
    """
    This class handles the test cases for user model of airbnb clone.
    """
    def setUp(self):
        self.new_user = User()
        self.new_user.first_name = "Ermiyas"
        self.new_user.last_name = "Abiye"
        self.new_user.email = "ermiyasabiye1999@gmail.com"
        self.new_user.password = "something"
        self.id = "{}.{}".format(self.new_user.__class__.__name__,
                                 self.new_user.id)
        self.all_objs = storage.all()

    def test_attributes(self):
        attributes = ["first_name", "id", "last_name", "email",
                      "created_at", "updated_at", "password"]
        for attribute in attributes:
            self.assertIn(attribute, self.new_user.__dict__.keys())

    def test_storage(self):
        self.assertIn(self.id, self.all_objs.keys())

    def test_values(self):
        loaded_model = self.all_objs[self.id]
        self.assertEqual(loaded_model.id, self.new_user.id)
        self.assertEqual(loaded_model.created_at, self.new_user.created_at)
        self.assertEqual(loaded_model.first_name, self.new_user.first_name)
        self.assertEqual(loaded_model.last_name, self.new_user.last_name)

    def test_type(self):
        loaded_model = self.all_objs[self.id]
        self.assertNotIsInstance(type(loaded_model), type(self.new_user))
