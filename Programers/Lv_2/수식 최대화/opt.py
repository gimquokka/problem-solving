'''
참고
https://soniacomp.medium.com/%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%88%98%EC%8B%9D%EC%B5%9C%EB%8C%80%ED%99%94-%ED%8C%8C%EC%9D%B4%EC%8D%AC-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-e43e53ae19b6
'''


def calc(priority, n, expression):
    # priority 연산자 우선순위 모음 / n 우선순위 --> 낮은 것부터 0, 1, 2 / expression 더 낮은 우선순위에서 쪼개진 식 문자열
    if n == 2:  # 가장 높은 우선순위에 도달했을 때, 계산한다.
        return str(eval(expression))
    if priority[n] == '*':  # 먼저 쪼갠 애들부터 계산한다.
        res = eval('*'.join([calc(priority, n+1, e)
                             for e in expression.split('*')]))
    if priority[n] == '+':
        res = eval('+'.join([calc(priority, n+1, e)
                             for e in expression.split('+')]))
    if priority[n] == '-':
        res = eval('-'.join([calc(priority, n+1, e)
                             for e in expression.split('-')]))
    return str(res)


def solution(expression):
    answer = 0
    priorities = [
        ('*', '-', '+'),
        ('*', '+', '-'),
        ('+', '*', '-'),
        ('+', '-', '*'),
        ('-', '*', '+'),
        ('-', '+', '*')
    ]
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer
