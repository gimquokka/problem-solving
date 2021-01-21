# 개념 짚고 넘어가기
- 문제에서 서로 다른 객체가 연결되어 있다는 내용 -> 그래프 알고리즘 떠올리기
- Min Heap : 항상 부모 노드가 자식 노드보다 크기가 작은 트리 자료구조
- Disjoint Sets Algorithm : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조(union과 find 연산으로 조작, 트리 자료구조를 이용)
 루트를 찾기 위해서는 재귀적으로 부모를 거슬러 올라가야 함(-> 경로 압축 기법 사용), undirected graph 내에서의 사이클 반별시 사용, MST kruskal algorithn에서 각 edge들에 대해서 서로소 집합들 합칠 때 사용
- kruskal algorithm 내부에서 사용되는 disjoint sets algorithm의 시간 복잡도는 sorting algorithm 시간 복잡도보다 작으므로 무시 -> O(ElogE)
- Topology Sort : O(V+E)


