from datetime import datetime, timedelta


# take time = count number?

def count_num(start, times):
    cnt = 0
    d = timedelta(milliseconds=999)
    for j in times:
        if j[0] <= start + d and j[0] >= start:
            cnt += 1
        elif j[1] >= start and j[1] <= start + d:
            cnt += 1
        elif j[0] >= start and start + d >= j[1]:
            cnt += 1
        elif j[0] <= start and j[1] >= start + d:
            cnt += 1
    return cnt


def solution(lines):
    times = []
    for i in lines:
        temp = i.split()
        t = temp[2][:-1]  # remove 's'
        if len(t) == 1:
            take_time = timedelta(seconds=(int(t))) - timedelta(milliseconds=1)  # +999
        else:
            a = t.split(".")
            take_time = timedelta(seconds=int(a[0]), milliseconds=int(a[1])) - timedelta(milliseconds=1)
        end_time = datetime.strptime(temp[0] + temp[1], '%Y-%m-%d%H:%M:%S.%f')
        times.append((end_time - take_time, end_time))  # (start_time, end_time)

    # times.sort(key = lambda x: x[0]) input이 이미 정렬됨.
    answer = 0
    for i in times:
        start = i[0]
        answer = max(count_num(start, times), answer)
        start = i[1]
        answer = max(count_num(start, times), answer)

    return answer