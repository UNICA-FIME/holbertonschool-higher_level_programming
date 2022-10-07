#!/usr/bin/python3
"""
Contains tests for base class

"""
from models.base import Base
import unittest

class TestBaseClass(unittest.TestCase):
    
    def test_assig_id(self):
        base1 = Base(1)
        self.assertEqual(base1.id, 1)

if __name__ == '__main__':
    unittest.main()
