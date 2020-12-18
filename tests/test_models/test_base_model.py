#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
import pep8


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    # def test_doc(self):
    #     """
    #     Tests if everything is documented
    #     """
    #     #  Module check
    #     # self.assertIsNotNone(console.__doc__)

    #     #  Class check
    #     self.assertIsNotNone(HBNBCommand.__doc__)

    #     # Methods check
    #     for method in dir(HBNBCommand):
    #         self.assertIsNotNone(method.__doc__)

    def test_pep8(self):
        """ Style pep8 """
        style = pep8.StyleGuide(quiet=True)
        # f1 = 'base_model.py'
        # f2 = 'tests/test_console.py'
        # result = style.check_files([f1, f2])
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")
        # self.assertEqual(True,True)

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    # def test_kwargs(self):
    #     """ """
    #     i = self.value()
    #     copy = i.to_dict()
    #     new = BaseModel(**copy)
    #     self.assertFalse(new is i)

    # def test_kwargs_int(self):
    #     """ """
    #     i = self.value()
    #     copy = i.to_dict()
    #     copy.update({1: 2})
    #     with self.assertRaises(TypeError):
    #         new = BaseModel(**copy)

    # def test_save(self):
    #     """ Testing save """
    #     i = self.value()
    #     i.save()
    #     key = self.name + "." + i.id
    #     with open('file.json', 'r') as f:
    #         j = json.load(f)
    #         self.assertEqual(j[key], i.to_dict())

    # def test_str(self):
    #    """ """
    #   i = self.value()
    #    self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
    #                    i.__dict__))

    # def test_todict(self):
    #     """ """
    #     i = self.value()
    #     n = i.to_dict()
    #     self.assertEqual(i.to_dict(), n)

    # def test_kwargs_none(self):
    #     """ """
    #     n = {None: None}
    #     with self.assertRaises(TypeError):
    #         new = self.value(**n)

    # def test_kwargs_one(self):
    #     """ """
    #     n = {'Name': 'test'}
    #     with self.assertRaises(KeyError):
    #         new = self.value(**n)

    # def test_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.id), str)

    # def test_created_at(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.created_at), datetime.datetime)

    # def test_updated_at(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.updated_at), datetime.datetime)
    #     n = new.to_dict()
    #     new = BaseModel(**n)
    #     self.assertFalse(new.created_at == new.updated_at)


if __name__ == '__main__':
    unittest.main()
