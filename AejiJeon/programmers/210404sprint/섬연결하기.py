# x 노드의 parent return
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# a, b가 속해있는 집합을 union
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


def solution(n, costs):
    parent = [i for i in range(n)]
    # 크루스칼 알고리즘 수행을 위해 모든 간선들을 cost에 대해서 오름차순으로 정렬
    edges = sorted(costs, key=lambda x: x[2])

    result = 0
    for a, b, cost in edges:
        # a, b node가 각각 속해있는 집합이 서로소인 경우
        if find_parent(parent, a) != find_parent(parent, b):
            # MST의 subgraph에 해당 edge 추가(집합을 합쳐줌)
            union_parent(parent, a, b)
            # cost를 더해줌
            result += cost
    return result


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
