import sys
k= int(input())
num=[ ]
a = sys.stdin.readline().split()

for i in a:
    num.append(i)

num.reverse()
for i in num:
    print(i, end=' ')
