# 풀이
- N개의 집들에 대해 가중치가 적은 N-1개의 길을 통해 집을 연결해 주는데 마지막에 연결되는 길을 포함하지 않게되면 N-2개의 길이 만들어 질 것이고 자동으로 두개 set으로 나누어질 것이다.(greedy 개념으로 생각하면 합당)
* 참고
- partition property : About a partition of the vertices of G into subsets U and V, there is a MST of G containing the edge that is an edge of minimum weight across the partition(문제와 연관x)

# 효율적인 풀이
MST를 이루는 weight들 중 최댓값 찾기 위해서 weight 값들을 따로 모아서 계산하지 않고 변수 하나를 추가하여 MST에 weight가 추가할 때마다 update 시켜준 후 마지막에 cost 합에서 빼주기(list.pop(), sum(list) 굳이 사용하지 않고)