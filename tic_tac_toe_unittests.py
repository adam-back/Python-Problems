import unittest
import tictactoe

class tic_tac_toe_TestCase(unittest.TestCase):
  def test_pass(self):
    self.assertTrue(True)

  def test_reverse_string(self):
    backwards = reverse_string('adam')
    self.assertEqual(backwards, 'mada')
    
if __name__ == '__main__':
    unittest.main()