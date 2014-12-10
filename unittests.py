import unittest
from reverse_string import reverse_string

class reverseStringTestCase(unittest.TestCase):
  def test_pass(self):
    self.assertTrue(True)

  def test_reverse_string(self):
    backwards = reverse_string('adam')
    self.assertEqual(backwards, 'mada')

if __name__ == '__main__':
    unittest.main()