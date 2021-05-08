def solution(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

    # 이렇게 작성하여도 됨
    # return s.lower().count('p') == s.lower().count('y')
