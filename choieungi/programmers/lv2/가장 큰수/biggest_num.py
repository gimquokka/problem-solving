def solution(numbers):
    answer = ''
    str_numbers = []
    for i in numbers:
        temp = ''
        while len(temp) < 5:
            temp += str(i)
        str_numbers.append((str(i), temp[:5]))

    str_numbers.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(numbers)):
        answer += str_numbers[i][0]

    return "0" if answer[0] == '0' else answer