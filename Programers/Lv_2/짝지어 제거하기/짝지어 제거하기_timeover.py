'''
시간초과 풀이
'''

def solution(s):
    _len = len(s)
    if _len % 2 != 0:
        return 0

    s = list(s)
    for i in range(_len//2):
        for idx in range(len(s)-1):
            if s[idx] == s[idx+1]:
                repeat = idx
                del s[idx:idx+2]
                break

    return 1 if len(s) == 0 else 0
