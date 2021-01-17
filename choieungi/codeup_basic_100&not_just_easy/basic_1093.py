import sys
k= int(input())
num=[ ]
a = sys.stdin.readline().split()

for i in range(23):
    num.append(0)

for i in a:
    c=int(i)
    num[c-1]=num[c-1]+1

for i in num:
    print(i, end=' ')

