#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import unittest
import pep8
from models.base_model import BaseModel


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_doc(self):
        """
        Tests if everything is documented
        """
        #  Module check
        self.assertIsNotNone(console.__doc__)

        #  Class check
        self.assertIsNotNone(HBNBCommand.__doc__)

        # Methods check
        for method in dir(HBNBCommand):
            self.assertIsNotNone(method.__doc__)

    def test_pep8(self):
        """ Style pep8 """
        style = pep8.StyleGuide(quiet=True)
        # f1 = 'place.py'
        # f2 = 'tests/test_console.py'
        # result = style.check_files([f1, f2])
        result = style.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0, "fix pep8")
        # self.assertEqual(True,True)

    # def test_city_id(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.city_id), str)

    # # def test_user_id(self):
    # #     """ """
    # #     new = self.value()
    # #     self.assertEqual(type(new.user_id), str)

    # # def test_name(self):
    # #     """ """
    # #     new = self.value()
    # #     self.assertEqual(type(new.name), str)

    # def test_description(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.description), str)

    # # def test_number_rooms(self):
    # #     """ """
    # #     new = self.value()
    # #     self.assertEqual(type(new.number_rooms), int)

    # # def test_number_bathrooms(self):
    # #     """ """
    # #     new = self.value()
    # #     self.assertEqual(type(new.number_bathrooms), int)

    # def test_max_guest(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.max_guest), int)

    # # def test_price_by_night(self):
    # #     """ """
    # #     new = self.value()
    # #     self.assertEqual(type(new.price_by_night), int)

    # def test_latitude(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.latitude), float)

    # def test_longitude(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.latitude), float)

    # def test_amenity_ids(self):
    #     """ """
    #     new = self.value()
    #     self.assertEqual(type(new.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
