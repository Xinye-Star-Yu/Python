import unittest
from lab1 import *

# A few test cases. You shoud add more of your own!
class TestLab1(unittest.TestCase):

	def test_max_list_iter_None_List(self):
		# test
		tlist = None
		with self.assertRaises(ValueError):  # used to check for exception
			max_list_iter(tlist)
	
	def test_max_list_iter_empty_List(self):
		self.assertEqual(max_list_iter([]), None)

	def test_max_list_iter_max_List(self):
		self.assertEqual(max_list_iter([1,2,3]), 3)

	def test_reverse_rec(self):
		self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
	
	def test_reverse_rec_None_List(self):
		# test
		tlist = None
		with self.assertRaises(ValueError):  # used to check for exception
			reverse_rec(tlist)

	def test_bin_search_ValueError(self):
		list_val = None
		with self.assertRaises(ValueError):
			bin_search(0, 0, 9, list_val)
	
	def test_bin_search_length_0(self):
		list_val = []
		self.assertEqual(bin_search(0, 0, len(list_val) -1, list_val), None)
	
	def test_bin_search(self):
		list_val =[0,1,2,3,4,7,8,9,10]
		low = 0
		high = len(list_val)-1
		self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
	
	def test_bin_search_target(self):
		list_val =[0,1,2,3,4,7,8,9,10]
		low = 0
		high = len(list_val)-1
		self.assertEqual(bin_search(5, 0, len(list_val)-1, list_val), None)
		

if __name__ == "__main__":
	unittest.main()
