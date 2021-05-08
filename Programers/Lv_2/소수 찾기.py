from itertools import permutations


def findPrime(num):
    is_prime = True

    if num in [0, 1]:
        return False

    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            return is_prime

    return is_prime


def solution(numbers):
    cnt = 0
    _len = len(numbers)
    num_list = list(numbers)
    used_num_set = set()

    for i in range(1, _len+1):
        for selected_element in permutations(num_list, i):
            generated_num = int("".join(selected_element))

            if generated_num in used_num_set:
                continue

            used_num_set.add(generated_num)

            if findPrime(int("".join(selected_element))):
                cnt += 1

    return cnt