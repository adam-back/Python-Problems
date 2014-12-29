import unittest
from airplaneBoarding import create_row, generate_seat_map

class flattenTestCase(unittest.TestCase):
  def test_create_row_CRJ700(self):
    "Create a row with 4 seats for CRJ 700"
    row = create_row(4,[2])
    self.assertEqual(row, [[],[],'',[],[]] )
  
  def test_create_row_747(self):
    "Create a row for 747"
    row = create_row(11,[3,8])
    self.assertEqual(row, [[],[],[],'',[],[],[],[],[],'',[],[],[]] )

  def test_create_row_odd_config(self):
    "Create a 1x2 row"
    row = create_row(3, [1])
    self.assertEqual(row, [[],'',[],[]] )

  def test_create_seat_map_CRJ700(self):
    "Create seat map for CRJ700"
    seat_map = generate_seat_map(13, 4, [2])
    self.assertEqual(seat_map, [
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]],
                                [[],[],'',[],[]]
                                ])

if __name__ == '__main__':
    unittest.main()