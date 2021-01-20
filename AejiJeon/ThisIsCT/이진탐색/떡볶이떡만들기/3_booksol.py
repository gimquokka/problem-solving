import sys
n, m = map(int, input().split())

array = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(array)  # 가능한 절단기 높이는 0 ~ max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1

    else:
        result = mid  # 적어도 m만큼 
        start = mid + 1

print(result)