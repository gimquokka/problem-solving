# Standard
def solution(s):
    idx = 0
    ans = ''
    for i in s:
        if i.isalpha():
            idx += 1
            ans += i.upper() if idx % 2 == 1 else i.lower()
        else:
            idx = 0
            ans += ' '
    return ans

# Optimal


def solution(s):
    return ' '.join([''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(w)]) for w in s.split(' ')])
