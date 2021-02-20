def solution(answers):
    length = len(answers)
    first = [1, 2, 3, 4, 5]*(length//5+1)
    second = [2, 1, 2, 3, 2, 4, 2, 5]*(length//8+1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(length//10+1)
    
    f_count, s_count, t_count = 0, 0, 0
    i = -1
    for ans in answers:
        i += 1
        if first[i] == ans:
            f_count += 1
        if second[i] == ans:
            s_count += 1
        if third[i] == ans:
            t_count += 1
    
    tmp = []
    tmp.append((f_count, 1))
    tmp.append((s_count, 2))
    tmp.append((t_count, 3))
    tmp.sort(key = lambda x: (-x[0], x[1]))
    
    answer = []
    answer.append(tmp[0][1])
    for i in range(2):
        if tmp[i][0] == tmp[i+1][0]:
            answer.append(tmp[i+1][1])
        else: break
    
    return answer