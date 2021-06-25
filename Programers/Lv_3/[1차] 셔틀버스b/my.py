from collections import deque

# 셔틀 버스 시간 어레이(분 단위 ex) 09:00 => 540)


def nt_to_arr(n, t):
    deptart_times = []
    for i in range(n):
        deptart_times.append(540+i*t)
    return deptart_times
# print(nt_to_arr(1, 10))

# 문자열 시간 => 분단위 시간 변환


def timetable_to_arr(timetable):
    arrive_times = []

    for stamp in timetable:
        hh, mm = stamp.split(":")
        arrive_times.append(60*int(hh) + int(mm))

    return arrive_times
# print(timetable_to_arr(["08:00", "08:01", "08:02", "08:03"]))

# 분단위 시간 => 문자열 시간 변환


def mtime_to_hhmm(minute):
    hh, mm = divmod(minute, 60)

    hh = str(hh) if hh >= 10 else "0"+str(hh)
    mm = str(mm) if mm >= 10 else "0"+str(mm)

    return hh+":"+mm
# print(mtime_to_hhmm(601))


def solution(n, t, m, timetable):
    departs = sorted(nt_to_arr(n, t))
    arrives = sorted(timetable_to_arr(timetable))

    q = deque(arrives)

    for idx, time in enumerate(departs):
        cnt0 = 0
        cnt = 0
        if idx == len(departs)-1:
            for stamp in q:
                if stamp <= time:
                    cnt0 += 1
            if cnt0 < m:
                return mtime_to_hhmm(time)

        while q:
            now = q.popleft()
            if now <= time:
                cnt += 1
                if cnt == m:
                    if idx == len(departs)-1:
                        cnt == m-1
                        return mtime_to_hhmm(now-1)
                    break
            else:
                q.appendleft(now)
                break


timetable = ["08:00", "08:01", "08:02", "08:03"]
print(solution(1, 1, 5, timetable))
timetable = ["09:10", "09:09", "08:00"]
print(solution(2, 10, 2, timetable))

timetable = ["09:00", "09:00", "09:00", "09:00"]
print(solution(2, 1, 2, timetable))

timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(solution(1, 1, 5, timetable))

timetable = ["23:59"]
print(solution(1, 1, 1, timetable))

timetable =["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(solution(10, 60, 45, timetable))
