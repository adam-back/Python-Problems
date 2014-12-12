import unittest
from format_phone_number import pretty_print_phone

class TestCases(unittest.TestCase):
  def test_pass(self):
    self.assertTrue(True)

  def pretty_print_phone1(self):
    pretty = pretty_print_phone(1234567)
    self.assertTrue(pretty, '123-4567')
    
  def pretty_print_phone2(self):
    pretty = pretty_print_phone('123-4567')
    self.assertTrue(pretty, '123-4567')

  def pretty_print_phone3(self):
    pretty = pretty_print_phone('123 4567')
    self.assertTrue(pretty, '123-4567')

  def pretty_print_phone4(self):
    pretty = pretty_print_phone(12345678)
    self.assertTrue(pretty, False)

  def pretty_print_phone5(self):
    pretty = pretty_print_phone(1234567890)
    self.assertTrue(pretty, '(123) 456-7890')

  def pretty_print_phone6(self):
    pretty = pretty_print_phone('123-456-7890')
    self.assertTrue(pretty, '(123) 456-7890')

  def pretty_print_phone7(self):
    pretty = pretty_print_phone('123-456-7890')
    self.assertTrue(pretty, '(123) 456-7890')

  def pretty_print_phone8(self):
    pretty = pretty_print_phone('123 4 56 7890')
    self.assertTrue(pretty, '(123) 456-7890')

  def pretty_print_phone9(self):
    pretty = pretty_print_phone('123 4 56-7890')
    self.assertTrue(pretty, '(123) 456-7890')

  def pretty_print_phone10(self):
    pretty = pretty_print_phone('(123 X 4 56-7890')
    self.assertTrue(pretty, '(123) 456-7890')

   def pretty_print_phone11(self):
    pretty = pretty_print_phone('(123 0 4 56-7890')
    self.assertTrue(pretty, False)

if __name__ == '__main__':
    unittest.main()