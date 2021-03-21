def solution(d, budget):
    cnt = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break
        cnt += 1
    return cnt
