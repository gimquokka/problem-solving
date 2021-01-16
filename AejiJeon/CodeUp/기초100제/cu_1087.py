# 1+2+3+... until the sum is larger than or equal to the input

a = int(input())

sum = 0
i = 1
while(True):
    if sum >= a: break
    sum += i
    i += 1
print(sum)
