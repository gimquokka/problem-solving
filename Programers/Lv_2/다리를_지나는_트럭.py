from collections import deque


def solution(bridge_length, weight, truck_weights):
    ans = 0
    sum = 0
    q = deque()
    for w in truck_weights:
        while True:
            if (len(q) == bridge_length):
                sum -= q.popleft()
            elif (w + sum <= weight):
                sum += w
                q.append(w)
                ans += 1
                break
            else:
                q.append(0)
                ans += 1
    return ans + bridge_length
