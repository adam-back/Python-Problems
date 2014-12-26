import unittest
from flat import flatten, findNonParen

class flattenTestCase(unittest.TestCase):
  def test_pass(self):
    self.assertTrue(True)

  def test_index_1(self):
    index = findNonParen([9])
    self.assertEqual(index, 1)

  def test_index_2(self):
    index = findNonParen([[9]])
    self.assertEqual(index, 2)

  def test_index_2_moreBrackets(self):
    index = findNonParen([[9,2], [2,3]])
    self.assertEqual(index, 2)

  def test_index_for_flatten(self):
    index = findNonParen([[[[1,2,3], ['a','b','c']]]])
    self.assertEqual(index, 4)

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