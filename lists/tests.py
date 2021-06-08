from functools import cmp_to_key
from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1,3)

