n = int(input())
lst = list(map(int, input().split()))

start, end = 0, n-1
result = -1
while True:
    if start > end:
        break
    mid = (start + end) // 2

    if mid == lst[mid]:
        result = mid
        break
    elif mid > lst[mid]:
        start = mid + 1

    else:
        end = mid - 1

print(result)
    