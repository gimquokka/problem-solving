from itertools import permutations

def calc(priority, n, expression):
    
    if n == 2:
        return str(eval(expression))
    
    if priority[n] == "*":
        res = eval("*".join([calc(priority, n+1, e) for e in expression.split("*")]))
    if priority[n] == "+":
        res = eval("+".join([calc(priority, n+1, e) for e in expression.split("+")]))
    if priority[n] == "-":
        res = eval("-".join([calc(priority, n+1, e) for e in expression.split("-")]))
        
    return str(res)

def solution(expression):
    priorities = permutations(["*", "+","-"])
    return max(abs(int(calc(priority, 0, expression))) for priority in priorities)


print(solution("100-200*300-500+20"), 60420)
print(solution("50*6-3*2"), 300)