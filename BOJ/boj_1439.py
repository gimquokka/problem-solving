'''
111 0/0
10 1/1
010 2/1
0101 3/2
10101 4/2
0101010 6/4
'''

s = input()

cnt = [s[0]]

for i in range(1, len(s)):
    if s[i] != cnt[-1]:
        cnt.append(s[i])

ans = min(cnt.count('0'), cnt.count('1'))
print(ans)
