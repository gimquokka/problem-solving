# time array ([hour, minute, second]) second초 더해줌
def add_second(time, second):
    new_time = time[:]
    new_time[2] = round(new_time[2] + (second - 0.001), 3)

    if new_time[2] >= 60:
        new_time[2] -= 60
        new_time[1] += 1
        if new_time[1] >= 60:
            new_time[1] -= 60
            new_time[0] += 1

    return new_time


# time array ([hour, minute, second]) second초 빼줌
def sub_second(time, second):

    new_time = time[:]
    # 0초인 경우에는 그대로 return시켜줌
    if second != 0:
        new_time[2] = round(new_time[2] - (second - 0.001), 3)
        if new_time[2] < 0:
            new_time[2] += 60
            new_time[1] -= 1
            if new_time[1] < 0:
                new_time[1] += 60
                new_time[0] -= 1

    return new_time


def solution(lines):
    for i in range(len(lines)):
        date, time, second = lines[i].split()
        time = time.split(":")
        # lines 배열은 ([hour, minute, second], 처리시간) tuple로 이루어짐
        lines[i] = ([int(time[0]), int(time[1]), float(time[2])], float(second[:-1]))

    # 종료시간을 기준으로 오름차순 정렬
    lines.sort(key=lambda x: (x[0][0], x[0][1], x[0][2]))

    result = 0
    for i in range(len(lines)):

        # 현재 로그의 응답 완료 시간부터
        now_start = lines[i][0]
        # 현재 로그의 음답 완료 시간 + 1초까지
        now_end = add_second(now_start, 1)
        count = 1
        # 종료시간이 i 번째 로그의 종료시간보다 큰 로그들을 전부 탐색
        for j in range(i + 1, len(lines)):
            # 로그의 시작 시간이 i 번째 로그의 종료시간보다 작은 경우
            # 즉, i 번째 로그의 종료시간 ~ 종료시간 + 1초 구간에 포함되는 경우

            # now_end, sub_second 둘다 계산 시 소수점 다 표현했음 -> 정확히 비교 가능
            if now_end >= sub_second(lines[j][0], lines[j][1]):
                count += 1

        result = max(result, count)

    return result


print(solution(["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]))
