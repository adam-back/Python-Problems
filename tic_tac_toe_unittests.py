import unittest
import tictactoe

class tic_tac_toe_TestCase(unittest.TestCase):
  def test_pass(self):
    self.assertTrue(True)

  def test_make_board(self):
    board = tictactoe.make_board()
    self.assertEqual(board, [["_","_","_"],
                             ["_","_","_"],
                             ["_","_","_"]]);
    
if __name__ == '__main__':
    unittest.main()