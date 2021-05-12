from collections import deque

def solution(s):
    if len(s) % 2 != 0:
        return 0

    stack = deque()
    s = deque(list(s))
    
    while s:
        stack.append(s.popleft())
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()  

    return 1 if not stack else 0

# print(solution("baabaa"))