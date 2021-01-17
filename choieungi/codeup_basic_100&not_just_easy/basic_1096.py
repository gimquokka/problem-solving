import sys
k= int(input())
num=[ ]

for i in range(19):
    line=[]
    for j in range(19):
        line.append(0)
    num.append(line)

for i in range(k):
    a,b = map(int,sys.stdin.readline().split())
    if num[a-1][b-1]!=1:
        num[a - 1][b - 1] += 1

for i in range(19):
    for j in range(19):
        print(num[i][j],end=' ')
    print('')

