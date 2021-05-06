import heapq


def solution(scoville, K):

    count = 0
    heapq.heapify(scoville)
    while scoville:

        min1 = heapq.heappop(scoville)
        # 모든 음식의 스코빌 지수가 K이상인 경우
        if min1 >= K:
            return count
        # 두 번째로 맵지 않은 음식이 존재하는 경우
        if scoville:
            min2 = heapq.heappop(scoville)
            # 섞은 음식의 스코빌 지수를 계산하여 queue에 넣어줌
            heapq.heappush(scoville, min1 + 2 * min2)
            count += 1
    return -1


print(solution([1, 2, 3, 9, 10, 12], 7))