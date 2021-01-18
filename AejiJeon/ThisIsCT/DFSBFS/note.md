# 개념 짚고 넘어가기  
- 컴퓨터 내부에서 recur ftn 동작 원리는 스택 자료구조와 동일 
- 반복적인 구현보다 재귀적 구현이 훨씬 simple!
- adj matrix : 두 노드가 연결되어 있는지에 대한 정보를 얻을 때 효율적 
- adj list : 특정 노드와 연결된 모든 인접 노드를 순회해야 할 때 효율적  
- DFS(재귀함수 이용)보다는 BFS(큐 자료구조 이용) 구현이 조금 더 빠르게 동작 nut 코드가 훨씬 김
- 1차원, 2차원 배열을 그래프 형태로 생각하면 수월하게 문제풀 수 있음
- 2차월 배열의 탐색 문제 -> 그래프 형태로 바꿔서 생각해보기!

# 몰랐던 python 기능  

print(lst) list 최하단 원소부터 출력
print(lst[::-1]) list 최상단 원소부터 출력
reversed(str or lst) reverse(only lst) reversed object 반환, 변수 자체는 변하지 않음
(only lst).reverse() lst 변수 자체가 reverse됨
[10: 5: -1] index 10부터 (5+1)까지 뒤집어서 반환 then, (str or lst)[::-1] 뒤집힌 결과를 반환

'''python
from collections import deque
queue = deque() #collections 모듈에서 제공하는 deque 자료구조, queue 라이브러리 이용하는 것보다 더 간단
for i in [5,3,7,1,4]:
    queue.append()
queue.popleft() #popright()는 존재하지 않음
print(queue) # deque([3,7,1,4]) list가 아닌 queue object 반환, lst = list(...) 사용해서 변경 가능
queue.reverse() 
print(queue) # deque([4,1,7,3]) 반환
'''

- global 사용 유무
'''python
def change_v(visited):
    visited[0] = True # parameter 변수의 부분을 변경하는 경우에는(index를 사용하여) 
                      # 결과가 함수 종료 후에도 적용됨 -> global 정의할 필요 x

visited = [False]*3
print(visited)
change_v(visited)
print(visited)  # visited = [True, False, False] printed

def turn_left(direction):
    direction = 1       # 함수 내에서 direction이라는 local variable이 새로 defined
                         # parameter 변수 자체 값을 변경할 시 변경 결과가 적용되지 않음
                         # -> 함수를 parameter없이 정의한 후 변경하고자 하는 벼수를 함수 내에서
                         # global로 정의

direction = 0 
turn_left(direction)  
print(direction)  # direction = 0 printed
'''

list(map(int, "0010")) = [0, 0, 1, 0]


