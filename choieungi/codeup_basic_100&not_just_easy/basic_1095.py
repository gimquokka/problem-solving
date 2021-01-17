import sys
k= int(input())
num=[ ]
a = sys.stdin.readline().split()

for i in a:
    num.append(int(i))

b=num[0]

for i in num:
    if b>i :
        b= i

print(b)

