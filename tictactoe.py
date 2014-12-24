# def tic_tac_toe(board, choices):

# def place_choice(marker, x, y):

# def check_rows():

# def check_columns():

# def check_diagonals():

# def computer_choice():

def make_board():
  board = []

  for i in range(3):
    board.append(["_","_","_"])

  # 3x3 matrix
  return board

def print_board(board):
  row = 0
  # Try to edit copy, not original <---- Currently not working
  pretty_board = board
  # for all rows on the board
  while row < len(pretty_board):
    # insert the row number at the front of the sub-array
    pretty_board[row].insert(0, row + 1)
    # move on to the next row
    row += 1

  # Add column references
  pretty_board.insert(0, ['','A','B','C'])

  # print pretty_board

  # return only for testing purposes
  return pretty_board

# Make a board
# Flip a coin, decide if user or AI goes first
# Print board with rows and columns (pretty print)
# Prompt user for choices
# Print new board with piece placed
  # Check for win or lose
# Complete until win or cat's game occurs