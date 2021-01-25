# 효율적인 풀이
그래프에서 모든 간선의 비용이 동일할 때는 BFS(faster than dijkstra) 사용하여 최단 거리 찾을 수 있음
(dijkstra에서는 heap을 사용하지만 bfs를 이용하면 방문하지 않은 노드에 대해서만 최단거리를 갱신해주면 됨)