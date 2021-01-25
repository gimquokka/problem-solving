import sys
input = sys.stdin.readline

n = int(input())

array = list(map(int, input().split()))

array.sort()

result = 0
count = 0

for i in array:
    count += 1
    if i <= count:
        result += 1
        count = 0


print(result)