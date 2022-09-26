import unittest
from urllib import request
from app import Owner


class TestOwner(unittest.TestCase):
    def setUp(self):
        self.request = {
            "firstname": "p",
            "lastname": "samir",
            "email": "sam@free.fr",
            "password": "azerty"
        }
    
    def test_firstname_value_error(self):
        with self.assertRaises(ValueError):
            owner = Owner(self.request)
    
    def test_owner_is_instance_of_owner(self):
        o = Owner(self.request)
        self.assertIsInstance(o, Owner)

    def test_check_email_is_false(self):
        self.assertFalse(self.request["email"])

    def test_check_synthaxe_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        self.assertRaises(self.request["email"] , regex)

    def test_lengt_for_firstname(self):
        self.assertTrue(len(self.request["firstname"]) > 3)

    def test_lengt_for_lastname(self):
        self.assertTrue(len(["lastname"]) > 3)



