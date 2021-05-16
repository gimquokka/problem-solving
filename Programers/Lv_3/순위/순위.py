def solution(n, results):
    ans = 0
    INF = int(1e9)

    # 2차원 리스트(그래프 표현)을 만들고, 모든 값 무한으로 초기화
    graph = [[INF]*(n+1) for _ in range(n+1)]

    # 자기 자신에게로의 비용 0으로 초기화
    for i in range(1, n+1):
        graph[i][i] = 0

    # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for a, b in results:
        graph[a][b] = 1
        # graph[b][a] = 1

    # Floyd Warshall(dp)
    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    for a in range(1, n+1):
        cnt = 0
        for b in range(1, n+1):
            if graph[a][b] != INF or graph[b][a] != INF:
                cnt += 1
            if cnt == n:
                ans += 1
                
    # for row in graph:
    #     print(*row)

    return ans


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
