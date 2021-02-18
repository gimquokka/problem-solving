def solution(numbers):
    answer = []
    count = [0]*201
    n = len(numbers)
    for i in range(n-1):
        for j in range(i+1, n):
            count[numbers[i] + numbers[j]] += 1
    for i in range(201):
        if count[i] > 0:
            answer.append(i)
            
            
    return answer
