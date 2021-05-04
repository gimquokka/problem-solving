import heapq


def solution(scoville, K):
    ans = 0
    _len = len(scoville)
    heapq.heapify(scoville)

    if scoville[0] >= K:
        return ans

    for i in range(_len-1):
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + 2*b)

        ans += 1

        if scoville[0] >= K:
            return ans

    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 1, 100], 7))
