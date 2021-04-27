# ai = min(ai,ai-k +1)

n,m = map(int, input().split())

money = [ ]
for i in range(n):
    temp = int(input())
    money.append(temp)

d= [10001] * (m+1) #m<10000

d[0] = 0

for i in range(n): #차례 대로 넣기
    k= money[i]
    for j in range(k, m+1):
        if d[j-k] != 10001: #(m<10000)
            d[j] = min(d[j],d[j-k]+1)

print(d[m])

