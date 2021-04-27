n = int(input())

d= [0] * 1001

d[1] = 1 #2*1
d[2] = 3 #3가지 종류 타일 조합
for i in range(2,n+1):
    d[i] = (d[i-1] + (d[i-2]*2))

print(d[n])


