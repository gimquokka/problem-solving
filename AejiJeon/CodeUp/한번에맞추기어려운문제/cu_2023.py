# numbers of column is A,B,..,Z,AA,AB,...,AZ,BA,... print the nth column number

q = int(input())

r = 0
l = []

while True:
    r = q % 26
    q //= 26
    if r == 0:
        q -= 1
        r = 26
    l.append(chr(ord('A') - 1 + r))
    if q == 0: break

l.reverse()
print("".join(l))

