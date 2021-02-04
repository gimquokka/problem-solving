import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

# 현재까지 측정할 수 있는 무게 중 최댓값
last = 0

for w in lst:
    # last + 1 값을 측정할 수 없는 경우
    if last + 2 <= w:
        break
    # last + 1, ..., last + w 값들 측정 가능
    else:
        last += w
print(last + 1)