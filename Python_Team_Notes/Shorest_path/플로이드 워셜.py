"""
Time complexity: O(n^3)

ex)
<Input>
4, 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

<Output>
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
"""
import sys
input = sys.stdin.readline
INF = int(1e9)

#  노드 및 간선 개수 입력 받기
n, m = map(int, input().split())

# 2차원 리스트(그래프 표현)을 만들고, 모든 값 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에게로의 비용 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# Floyd Warshall(dp)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

print(graph)
