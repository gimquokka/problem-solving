#boj 2792
import math
import sys
n,m = map(int,input().split())
jewel = []
for _ in range(m):
    jewel.append(int(sys.stdin.readline()))



def binary_search(array,start,end):
    global n
    answer = 0

    while start<=end:
        envy = 0
        mid = start+(end-start)//2 #start+end가 10^9 초과 할 수 있으니
        for i in array:
            envy += math.ceil(i/mid)
        if envy <=n:
            answer = mid
            end = mid - 1
        else:
            start = mid+1
    return int(answer)


print(binary_search(jewel,1,max(max(jewel),n)))