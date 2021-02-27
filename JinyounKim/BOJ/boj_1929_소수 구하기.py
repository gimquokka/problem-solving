s, e = map(int, input().split())

ans = []

is_prime = [True]*(e+1)
is_prime[0], is_prime[1] = 0, 0
for i in range(2, e+1):
    j = 2
    while i*j <= e and i <= int(e**0.5)+1:
        is_prime[i*j] = False
        j += 1
    if s <= i and is_prime[i]:
        ans.append(i)

for i in ans:
    print(i)
    


