def solution(n, stages):
    l = len(stages)

    result = []

    for i in range(1, n+1):

        count = stages.count(i)
        if l == 0:
            fail = 0
        else:
            fail = count / l

        result.append((i,fail))
        l -= count
    
    result.sort(key=lambda x: -x[1])
    result = [i[0] for i in result]

    
    return result

n1 = 5
n2 = 4
stages1 = [2,1,2,6,2,4,3,3]
stages2 = [4,4,4,4,4]

print(solution(n2, stages2))