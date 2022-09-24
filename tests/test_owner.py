import unittest
from urllib import request
from app import Owner


class TestOwner(unittest.TestCase):
    def test_firstname_value_error(self):
        request = {
            "firstname": "p",
            "lastname": "samir",
            "email": "sam@free.fr",
            "password": "azerty"
        }
        with self.assertRaises(ValueError):
            owner = Owner(request)
            
# au moins 11tests

# test check_mail qui renvoi true ou false

