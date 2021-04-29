from collections import deque


def solution(numbers):
    answer = ''
    str_numbers = []
    for i in numbers:
        str_numbers.append(str(i))
    str_numbers.sort(key=lambda x: x[0])

    while str_numbers:
        if len(str_numbers) > 1:
            if str_numbers[-1][0] != str_numbers[-2][0]:
                answer += str_numbers.pop()
            elif str_numbers[-1][0] == str_numbers[-2][0] and len(str_numbers[-1]) == len(str_numbers[-2]):
                answer += str_numbers.pop()
            else:
                answer += str_numbers.pop() if str_numbers[-1][-1] > str_numbers[-2][0] else str_numbers.pop(-2)
        else:
            answer += str_numbers.pop()

    return answer