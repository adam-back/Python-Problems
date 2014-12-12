# Given a string or number which includes a user's phone number,
# format the phone number as (123) 456-7890 and return it.
# The number may be 7 or 10 digits.
#
# See format_phone_number_unittests.py for cases.
import re

def pretty_print_phone(userPhone):
  if (type(userPhone) is int) or (type(userPhone) is str):
    #find all numbers 
    #if 7 numbers
      #place - after third number
    #else if 10 number
      #place (), space, and -
    #else
      #return False because the numbers are too many/few 
      return True
  else:
    return False

def find_all_numbers(n):
  found_numbers = ''
  numbers =  re.findall('[0-9]', str(n))
  for digit in numbers:
   found_numbers += digit
  return found_numbers