def check_balanced(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
    if count == 0:
        return True
    else: 
        return False


def check_right(s):
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else: 
        return False 

def div_string(s):
    u = ''
    for c in s:
        u += c
        if check_balanced(u):
            
            v = s[len(u):]
            
            break
    return u, v

def flip(s):
    ns = ''
    for c in s:
        if c == '(':
            ns += ')'
        else:
            ns += '('
    return ns


def solution(w):
    if w == '':
        return ''

    u, v = div_string(w)
    
    if check_right(u):
        return  u + solution(v)
    
    else:
        u = u[1:-1]
        return '('+solution(v) + ')' + flip(u)

s1 = "(()())()"
s2 = ")("
s3 = "()))((()" 
print(solution(s1))
print(solution(s2))
print(solution(s3))












