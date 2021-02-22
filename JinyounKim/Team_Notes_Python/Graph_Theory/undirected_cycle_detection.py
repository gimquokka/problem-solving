"""
union_find를 이용하여 undirected graph에서 cycle dection.
(방향 그래프에서의 사이클 탐지 DFS로 가능함)

설명
- 간선을 추가할 때 find_parent가 같으면 cycle이 있는것!
"""
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

# 노드와 간선의 개수 입력 받기
v, e = map(int, input().split())
# 부모 테이블, 자기 자신으로 초기화
parent = [i for i in range(v+1)]

cycle = False  # 사이클 발생 여부
for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print('사이클이 발생하였습니다.')
else:
    print('사이클이 발생하지 않았습니다.')
