n = int(input())

# 1, 2, 3, 5만 소인수로 가지는 수 = 못생긴 수
# "못생긴 수" 수열 초기화
ugly = [0]*n
# 시작은 1부터
ugly[0] = 1

# 2, 3, 5의 배수를 순차적으로 증대시키기 위한 index를 선언
i2 = i3 = i5 = 0
# 다음 2, 3, 5를 받기 위한 변수 초기환
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    # 다음 2, 3, 5의 배수 후보들 중 가장 작은 수 선언
    ugly[i] = min(next2, next3, next5)
    # if 구분 3번 걸어서 배수가 겹치는 경우(ex. 6) 다음 수로 진행 시킴
    if ugly[i] == next2:
        i2 += 1
        next2 = ugly[i2]*2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3]*3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5]*5

# 정답 출력
print(ugly[n-1])
