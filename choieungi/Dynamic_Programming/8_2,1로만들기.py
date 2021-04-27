x = int(input())

d = [0] * 1000001 #dp 테이블

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
        #1뺀거 vs 나누기 중 더 작은 값 (d[i]인 이유는 앞에서 이미 1을 더해 호출 횟수를 셈
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    elif i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])

