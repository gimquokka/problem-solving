def first_binary_search(array, target, start, end):

    while True:
        if start > end:
            return -1
        mid = (start + end) // 2

        if array[mid] == target and (mid == 0 or array[mid-1] < target):
            return mid
        
        elif array[mid] == target or array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1



def last_binary_search(array, target, start, end):
    n = len(array)
    start, last = 0, n-1

    while True:
        if start > end:
            return -1
        
        mid = (start + end) // 2

        if array[mid] == target and (mid == n-1 or array[mid+1] > target):
            return mid
        elif array[mid] or array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

n, x = map(int, input().split())
lst = list(map(int, input().split()))

s = first_binary_search(lst, x, 0, n-1)
if s == -1:
    print(-1)
else:
    l = last_binary_search(lst, x, 0, n-1)
    print(l-s+1)