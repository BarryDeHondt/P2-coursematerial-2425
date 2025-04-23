###############
#
# This is your favorite file!
# Write your tests here
#
###############

import unittest
from dog import *
from student import *


class TestFromSameNest(unittest.TestCase):

    def setUp(self):
        self.father = Dog("Rex Sr", "Labrador", "black", 2010)
        self.mother = Dog("Bella Sr", "Labrador", "brown", 2011)

        self.dog1 = Dog("Max", "Labrador", "black", 2020, self.father, self.mother)
        self.dog2 = Dog("Luna", "Labrador", "black", 2020, self.father, self.mother)
        self.dog3 = Dog("Charlie", "Labrador", "black", 2021, self.father, self.mother)  # different year
        self.dog4 = Dog("Milo", "Labrador", "black", 2020, None, self.mother)  # different father
        self.dog5 = Dog("Daisy", "Labrador", "black", 2020, self.father, None)  # different mother

    def test_same_nest(self):
        self.assertTrue(from_same_nest(self.dog1, self.dog2))

    def test_same_dog(self):
        self.assertFalse(from_same_nest(self.dog1, self.dog1))

    def test_different_birth_year(self):
        self.assertFalse(from_same_nest(self.dog1, self.dog3))

    def test_different_father(self):
        self.assertFalse(from_same_nest(self.dog1, self.dog4))

    def test_different_mother(self):
        self.assertFalse(from_same_nest(self.dog1, self.dog5))

if __name__ == "__main__":
    unittest.main()