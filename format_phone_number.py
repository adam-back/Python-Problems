# Given a string or number which includes a user's phone number,
# format the phone number as (123) 456-7890 and return it.
# The number may be 7 or 10 digits.
#
# See format_phone_number_unittests.py for cases.
import re

def pretty_print_phone(userPhone):
  if (type(userPhone) is int) or (type(userPhone) is str):
    #find all numbers 
    numbers = find_all_numbers(userPhone)

    if len(numbers) == 7 or len(numbers) == 10:
      #place - after third number
      return True
    else:
      #return False because the numbers are too many/few 
      return False
  else:
    return False

def find_all_numbers(n):
  found_numbers = ''
  numbers =  re.findall('[0-9]', str(n))
  return numbers