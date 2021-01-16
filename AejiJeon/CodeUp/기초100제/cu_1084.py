# possble 3 dim tuples (r, g, b) and the number

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

count = 0

for i in range(0, a):
    for j in range(0, b):
        for k in range(0, c):
            print(i, j, k)
            count += 1

print(count)
