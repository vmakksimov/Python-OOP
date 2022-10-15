from collections import deque

def best_list_pureness(*test):
    rotate_count = int(test[1])
    numbers_to_rotate = deque((test[0]))

    final_rotation = None
    max_number = -9999999
    for big_rotation in range(rotate_count +1):
        final_result = sum([numbers_to_rotate[index] * index for index in range(len(numbers_to_rotate))])
        numbers_to_rotate.appendleft(numbers_to_rotate.pop())

        if final_result > max_number:
            max_number = final_result
            final_rotation = big_rotation


    return f'Best pureness {max_number} after {final_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
