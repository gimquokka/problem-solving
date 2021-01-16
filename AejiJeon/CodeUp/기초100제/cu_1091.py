# An+1 = (m)*An + d  -> An=?

a, m, d, n = map(int, input().split())


for i in range(2, n + 1):
    a = m*a + d

print(a)
