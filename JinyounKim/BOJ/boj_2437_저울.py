'''
1 1 2 3 6 7 30

1 2 4 7 13

ans = 1

1, 2, 3, 4,

# Case True
1 ~ a1+
a2 <= a1 + a2 + 1
ans = 1 ~ (a1 + a2)
1 ~ (a1 + a2)

# Case False
a2 > a1 + 1
ans = 1 ~ a1
This case we can not make a1 + 1
a1 < a1+1 < a2

1 => 1+1 => 3
'''

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

data.sort()

# Start 1 is key point
answer = 1
for i in data:
    # >
    if i > answer:
        break
    answer += i
print(answer)