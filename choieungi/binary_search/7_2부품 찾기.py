import sys

def check(store, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if store[mid] == target:
            return 'yes'
        elif target < store[mid]:
            end =mid -1
        else:
            start = mid +1
    return 'no'

n = int(input())
#sys로 숫자 리스트 받기
store_list = list(map(int,sys.stdin.readline().split()))

m = int(input())
check_list = list(map(int,sys.stdin.readline().split()))

#가게 부품 정렬
store_list.sort()

for i in check_list:
    print(check(store_list,i,0,n-1), end=' ')
