def create_row(num_seats):
  "Create what a row looks like. Aisles is an array of indicies specifying where aisle should separate seats"
  row = []

  # Create seats
  for i in range(0, num_seats):
    row.append([])

  return row

def generate_seat_map(rows, seats_in_row):
  seat_map = []
  seats = 0
  row = []
  while seats < seats_in_row:
    row.append([]);
  return seat_map
