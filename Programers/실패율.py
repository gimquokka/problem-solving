# 실패율
# 1, 1, 2
from collections import Counter

def solution(N, stages):
    d = Counter(stages)
    
    cnt_arr = [0 for _ in range(N+2)]
    
    for k, v in d.items():
        cnt_arr[k] = v
    
    l = len(stages)
    result = []
    prev_sum = 0
    for i in range(1, N+1):
        result.append((cnt_arr[i]/(l-prev_sum) if (l-prev_sum) else 0, i))
        prev_sum += cnt_arr[i]
    
    result.sort(key = lambda x: (-x[0], x[1]))
    
    ans = [s for _, s in result]
    
    return ans
    

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])