# print larger number with ternary operator

a, b = input().split()

num1 = int(a)
num2 = int(b)

print(num1 if num1 > num2 else num2)