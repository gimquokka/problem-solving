import sys
num=[ ]

for i in range(19):
    line=[]
    a= sys.stdin.readline().split()
    for j in a:
        line.append(int(j))
    num.append(line)

k= int(input())

for i in range(k):
    a,b = map(int,sys.stdin.readline().split())
    for i in range(19):
        if num[a-1][i] ==0:
            num[a-1][i]=1
        elif num[a-1][i]==1:
            num[a-1][i]=0

    for i in range(19):
        if num[i][b-1] ==0:
            num[i][b-1]=1
        elif num[i][b-1]==1:
            num[i][b-1]=0

#결과 출력
for i in range(19):
    for j in range(19):
        print(num[i][j],end=' ')
    print('')

