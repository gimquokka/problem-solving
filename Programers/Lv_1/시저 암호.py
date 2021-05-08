def push(char, n):
    if ord('a') <= ord(char) <= ord('z'):
        if ord('z') < ord(char) + n:
            return chr(ord(char)+n-26)
        else:
            return chr(ord(char)+n)
    elif ord('A') <= ord(char) <= ord('Z'):
        if ord('Z') < ord(char) + n:
            return chr(ord(char)+n-26)
        else:
            return chr(ord(char)+n)
    else:
        return char

def solution(s, n):
    answer = []
    for i in s:
        answer.append(push(i, n))
    return ''.join(answer)

'''
# Optimum solution
def solution(s, n):
    answer = []
    for i in s:
        if i.islower():
            answer.append(chr((ord(i)+n - ord('a'))%26 + ord('a')))
        elif i.isupper():
            answer.append(chr((ord(i)+n- ord('A'))%26 + ord('A')))
        else:
            answer.append(i)
    return ''.join(answer)


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
'''
