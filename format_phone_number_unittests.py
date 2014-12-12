import unittest
from format_phone_number import pretty_print_phone

class TestCases(unittest.TestCase):

  def test_phone_7_nums_only(self):
    pretty = pretty_print_phone(1234567)
    self.assertTrue(pretty, '123-4567')
    
  def test_phone_7_already_formatted(self):
    pretty = pretty_print_phone('123-4567')
    self.assertTrue(pretty, '123-4567')

  def test_phone_7_space(self):
    pretty = pretty_print_phone('123 4567')
    self.assertTrue(pretty, '123-4567')

  def test_phone_8(self):
    pretty = pretty_print_phone(12345678)
    self.assertTrue(pretty, False)

  def test_phone_10_nums_only(self):
    pretty = pretty_print_phone(1234567890)
    self.assertTrue(pretty, '(123) 456-7890')

  def test_phone_10_dashes(self):
    pretty = pretty_print_phone('123-456-7890')
    self.assertTrue(pretty, '(123) 456-7890')

  def test_phone_10_spaces(self):
    pretty = pretty_print_phone('123 4 56 7890')
    self.assertTrue(pretty, '(123) 456-7890')

  def test_phone_10_mixed1(self):
    pretty = pretty_print_phone('123 4 56-7890')
    self.assertTrue(pretty, '(123) 456-7890')

  def test_phone_10_mixed2(self):
    pretty = pretty_print_phone('(123 X 4 56-7890')
    self.assertTrue(pretty, '(123) 456-7890')

  def test_phone_11(self):
    pretty = pretty_print_phone('(123 0 4 56-7890')
    self.assertTrue(pretty, False)

if __name__ == '__main__':
  unittest.main()