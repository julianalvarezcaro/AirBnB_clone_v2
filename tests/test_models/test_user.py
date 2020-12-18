#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pep8
from models.base_model import BaseModel
import unittest


class test_User(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    # def test_doc(self):
    #     """
    #     Tests if everything is documented
    #     """
    #     #  Module check
    #     self.assertIsNotNone(console.__doc__)

    #     #  Class check
    #     self.assertIsNotNone(HBNBCommand.__doc__)

    #     # Methods check
    #     for method in dir(HBNBCommand):
    #         self.assertIsNotNone(method.__doc__)

    def test_pep8(self):
        """ Style pep8 """
        style = pep8.StyleGuide(quiet=True)
        # f1 = 'user.py'
        # f2 = 'tests/test_console.py'
        # result = style.check_files([f1, f2])
        result = style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")
        # self.assertEqual(True,True)

    # def test_first_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.first_name), str)

    # def test_last_name(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.last_name), str)

    # def test_email(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.email), str)

    # def test_password(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.password), str)


if __name__ == '__main__':
    unittest.main()
