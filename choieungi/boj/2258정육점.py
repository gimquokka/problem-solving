import sys
n,m= map(int,input().split())
meat =[0]*(n)

for i in range(n):
    a,b =map(int,input().split())
    meat[i] =(a,b)

meat.sort(key=lambda x:(x[1],-x[0]))

ans = sys.maxsize
exist =False
amount =0
sum =0

for i in range(n):
    amount += meat[i][0]
    if i>0 and meat[i][1] == meat[i-1][1]:
        sum += meat[i][1]
    else:
        sum =0

    if amount >= m:
        ans = min(ans, meat[i][1] + sum)
        exist = True

print(ans if exist else -1)

#내가 놓친 부분: 같은 가격인 것들이 여러개 있을 때, 그 다음으로 큰 가격이 후보일거라 생각했는데 알고보니 그 개수만큼 고기를 사야했다.
# 가격의 최솟값을 계속 갱신해줘야한다.






