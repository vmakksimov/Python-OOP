def check(nums, r, c):
    if 0 <= r < nums and 0 <= c < nums:
        return True
    return False


letters = list(input())
num = int(input())

matrix = []
for _ in range(num):
    matrix.append(list(input()))

player_row, player_col = 0, 0
for row in range(num):
    for col in range(num):
        if matrix[row][col] == 'P':
            player_row, player_col = row, col

direction = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c),
}
current_row, current_col = player_row, player_col

for commands in range(int(input())):
    act = input()
    for key, value in direction.items():
        if act == key:
            next_row, next_col = value(current_row, current_col)
            if check(num, next_row, next_col):
                if matrix[next_row][next_col] != '-':
                    letters.append(matrix[next_row][next_col])

                matrix[next_row][next_col] = 'P'
                matrix[current_row][current_col] = '-'
                current_row, current_col = next_row, next_col
            else:
                if len(letters) > 0:
                    letters.pop()
result = ''
for el in letters:
    result += el
print(result)
for el in matrix:
    print(f'{"".join(el)}')
