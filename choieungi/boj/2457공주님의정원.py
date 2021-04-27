'''
1. 월별 처리, 지는 날 전까지 꽃이 피어 있다.
2. 3월 1일에서 11월 30일까지 매일 꽃이 한 가지 이상 피어 있다. 310 < x <1130
3. 꽃의 수의 최소한으로 한다


'''
n= int(input())
flowers = [0] * n

for i in range(n):
    sm, sd, lm, ld = map(int,input().split())
    flowers[i] = (sm*100+sd,lm*100+ld)


flowers.sort(key=lambda x:(-x[1]))

temp = 301
cnt = 0

if temp <=1130:
    for _ in range(n):
        if temp > 1130:
            print(cnt)
            break

        for i in range(n):
            if flowers[i][0] <= temp:
                temp = max(temp,flowers[i][1])
        cnt += 1

    if cnt==n and temp<=1130:
        print(0)