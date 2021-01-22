#  N to be 1

#point 최대한 많이 나누기
#greedy 알고리즘은 최적의 해를 구하는 것이 핵심

def solution(N,K):
    count = 0
    while (N!=1):
        if N%K!=0:
            N-=1
            count+=1
        else:
            N=N/K
            count+=1
    return count

print(solution(25,5))
print(solution(17,3))

#코드 리뷰: 반복문을 적게 돌릴 고민을 해보자.


