# print first number that satisfies sum of natural numbers from 1 sequentially is larger than or equal to input

n = int(input())

sum = 0
i = 0
while sum < n:
    i += 1
    sum += i
print(i)



