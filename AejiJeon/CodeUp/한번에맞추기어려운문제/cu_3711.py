# about a, b  both have same number of digit like 233~780

a, b, k = input().split()
k = int(k)

def sdig(f, t):
    nums = 0
    l = len(f)

'''    if a1 == b1 == 1:
        if int(f) <= k and int(t) >= k:
            return 1
        else:
            return 0
'''

    if f == t:

        for i in range(l):
            if t[i] == str(k): nums += 1
        return nums


    for i in range(l):
        x = int(f[l - 1])
        y = int(t[l - 1])
        if x < k: g = f[:l - 1] + '0'*i
        elif x == k:
            if i == 0: g = f[:l - 1]
            else: g = f[:l - 1] + f[l:]
        else:
            if l == 1: g = ''
            else: g = str(int(f[:l - 1]) + 1) + '0'*i

        if y > k: h = t[:l - 1] + '9'*i
        elif y == k:
            if i == 0: h = t[:l - 1]
            else: h = t[:l - 1] + t[l:]
        else:
            if l == 1: h = ''
            else: h = str(int(f[:l - 1]) - 1) + '9'*i
        l -= 1
        if g != '' and h != '':
            nums += int(h) - int(g) + 1

    return nums

a1 = len(a)
b1 = len(b)
s = b1 - a1
result = 0
if s != 0:
    for i in range(s + 1):
        if i == 0: result += sdig(a, str(10**a1 - 1))
        elif i == s: result += sdig(str(10**(b1 - 1)), b)
        else: result += sdig(str(10**(a1 + i - 1)), str(10**(a1 + i) - 1))

else: result = sdig(a, b)

print(result)
