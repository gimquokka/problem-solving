def balance_string(p):
    
    r, l = 0, 0
    
    for c in p:
        
        if c == "(":
            r += 1
        else:
            l += 1
            
        if r == l:
            u, v = p[:(r+l)], p[(r+l):]
            break
        
    return (u, v)


def check_right(p):
    
    cnt = 0
    
    for c in p:
        
        if c == "(":
            cnt += 1
        else:
            cnt -= 1
            
        if cnt < 0:
            return False
        
    return (cnt == 0)
        
        
def remove_and_swap(p):
    ret = ""
    p = p[1:-1]
    for c in p:
        if c == "(":
            ret += ")" 
        else:
            ret += "("
    return ret
    
def solution(p):
    
    if len(p) == 0:
        return p
    
    u, v = balance_string(p)
    
    if check_right(u):
        return u+solution(v)
    else:
        s = "("
        s += solution(v) + ")"
        s += remove_and_swap(u)
        
    return s
        
        
print(solution("()))((()"))
    
    
    
    
    
