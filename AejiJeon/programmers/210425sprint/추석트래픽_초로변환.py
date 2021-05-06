def solution(lines):
    result = 0
    # get input
    S, E = [], []
    i = 0
    for line in lines:

        type(line)
        (d, s, t) = line.split(" ")

        # 다 쪼갬
        t = float(t[0:-1])
        (hh, mm, ss) = s.split(":")
        seconds = float(hh) * 3600 + float(mm) * 60 + float(ss)
        # 로그 종료 시간을 index와 함께 담아줌
        E.append((seconds, i))
        # 로그 시작 시간을 담아줌
        S.append(seconds - t + 0.001)

        i += 1
    # 종료시간을 기준으로 오름차순 정렬
    E.sort()
    for i in range(len(E)):
        now_end_time, idx = E[i]
        count = 1
        # 종료시간이 i 번째 로그의 종료시간보다 큰 로그들을 전부 탐색
        for j in range(i + 1, len(E)):
            # 현재 로그의 응답 완료 시간부터
            # 현재 로그의 응답 완료 시간 + 1초 사이에 포함된 경우
            # 현재 로그의 응답 완료 시간 >= 확인하고 있는 로그의 응답 시작 시잔
            if round(now_end_time + 1 - 0.001, 3) >= round(S[E[j][1]], 3):
                count += 1
        result = max(result, count)

    return result


print(
    solution(
        [
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s",
        ]
    )
)
