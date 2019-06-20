import unittest
from lab0 import *

 class TestLab1(unittest.TestCase):

     def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

     # Add more tests!

 if __name__ == "__main__":
        unittest.main()
