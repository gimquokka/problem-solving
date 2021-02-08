def solution(N, stages):
    answer = []
    
    stages_user = [0]*(N+2)
    fail_rate_arr = []
    
    for i in stages:
        stages_user[i] += 1
    
    for i in range(1, N+1):
        user_num = sum(stages_user[i:])
        fail_rate = stages_user[i]/user_num
        fail_rate_arr.append((fail_rate, i))        
    
    fail_rate_arr.sort(key = lambda x: (-x[0], x[1]))
    
    for _, stage in fail_rate_arr:
        answer.append(stage)
    
    
    return answer