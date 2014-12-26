import unittest
from flat import flatten

class flattenTestCase(unittest.TestCase):
  def test_pass(self):
    self.assertTrue(True)

  def test_flatten_array_1(self):
    flattendedArray = flatten([[[[1,2,3] , ['a','b','c']]]])
    self.assertEqual(flattendedArray, [[1,2,3], ['a','b','c']])

  def test_flatten_array_2(self):
    flattendedArray = flatten([[[1,2,3] , ['a','b','c']]])
    self.assertEqual(flattendedArray, [[1,2,3], ['a','b','c']])

  def test_flatten_array_3(self):
    flattendedArray = flatten([[[1,2,3]] , [['a','b','c']]])
    self.assertEqual(flattendedArray, [[1,2,3], ['a','b','c']])
    
if __name__ == '__main__':
    unittest.main()