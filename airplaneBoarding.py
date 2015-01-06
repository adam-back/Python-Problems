def create_row(num_seats, aisle):
  "Create what a row looks like. Aisles is an array specifying where aisles should separate seats"
  row = []

  # Create seats
  for i in range(0, num_seats):
    row.append([])

  # Add aisles
  aisle_offset = 0 # to account for list indicies changing
  for location in aisle:
    # location should be the seat before the aisle, from L->R
    row.insert(location + aisle_offset, '')
    aisle_offset += 1

  return row

def generate_seat_map(rows, seats_in_row, aisle):
  "Create a seat map. Aisle is an array of values."
  seat_map = []
  row = create_row(seats_in_row, aisle)

  for row_num in range(0, rows):
    seat_map.append(row)

  return seat_map

def pretty_print_seats(seat_map):
  print "\n"
  for row in range(0, len(seat_map)):
    print str(seat_map[row]) + "\n"