#!/usr/bin/python3
"""This module contains unit tests for the functions and classes defined in the
user model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Defines a test class for User"""

    def __init__(self, *args, **kwargs):
        """Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Defines test for first_name"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """Defines tests for last_name"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """Defines tests for test_email"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """Defines tests for password"""
        new = self.value()
        self.assertEqual(type(new.password), str)
