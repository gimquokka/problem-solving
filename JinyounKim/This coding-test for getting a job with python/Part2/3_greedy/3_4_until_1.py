n, k = map(int, input().split())

cont = 0
while(n!=1):
	if n%k == 0: n /= k
	else: n -= 1
	cont += 1
print(cont)