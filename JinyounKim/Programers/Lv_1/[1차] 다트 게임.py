def get_exp(string):
    exp_dict = {"S": 1, "D": 2, "T": 3}
    exp = []
    for c in string:
        if c in {"S", "D", "T"}:
            exp.append(exp_dict[c])
    return exp


def get_num(string):
    num = []
    tmp = ''
    for c in string:
        if c.isdigit():
            tmp += c
        else:
            if tmp != '':
                num.append(int(tmp))
                tmp = ''
    return num


def get_opt(string):
    option = [0]*3
    cnt = -1
    for c in string:
        if c in {"S", "D", "T"}:
            cnt += 1
        elif c in {"*", "#"}:
            if c == "*":
                option[cnt] = 1
            else:
                option[cnt] = 2
    return option


'''
dartResult = "1S234S*10T"
print(get_num(dartResult))
print(get_exp(dartResult))
print(get_opt(dartResult))
'''


def solution(dartResult):
    num = get_num(dartResult)
    exp = get_exp(dartResult)
    opt = get_opt(dartResult)
    ans = []
    index = -1
    for n, e, o in zip(num, exp, opt):
        index += 1
        # exp 반영
        ans.append(n**e)
        if o == 0:
            continue
        # "*"의 경우 처리
        elif o == 1:
            ans[index] *= 2
            # 첫번째 원소의 경우 처리
            if index > 0:
                ans[index-1] *= 2
        # "#"의 경우 처리
        else:
            ans[index] = -ans[index]
    return sum(ans)


dartResult = "1D2S#10S"
print(solution(dartResult))
