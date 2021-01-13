# print the smallest number among 3 integers with ternary operator

a, b, c = input().split()

num1 = int(a)
num2 = int(b)
num3 = int(c)

print((num2 if num3 > num2 else num3) if num1 > num2 else (num1 if num3 > num1 else num3))