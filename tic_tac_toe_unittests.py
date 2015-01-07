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

  def test_print_board_pretty(self):
    board = tictactoe.make_board()
    prettyBoard = tictactoe.print_board(board);
    # Should print pretty, but not change original
    self.assertEqual(prettyBoard, [['','A','B','C'],
                                   [1, "_","_","_"],
                                   [2, "_","_","_"],
                                   [3, "_","_","_"]])
  
  def test_pretty_shouldnt_change_original_board(self): # <---- Not passing. Fn changes original input
    # # Shouldn't change the original board
    board = tictactoe.make_board()
    prettyBoard = tictactoe.print_board(board);
    self.assertEqual(board, [["_","_","_"],
                             ["_","_","_"],
                             ["_","_","_"]])
    
if __name__ == '__main__':
    unittest.main()