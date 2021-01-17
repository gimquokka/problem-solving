import sys
num=[ ]
#이차원 배열 입력 받기
for i in range(10):
    a= list(map(int,input().split()))
    num.append(a)

#개미 이동
a,b =1,1
while 1:
    if num[1][1]==2:
        num[1][1]=9
        break
    elif num[a][b+1] ==0 :
        num[a][b]=9
        b+=1
    elif num[a][b+1] ==1 and num[a+1][b]==0:
        num[a][b]=9
        a+=1
    elif num[a][b+1] ==2:
        num[a][b]=9
        num[a][b+1] = 9
        break
    elif num[a+1][b] == 2:
        num[a][b]=9
        num[a+1][b] = 9
        break
    elif num[a][b + 1] == 1 and num[a + 1][b] == 1:
        num[a][b]=9
        break

for i in range(10):
    for j in range(10):
        print(num[i][j],end=' ')
    print('')

