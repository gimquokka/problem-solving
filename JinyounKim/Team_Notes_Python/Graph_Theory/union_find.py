"""
Time complexity
노드의 개수: v, union 연산: v-1, find 연산: M
O(V+M(1+log_(2-m/v)(v)))

"""

# 특정 원소가 속한 집합을 찾기


def find_parent(parent, x):
    # 루트 노드가 아니면, 루트 노드를 찾을 때까지 재귀적으로 호출 => 경로 압축 방식
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


# 노드, 간선의 개수 입력 받기
n, m = map(int, input().split())

# 부모 테이블 초기화
parent = [i for i in range(n+1)]
# union연산을 모든 간선에 대하여 수행
for _ in range(m):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합을 출력
# (parent 테이블을 그대로 쓰는게 아니라 find_parent로 호출해줘야 적확한 값이 나옴)
for i in range(1, n+1):
    print(find_parent(parent, i), end=' ')
print()

# 방향 그래프에서의 사이클 탐지 DFS로 가능함
