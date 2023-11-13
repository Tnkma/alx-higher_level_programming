#!/usr/bin/python3
import unittest
from models.base import Base
"""
Imports the different class for
each methods
"""

class TestBase(unittest.TestCase):

    def test_init(self):
        obj = Base(12)
        self.assertEqual(obj.id, 12)


if __name__ == '__main__':
    unittest.main()
