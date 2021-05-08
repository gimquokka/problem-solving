"""
###Strategy###
1. Case를 잘 나누어 탐색을 진행
2. 좋은 구간의 개수가 (m-s)(e-m)-1임으로 이는 위로 볼록한 2차 함수꼴임 (이것이 이해 안된다면, 문제의 예시를 귀납적으로 계산해보며 이해해야함)
즉, m은 s, e 주변에서 최솟값을 가진다.
1. 2.
=> (0) S에 속하는 원소들 (좋은 구간 0개) (1) 1 ~ 100, (2) S의 원소 -+100 범위만 탐색하면 최소 좋은 구간 100개의 경우를 보장할 수 있음

(s: m보다 작은 S의 원소 중 가장 m에 가까운 수
 e: m보다 큰 S의 원소 중 가장 m에 가까운 수
 m: 현재 좋은 구간의 개수를 구하고자 하는 원소
 s < m < e)

### Time Complexity ###
200*L >>> O(1) (bcz L <= 50)

### Tip ###
1. l 집합 앞에 0 넣어줌으로서 앞부분 edge case를 따로 처리하지 않을수도 있을 듯함
2. 개인적으로 그냥 앞뒤는 따로 처리해주는 것이 같편한 것 같아서 그렇게 처리함

"""
import heapq
INF = int(1e16)

# Get Inputs
l = int(input())

lucky = list(map(int, input().split()))
lucky.sort()

n = int(input())

# m_set exists for check i in q just in case
m_set = set()
q = []
# Case 0. x is in S (num fo case is zero)
# Add S into priority queue and m_set
for i in lucky:
    heapq.heappush(q, (0, i))
    m_set.add(i)

# Case 1. x is 1 ~ 100 or under min(lucky)
min_lucky = min(lucky)
for m in range(1, 101):
    if m >= min_lucky or (m in m_set):
        break
    p = (m-0)*(min_lucky-m)-1
    heapq.heappush(q, (p, m))
    m_set.add(m)

# Case 2. x is between lucky_set's element
# 2 - 1. x = min(lucky) - (1 ~ 100)
for gap in range(-1, -101, -1):
    m = lucky[0] + gap
    # condition: m < 101 is for avoiding case.1
    if m < 101 or (m in m_set):
        break
    p = (m-0)*(lucky[0] - m)-1  # = (m-s)(e-m)-1
    heapq.heappush(q, (p, m))
    m_set.add(m)
# 2 - 2. x = min(lucky) + (1 ~ 100)
for gap in range(1, 101):
    m = lucky[0] + gap
    if l > 1:
        if m >= lucky[1] or (m in m_set):
            break
        p = (m - lucky[0])*(lucky[1]-m)-1  # = (m-s)(e-m)-1
        heapq.heappush(q, (p, m))
        m_set.add(m)
    else:  # If l == 1 then after that is INF cases
        if m in m_set:
            break
        heapq.heappush(q, (INF, m))
        m_set.add(m)

# 2 - 3. x = lucky set -+ (1 ~ 100) (except lucky[0] that is 2 - 1, 2)
for i in range(1, l-1):
    pre = lucky[i-1]
    s = lucky[i]
    e = lucky[i+1]
    # 2 - 3 - 1. x = lucky set - (1 ~ 100)
    for gap in range(-1, -101, -1):
        m = s+gap
        if (m <= pre) or (m in m_set):
            break
        p = (m - pre)*(s - m)-1
        heapq.heappush(q, (p, m))
        m_set.add(m)
    # 2 - 3 - 2. x = lucky set + (1 ~ 100)
    for gap in range(1, 101):
        m = s+gap
        if (m >= e) or (m in m_set):
            break
        p = (m - s)*(e-m)-1
        heapq.heappush(q, (p, m))
        m_set.add(m)
# Case 3. around max(lucky_set)
# bcz, If l == 1. then it is overlap with 2 - 1, 2. 사실 m in m_set이 있기 때문에 꼭 필요한 조건은 아님
if l > 1:
    # 3 - 1. x is max(lucky_set) - (1 ~ 100)
    for gap in range(-1, -101, -1):
        m = lucky[l-1]+gap
        if m <= lucky[l-2] or (m in m_set):
            break
        p = (m-lucky[l-2])*(lucky[l-1]-m)-1
        heapq.heappush(q, (p, m))
        m_set.add(m)
    # 3 - 2. x is max(lucky_set) + (1 ~ 100)
    for gap in range(1, 101):
        m = lucky[l-1]+gap
        if m in m_set:
            break
        heapq.heappush(q, (INF, m))
        m_set.add(m)

# Print out answer
ans = []
for i in range(n):
    ans.append(heapq.heappop(q)[1])

print(*ans, sep=' ')
