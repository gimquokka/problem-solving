# 실수한 부분
문제를 잘못 이해함, 3번 강의의 선수 강의로 1번과 2번강의가 있을 때 1, 2번 강의를 동시에 들을 수 없다는 가정 하에 문제에 접근함.. 
1, 2번 강의 사이에 순서가 없다면 동시에 들을 수 있음. 각각 30, 20분 걸린다고 하면 1, 2번 강의를 동시에 수강하게 되면 최소 30분이 걸림

# 풀이
topological order 순서대로 최소시간 구해주면 됨, 한 강의에 대한 선수 강의가 여러개 있을 경우에는 계산된 선수 강의 최소 시간 + 현재 강의 시간 값중 최댓값이 최소 시간이 되도록 설정  
input 4 3 1 -1 about course 2 : course 2의 indegree 값은 선수 강의 수(2개), edge 정보는 각 선수 강의들로부터 뻗어져 나오는 edge로 고려해주어야 함 ex) course 3 -> course 2, course 1 -> course 2
indegree 정보는 각 강의에 대한 선수 강의들의 수, 그래프 edge 정보는 선수 강의들 vertex

# 몰랐던 python 기능
'''python  
import copy
lst2 = copy.deepcopy(lst1) # lst2 = lst1[:] 과 동일한 표현 
'''
