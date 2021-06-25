def solution(n, results):
    INF = int(1e9)
    answer = 0
    graph = [[INF]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        graph[i][i] = 0

    for i, j in results:
        graph[i][j] = 1

    for k in range(1, n+1):
        for a in range(1, n+1):
            for b in range(1, n+1):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

    for a in range(1, n + 1):
        count = 0
        for b in range(1, n + 1):
            if graph[a][b] != INF or graph[b][a] != INF:
                count += 1
        if count == n:
            answer += 1
    # for row in graph:
    #     print(row)
    return answer


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
