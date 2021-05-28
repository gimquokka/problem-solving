def solution(n,a,b):
    cnt = 0
    while a != b:
        cnt += 1
        a, b = (a+1)//2, (b+1)//2
    return cnt
        
print(solution(8, 4, 7))