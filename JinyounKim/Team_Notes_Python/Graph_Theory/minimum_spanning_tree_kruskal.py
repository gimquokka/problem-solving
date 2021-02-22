"""
Tree는 간선의 개수: (노드의 개수 - 1). 
Minimum Spanning Tree도 Tree임으로 그러하다.

설명
1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2. 간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    (1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함 (2) 발생 시 포함하지 않음
3. 모든 간선에 대하여 2번을 반복

Time Complexity
O(ElogE) 
# 간선을 넣고, 뽑아내는 시간 복잡도. union_find는 상대적으로 time complexit가 적음으로 생략
"""
import heapq

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [i for i in range(v+1)]

# 간선을 받을 리스트와 최종 비용 담을 변수
edges = []
result = 0

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    heapq.heappush(edges, (cost, a, b))

# 간선을 하나씩 확인하며
while edges:
    cost, a, b = heapq.heappop(edges)
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
