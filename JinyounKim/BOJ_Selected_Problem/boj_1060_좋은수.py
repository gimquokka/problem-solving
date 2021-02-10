import heapq
INF = int(1e16)

l = int(input())

lucky = list(map(int, input().split()))
lucky.sort()

n = int(input())

m_set = set()
q = []
for i in lucky:
    heapq.heappush(q, (0, i))
    m_set.add(i)

# Case 1. x is under min(lucky)
min_lucky = min(lucky)
for m in range(1, 101):
    if m >= min_lucky or (m in m_set):
        break
    p = (m-0)*(min_lucky-m)-1
    heapq.heappush(q, (p, m))
    m_set.add(m)

# Case 2. x is between lucky_set
# Fist case => min(lucky) - 100
for gap in range(-1, -101, -1):
    m = lucky[0] + gap
    if m < 101 or (m in m_set):
        break
    p = (m-0)*(lucky[0] - m)-1
    heapq.heappush(q, (p, m))
    m_set.add(m)

for gap in range(1, 101):
    m = lucky[0] + gap
    if l > 1:
        if (m >= lucky[1]) or (m in m_set):
            break
        p = gap*(lucky[1]-m)-1
        heapq.heappush(q, (p, m))
        m_set.add(m)
    else:
        if m in m_set:
            break
        heapq.heappush(q, (INF, m))
        m_set.add(m)


for i in range(1, l-1):
    pre = lucky[i-1]
    s = lucky[i]
    e = lucky[i+1]
    for gap in range(-1,-101, -1):
        m = s+gap
        if (m <= pre) or (m in m_set):
            break
        p = (m - pre)*(s-m)-1
        heapq.heappush(q, (p, m))
        m_set.add(m)
    for gap in range(1, 101):
        m = s+gap
        if m >= e or (m in m_set):
            break
        p = (m - s)*(e-m)-1
        heapq.heappush(q, (p, m))
        m_set.add(m)

if l > 1:
    # Case 3. x is max(luck)- 100
    for gap in range(-1, -101, -1):
        m = lucky[l-1]+gap
        if m <= lucky[l-2] or (m in m_set):
            break
        p = (m-lucky[l-2])*(lucky[l-1]-m)-1
        heapq.heappush(q, (p, m))
        m_set.add(m)

    for gap in range(1, 101):
        m = lucky[l-1]+gap
        if (m in m_set):
            break
        heapq.heappush(q, (INF, m))
        m_set.add(m)

ans = []
for i in range(n):
    ans.append(heapq.heappop(q)[1])

print(*ans, sep = ' ')

