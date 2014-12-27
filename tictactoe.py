import random

# def tic_tac_toe(board, choices):

# def place_choice(board, marker, x, y):

# def check_rows(board):

# def check_columns(board):

# def check_diagonals(board):

# def computer_choice():

def make_board():
  newBoard = []

  for i in range(3):
    newBoard.append(["_","_","_"])

  # 3x3 matrix
  return newBoard

def print_board(board):
  row = 0
  # Try to edit copy, not original <---- Currently not working
  board
  # for all rows on the board
  while row < len(board):
    # insert the row number at the front of the sub-array
    board[row].insert(0, row + 1)
    # move on to the next row
    row += 1
  # Add column references
  board.insert(0, ['','A','B','C'])
  prettyBoard = board
  # Print pretty board
  print prettyBoard


  # change board back to original states
  while row >= 0:
    # insert the row number at the front of the sub-array
    del board[row][0]
    # move on to the next row
    row -= 1
  del board[0]

  # return only for testing purposes
  return "Original:" + board +"\nPretty:" + prettyBoard


# Make a board
# Flip a coin, decide if user or AI goes first
# Print board with rows and columns (pretty print)
# Prompt user for choices
# Print new board with piece placed
  # Check for win or lose
# Complete until win or cat's game occurs