import unittest
from airplaneBoarding import create_row

class flattenTestCase(unittest.TestCase):
  def test_pass(self):
    self.assertTrue(True)

  def test_create_row(self):
    "Create a row with 4 seats"
    row = create_row(4)
    self.assertEqual(row, [[],[],[],[]] )
    
if __name__ == '__main__':
    unittest.main()