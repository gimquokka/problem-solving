n, x = map(int, input().split())
lst = list(map(int, input().split()))


def binary_search(start, end, x):
    while True:
        if start > end:
            return -1
            
        mid = (start + end) // 2
        
        
        if lst[mid] == x:
            return mid
        
        elif lst[mid] < x:
            start = mid + 1
        
        else:
            end = mid - 1


i = binary_search(0, n-1, x)
if i == -1:
    print(-1)
else:
    count = 1
    j = i + 1
    while True:
        if j > n-1 or lst[j] != x:
            break
        count += 1
        j += 1
    
    j = i - 1
    while True:
        if j < 0 or lst[j] != x:
            break
        count += 1
        j -= 1
    
print(count)

        
