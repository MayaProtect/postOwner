import re
import bcrypt
from uuid import uuid4
from bson.binary import Binary


class Owner:
    def __init__(self, request: dict):
        if type(request["firstname"]) is not str:
            raise TypeError("Firstname must be a string")

        if len(request["firstname"]) < 3:
            raise ValueError("Firstname must be longer than 3 characters")

        if type(request["lastname"]) is not str:
            raise TypeError("Lastname must be a string")

        if len(request["lastname"]) < 3:
            raise ValueError("Lastname must be longer than 3 characters")

        if type(request["email"]) is not str:
            raise TypeError("Email must be a string")

        if self.check_email(request["email"]) is False:
            raise ValueError("Email must be valid")

        self.firstname = request["firstname"]
        self.lastname = request["lastname"]
        self.email = request["email"]
        self.password = request["password"]
        self.id = uuid4()

    @staticmethod
    def check_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if re.fullmatch(regex, email):
            return True
        else:
            return False

    def to_save_data(self):
        return {
            "uuid": Binary.from_uuid(self.id),
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password
        }

    def to_respond(self):
        return {
            "id": str(self.id),
            "name": self.firstname + " " + self.lastname
        }
