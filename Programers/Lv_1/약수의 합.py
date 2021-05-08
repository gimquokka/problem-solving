def solution(n):
    answer = n
    # n//2 + 1까지만 봐도 됨. 1/2을 넘으면 약수가 본인 말고 존재하지 않음으로
    for i in range(1, n//2+1):
        if n % i == 0:
            answer += i
    return answer
