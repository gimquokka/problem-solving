import sys
n = int(input())
dic = dict()

for line in range(n):
    num = int(sys.stdin.readline())
    if num not in dic: dic[num] = 1
    else: dic[num] += 1

mx1 = max(dic.values())
mx2 = 0

for i in dic:
    if mx2 < dic[i] < mx1: mx2 = dic[i]

s1 = set()
s2 = set()

for i in dic:
    if dic[i] == mx1: s1.add(i)
    if dic[i] == mx2: s2.add(i)

if len(s1) > 1: print(abs(max(s1) - min(s1)))
else:
    v1 = abs(max(s1) - min(s2))
    v2 = abs(max(s2) - min(s1))
    print(max(v1, v2))