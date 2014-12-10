def reverse_string(word):
  output = ''
  letters = []
  if type(word) is str:
    for letter in word:
      letters.append(letter)
  
    letters.reverse()

    for letter in letters:
      output += letter
  
    return output
  else:
    return False