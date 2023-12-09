#!/usr/bin/python3
"""
This program handles the test cases for state model.
"""
import models
import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):
    """
    This class handles the test cases for state model.
    """
    def test_attributes(self):
        state = State()
        attributes = ["id", "created_at", "updated_at"]
        for attribute in attributes:
            self.assertIn(attribute, state.__dict__.keys())

    def test_type(self):
        self.assertEqual(State, type(State()))
        self.assertIn(State(), models.storage.all().values())
        self.assertEqual(str, type(State().id))
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))
