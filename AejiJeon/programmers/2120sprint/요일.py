def solution(a, b):
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    dic = {0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6:"SAT"}
    days = 0
    for i in range(1, a):
        days += day[i-1]
    days += b
    # 금요일부터 시작하므로 5를 더해줌
    return dic[(5 + days - 1) % 7]
    # 훨씬 파이써닉함
    # return days[(5+sum(months[:a-1])-1)%7]
print(solution(12, 31))