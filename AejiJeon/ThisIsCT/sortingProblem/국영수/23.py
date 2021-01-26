import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(input().split())

lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:int(x[3]), reverse = True)
lst.sort(key=lambda x:int(x[2]))
lst.sort(key=lambda x:int(x[1]), reverse = True) # 숫자 string가지고 비교할 수 x '3'>'100' and '1'<'3'임

for i in range(n):
    print(lst[i][0])