# input a r n of geometric sequence -> an = ?

a, r, n = map(int, input().split())

an = a*(r**(n-1))

print(an)