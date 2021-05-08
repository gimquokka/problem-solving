def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[v]:
            dfs(graph, i, visited)
