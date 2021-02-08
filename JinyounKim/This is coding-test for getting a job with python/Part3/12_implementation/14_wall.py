'''
n =12
weak = [1, 5, 6, 10]
gap = [3, 4, 1, 4]
=> [0, 0, 0, 3]
dist = [1, 2, 3, 4]
'''

'''
n = 12
weak = [1, 3, 4, 9, 10]
gap = [3, 2, 1, 5, 1]
n-2개부터 탐색
dist = [3, 5, 7]
'''
from bisect import bisect_left

def remove_gap(gap, start, end):
    if start == 0:
        del gap[-1]
    if end == len(gap):
        del gap[0]
    for i in range(start, end):
        del gap[i]
    return gap

def find_gap(n, weak):
    length = len(weak)
    gap = [0]*length

    gap[0] = (n - weak[-1]) + weak[0]
    for i in range(1, length):
        gap[i] = weak[i] - weak[i-1]
    return gap

def solution(n, weak, dist):
    gap = find_gap(n, weak)
    length = len(weak)
    
    min_val = 200
    for num in range(length-2, 0, -1):
        for i in range(length-num-1):
            now = sum(gap[i:i+num+1])
            if min_val > now:
                min_val = now
                min_i = i
        if bisect_left(dist, min_val) == len(dist):
            return -1
        else:
            gap = remove_gap(gap, min_i, min_i+num)


    
    return answer

    