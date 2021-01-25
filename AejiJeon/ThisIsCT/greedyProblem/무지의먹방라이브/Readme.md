# 실수한 부분
solution 함수를 구현하는 문제인데 함수 구현 없이 코드 안에서 input값 설정 후 코드를 짬.., 코드 짜면서 annotation 다는 연습하기!

# 궁금한 부분
heap.heappush(q, ...) -> heapq.heappop(q) 전에 q[0][0] 사용할 수 있나..? q[0][0]=min값을 가지고 나머지(q[1~][0])는 정렬 되어있지 x? 

# 몰랐던 python 기능
tuple이나 list들로 구성하는 list를 (list구성하는 element의)특정 index에 따라 sort하는 방법: key = lambda x: x[index] 이용
example)  
'''python
result = sorted(q, key=lambda x:x[1])
'''