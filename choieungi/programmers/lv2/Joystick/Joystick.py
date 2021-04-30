def solution(name):
    answer = 0
    values = []
    for i in name:
        values.append(min(ord(i) - ord("A"), ord("Z") - ord(i) + 1))
    answer += sum(values)

    location = 0
    while True:
        values[location] = 0
        if (not sum(values)):
            break

        right = 1
        left = 1
        for i in range(1, len(values)):
            if values[location + i] == 0:
                right += 1
            else:
                break

        for i in range(1, len(values)):
            if values[location - i] == 0:
                left += 1
            else:
                break
        if right > left:
            answer += left
            location -= left
        else:
            answer += right
            location += right
    return answer


print(solution("EUNAGI"))