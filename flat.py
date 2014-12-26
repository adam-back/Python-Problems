def findNonParen(list_as_string):
  index = 0
  for char in str(list_as_string):
    if char != '[':
      return index
    else:
      index += 1

  return -1

def flatten(list_of_lists):
  # turn input into string
  # iterate through looking for first non-[ character
  # look for next ] character
  # splice everything between those two indicies into an output variable
  # search from ] for next non-[ char, repeat above process
  return list_with_removed_parens