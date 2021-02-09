# 시간초과..
import sys
import copy

input = sys.stdin.readline

n, p, k = map(int, input().split())

# graph -> adjacent matrix structure
graph = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(p):
    a, b, cost = map(int, input().split())
    graph[a][b] = cost
    graph[b][a] = cost

# 1 ~ n 연결된 vertices를 담는 array에서
# edge cost값이 큰 순서대로 k개를 제외한 나머지 edges 중
# cost의 최댓값을 return
def getMaxCost(arr):
    length = len(arr)
    # 공짜로 연결하는 경우
    if length <= k:
        return 0
    # 연결된 순서대로 인터넷 선 가격을 담아줌(edge cost)
    new_arr = [graph[arr[i]][arr[i + 1]] for i in range(length - 1)]
    # 선 가격 순서대로 오름차순 정렬
    new_arr.sort()
    # 비싼 선들 k개를 제외한 남은 선들 중에서 최댓값 return
    return max(new_arr[: length - 1 - k])


def dfs(arr, now):
    global result

    # dfs 호출 단계에 대해 연결된 vertices를 담는 array
    arr = copy.deepcopy(arr)
    arr.append(now)
    # n번 컴퓨터까지 연결된 경우
    if now == n:

        # 결괏값 update
        result = min(result, getMaxCost(arr))
        return

    for i in range(1, n + 1):
        # dfs 호출 단계에서 다음으로 연결할 vertex 선택
        if graph[now][i] != 0 and i not in arr:
            dfs(arr, i)
    return


INF = int(1e9)
result = INF
dfs([], 1)
if result != INF:
    print(result)
else:
    print(-1)
