import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    hq = []
    for idx, elem in enumerate(food_times):
        heapq.heappush(hq, (elem, idx))

    l = len(hq)
    prev = 0
    while l*(hq[0][0]-prev) < k:
        now = heapq.heappop(hq)[0]
        val = now - prev
        k -= val*l
        prev = now
        l -= 1
        
    hq.sort(key= lambda x: x[1])
    
    return hq[k%l][1]+1

print(solution([3, 1, 2], 4))