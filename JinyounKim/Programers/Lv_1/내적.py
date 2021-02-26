# Mine
def solution(a, b):
    ans = 0
    for i in range(len(a)):
        ans += a[i]*b[i] 
    return ans

# Opt
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
