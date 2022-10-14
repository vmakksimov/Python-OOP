def check(r, c):
    if 0 <= r < 7 and 0 <= c < 7:
        return True
    return False


def check_player(current, counter, first, second):
    if counter % 2 == 0:
        current = second
    elif counter % 2 != 0:
        current = first

    return current


def calculate_d(mat, r, c, box):
    if box.isnumeric():
        return box
    else:
        result = int(mat[r][0]) + int(mat[r][-1]) + int(mat[0][c]) + int(mat[-1][c])
        if box == 'D':
            result *= 2
        elif box == 'T':
            result *= 3
        return result


first_player, second_player = input().split(', ')
first_player_score = 501
second_player_score = 501
matrix = []
hit_counter = 0
for _ in range(7):
    matrix.append(input().split())

first_player_turns = 0
second_player_turns = 0
throw = None
current_player = None
while True:
    command = [int(num) for num in input()[1:-1].split(',')]
    hit_counter += 1
    hit_row, hit_cow = int(command[0]), int(command[1])
    current_player = check_player(current_player, hit_counter, first_player, second_player)
    if current_player == first_player:
        first_player_turns += 1
    elif current_player == second_player:
        second_player_turns += 1

    is_valid = check(hit_row, hit_cow)
    if is_valid:
        current_box = matrix[hit_row][hit_cow]

        if current_box == 'B':
            if current_player == first_player:
                throw = first_player_turns
            elif current_player == second_player:
                throw = second_player_turns
            break

        final_result = calculate_d(matrix, hit_row, hit_cow, current_box)
        
        if current_player == first_player:
            first_player_score -= int(final_result)
            if first_player_score <= 0:
                throw = first_player_turns
                break

        elif current_player == second_player:
            second_player_score -= int(final_result)
            if second_player_score <= 0:
                throw = second_player_turns
                break

print(f'{current_player} won the game with {throw} throws!')