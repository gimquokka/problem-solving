# 개념 짚고 넘어가기
위상 정렬에서 3가지 케이스 존재  
- 위상 정렬의 결과가 오직 1개 -> only 1 possible order
- 위상 정렬의 결과가 2개 이상인 경우
- 사이클이 발생(no tolological order)


# 실수한 부분
graph = [[]]*n -> 똑같은 list([])가 n번 복사(shallow copy)  
graph = [[] for _ in range(n)]