# Given a string or number which includes a user's phone number,
# format the phone number as (123) 456-7890 and return it.
# The number may be 7 or 10 digits.
#
# See format_phone_number_unittests.py for cases.
import re

def pretty_print_phone(userPhone):

  # A number or string may be entered
  if (type(userPhone) is int) or (type(userPhone) is str):
    #find all numbers 
    numbers = find_all_numbers(userPhone)

    if len(numbers) == 7:
      numbers.insert(3, '-')
      # return numbers.
    elif len(numbers) == 10:
      numbers.insert(0, '(')
      numbers.insert(4, ')')
      numbers.insert(5, ' ')
      numbers.insert(9, '-')
    else:
      #return False because the numbers are too many/few 
      return False
  else:
    # A string or number wasn't passed
    return False

def find_all_numbers(n):
  found_numbers = ''
  numbers =  re.findall('[0-9]', str(n))
  return numbers

def create_string_from_list(list_of_nums):
  output_string = ''
  for number in list_of_nums:
    output_string += number
  return output_string