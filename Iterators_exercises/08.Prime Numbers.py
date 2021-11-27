def is_primer(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    for i in range(2, number):
        if number % i == 0:
            return False

    return True




def get_primes(numbers):
    for num in numbers:
        if is_primer(num):
            yield num




print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))