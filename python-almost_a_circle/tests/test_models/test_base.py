#!/usr/bin/python3
"""
Unisttest for class Base
"""
from models.base import Base
import unittest

class TestBaseClass(unittest.TestCase):
    """
    Testing Base
    """
    def test_casebase(self):
        """Test of instantiation"""
        case_1 = Base()
        self.assertEqual(case_1.id, 1)

if __name__ == "__main__":
    unittest.main()

