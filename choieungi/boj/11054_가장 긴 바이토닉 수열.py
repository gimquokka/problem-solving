#boj_11054
n = int(input())

sequence = list(map(int, input().split()))

d1 = [1] *(n+1) #부분 증가 수열

#최장 부분 증가/감소 수열
for i in range(1,n):
    for j in range(i):
        if sequence[j]<sequence[i]:
            d1[i] = max(d1[j]+1,d1[i])

#최장 증가 수열일 때, 최장 부분 증가 테이블에 감소할 때도 갱신
#최장 감소 수열이 더 길다면, max값이므로 최장 감소 수열이 출력될 것이다.

for i in range(1, n):
    for j in range(i):
        if sequence[j]>sequence[i]:
            d1[i] = max(d1[j]+1,d1[i])

print(max(d1))
