def solution(s):
    s = s[1:-1]
    elements = s.split("},{")
    elements[0] = elements[0][1:]
    elements[-1] = elements[-1][:-1]
    
    elements.sort(key = lambda x : len(x))
    
    elements = [list(map(int, e.split(","))) for e in elements]
    
    answer = []
    for arr in elements:
        for e in arr:
            if e not in answer:
                answer.append(e)
                
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))