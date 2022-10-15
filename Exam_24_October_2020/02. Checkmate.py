def check(r, c, num):
    if 0 <= r < num and 0 <= c < num:
        return True
    return False


matrix = []
for _ in range(8):
    matrix.append(input().split())

king_row, king_col = 0, 0

queens_positions = []
for col in range(8):
    for row in range(8):
        if matrix[row][col] == 'K':
            king_row, king_col = row, col
        elif matrix[row][col] == 'Q':
            queens_positions.append([row, col])


queen_direction = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c),
    'diagonall_down_right': lambda r, c: (r + 1, c + 1),
    'diagonall_down_left': lambda r,c: (r +1, c -1),
    'diagonall_up_lef': lambda r, c: (r -1, c -1),
    'diagonall_up_right': lambda r, c: (r -1, c+ 1),
}
queens_path = []

is_found = False
for position in queens_positions:
    for key, value in queen_direction.items():
        current_row, current_cow = position[0], position[1]
        while queen_direction:
            is_found = False
            next_row, next_cow = value(current_row, current_cow)
            #if check(next_row, next_cow, 8):
            if matrix[next_row][next_cow] == 'K':
                queens_path.append([position[0], position[1]])
                is_found = True
                break
            elif matrix[next_row][next_cow] == 'Q':
                break
            else:
                current_row, current_cow = next_row, next_cow

        if is_found:
            break

if len(queens_path) > 0:
    for el in queens_path:
        print(el)
else:
    print('The king is safe!')