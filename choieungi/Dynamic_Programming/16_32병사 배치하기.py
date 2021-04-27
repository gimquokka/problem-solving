n= int(input())
soilder = list(map(int,input().split()))
soilder.reverse()

d=[1]*(n+1)
#문자 1개 당 길이가 1이므로 다음과 같이 초기화함

for i in range(1,n):
    for j in range(i):
        if soilder[j]<soilder[i]:
            d[i] = max(d[i],d[j]+1)

print(n-max(d))



