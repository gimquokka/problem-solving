# Find a minimum value using ternery operation
a, b, c = input().split()

a = int(a)
b = int(b)

a1 = (a if a>b else b)
a2 = (a1 if a1 > c else c)

print(a2)
