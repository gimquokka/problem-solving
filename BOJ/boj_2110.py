import sys

input = sys.stdin.readline

n, c = map(int, input().split())

data = [0 for _ in range(n)]
for i in range(n):
    data[i] = int(input())
    
data.sort()

def check(dist):
    global data, c, n
    
    cnt = 1
    
    now = data[0]
    for i in range(1, n):
        if data[i] >= (now + dist):
            # print(data[i])
            now = data[i]
            cnt += 1
        
        if cnt >= c:
            return True
    
    return False

# print(check(3))


l = data[-1] - data[0]
s = 1

while s <= l:
    mid = int((l + s)/2)
    if check(mid):
        s = mid + 1
        ans = mid
        # print(ans)
    else:
        l = mid - 1

print(ans)
    
    
                    





