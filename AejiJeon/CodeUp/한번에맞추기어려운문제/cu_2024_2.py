# dictionary 삽입 순서 적용 x

def exp4(s1):
    ssss = ''
    i = 0
    _l = len(s1)
    for _ in range(_l):
        ssss += exp1(s1[i], _l)
        i += 1
        _l -= 1
    return ssss

def exp1(c, _l):
    s = digit[int(c)]
    if c != '0':
        if _l == 4: return s + '천'
        elif _l == 3: return s + '백'
        elif _l == 2: return s + '십'
        else: return s
    else: return ''

digit = {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구', 0: ''}

n = input()

l = len(n)

dic = {}

q = l // 4
d = l % 4
dic[q] = n[0:d]

for _ in range(q):
    q -= 1
    dic[q] = n[d:d + 4]
    d += 4

dd = list(dic.keys())
dd.reverse()
rslt = ''
for i in dd:
    rslt += exp4(dic[i])
    if dic[i] != '' and dic[i] != '0000':
        rslt += '억' if i == 2 else '만' if i == 1 else ''
if n != '0':
    print(rslt)
else: print('영')