import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# weight = [0]*n
# cost = [0]*n
meat = [0]*n
weight_sum = 0
cost_sum = 0
for i in range(n):
    w, c = map(int, input().split())
    meat[i] = [w, c]
meat.sort()

s = 0
e = n

ans = -1
while s <= e:
    mid = (s+e)//2 
    # print(sum(weight[:i]))
    # print(mid)
    if sum(weight for weight, _ in meat[:mid]) >= m:
        if mid == n:
            ans = meat[n-1][1]
            break
        while meat[mid-1][0] != meat[mid][0]:
            mid += 1 
        ans = min(sum(cost for _, cost in meat[:mid]), meat[mid+1][1])
        e = mid-1
    else:
        s = mid+1

print(ans)
    

