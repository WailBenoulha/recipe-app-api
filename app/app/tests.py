from django.test import SimpleTestCase
from . import calcs

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        res = calcs.add(5,6)
        self.assertEqual(res,11)
    
    def test_substract(self):
        res = calcs.substract(10,15)
        self.assertEqual(res,5)
