# 개념 짚고 넘어가기
- greedy, DP -> 최단 경로 알고리즘에 그대로 적용됨
- heap data structure : priority queue를 구현하기 위해 사용하는 자료구조 중 하나 
- Priority Queue를 이용한 Dijkstra Algorithm : 간단히 O(ElogV)

# 몰랐던 python 기능들
''' python  
import sys
input = sys.stdin.readline.rstrip() #치환하여 사용

n, m = map(int, input().split())  
'''

PriorityQueue and heapq(speed 더 빠름) libraries in python
python library에서는 기본적으로 Min Heap 구조 이용(값이 낮은 데이터가 먼저 삭제) -> dijkstra algorithm 적용시에 good!
Max Heap으로 사용하고 싶을 경우 우선순위 해당 값에 (-) 붙여서 넣은후 나중에 꺼낸 후 (+)로 되돌림
Priority Queue list로 구현 시: 한번 삭제할 시 O(n) -> 전체 연산 횟수 : O(n^2)
               heap으로 구현 시 : O(logn) -> 전체 연산 횟수 : O(nlogn)

