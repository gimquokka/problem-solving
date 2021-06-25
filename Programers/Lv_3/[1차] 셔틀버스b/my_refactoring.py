# 셔틀 버스 시간 어레이(분 단위 ex) 09:00 => 540)
def nt_to_arr(n, t):
    deptart_times = []
    for i in range(n):
        deptart_times.append(540+i*t)
    return deptart_times

# 문자열 시간 => 분단위 시간 변환
def timetable_to_arr(timetable):
    arrive_times = []

    for stamp in timetable:
        hh, mm = stamp.split(":")
        arrive_times.append(60*int(hh) + int(mm))

    return sorted(arrive_times)

# 분단위 시간 => 문자열 시간 변환
def mtime_to_hhmm(minute):
    hh, mm = divmod(minute, 60)

    hh = str(hh) if hh >= 10 else "0"+str(hh)
    mm = str(mm) if mm >= 10 else "0"+str(mm)

    return hh+":"+mm

import heapq

def solution(n, t, m, timetable):
    departs = nt_to_arr(n, t)
    arrives = timetable_to_arr(timetable)

    for dept_time in departs:
        if dept_time == departs[-1]:
            cnt = 0
            for arrive_time in arrives:
                if arrive_time > dept_time:
                    break
                cnt += 1
            if cnt < m:
                return mtime_to_hhmm(dept_time) 
        
        cnt = 0
        while arrives: 
            if arrives[0] > dept_time:
                break
        
            now = arrives.pop(0)
            cnt += 1
            if dept_time == departs[-1] and cnt == m:
                return mtime_to_hhmm(now-1)
            
            if m == cnt:
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
