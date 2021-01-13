# sum of even numbers among 1 ~ n

n = int(input())
n = n//2

sum = 0
for i in range(1, n+1):
    sum += 2*i

print(sum)
