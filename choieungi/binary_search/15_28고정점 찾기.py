n = int(input())
element = list(map(int, input().split()))

def binary_search(array, start, end):
    while start<=end:
        mid = (start+end)//2
        if array[mid] == mid :
            return mid
        elif array[mid] > mid:
            end = mid-1
        else:
            start = mid+1
    return -1
print(binary_search(element,0,n-1))

# 7
#-15 -4 2 8 10 14 19
# 복붙할 때 오류?