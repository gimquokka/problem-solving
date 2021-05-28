'''
참고 주소
https://eda-ai-lab.tistory.com/500
'''
def solution(n,a,b):
    cnt = 0
    while a != b:
        cnt += 1
        a, b = (a+1)//2, (b+1)//2
        print(a, b, cnt)
    return cnt
        
print(solution(8, 1, 4))