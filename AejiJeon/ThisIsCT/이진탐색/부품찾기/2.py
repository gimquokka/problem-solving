import sys

n = int(input())
n_lst = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
m_lst = list(map(int, sys.stdin.readline().rstrip().split()))

n_lst.sort()


def bineary_search(array, target, start, end):
    if start > end:
        return "no"
    
    mid = (start + end) // 2

    if array[mid] == target:
        return "yes"

    elif array[mid] > target:
        return bineary_search(array, target, start, mid-1)
    
    else:
        return bineary_search(array, target, mid+1, end)
    

for i in m_lst:
    print(bineary_search(n_lst, i, 0, n-1), end = " ")
