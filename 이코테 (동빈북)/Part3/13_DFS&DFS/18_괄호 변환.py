# 최소 "균형잡힌 괄호 문자열" 인덱스 반환
def balanced_index(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i


# "균형잡힌 괄호 문자열"인 p가 '옳은 괄호 문자열'인지 판단
def check_right(p):
    cnt = 0
    for i in p:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True


def solution(p):
    # 1. 빈 문자열인 경우 그대로 반환
    if p == '':
        return p
    # 2. 문자열 w를 '균형잡힌 괄호 문자열' u, v로 분리
    i = balanced_index(p)
    u, v = p[:i+1], p[i+1:]
    # 3. 문자열 u가 '올바른 괄호 문자열'이라면 v에 대하여 다시 수행
    if check_right(u):
        return u + solution(v)
    # 4. 문자열 u가 """"이 아니라면 아래의 과정을 수행
    # 4-1
    answer = '('
    # 4-2
    answer += solution(v)
    # 4-3
    answer += ')'
    # 4-4
    u = list(u[1:-1])
    for j in range(len(u)):
        if u[j] == '(':
            u[j] = ')'
        else:
            u[j] = '('
    answer += ''.join(u)
    # 4-5
    return answer
