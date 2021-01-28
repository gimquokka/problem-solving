from bisect import bisect_left, bisect_right



n, x = map(int, input().split())
array = list(map(int, input().split()))
print(array)
print(bisect_right(array, x), bisect_left(array, x))
count = bisect_right(array, x) - bisect_left(array, x)
print(count)
if count == 0:
    print(-1)

else:
    print(count)