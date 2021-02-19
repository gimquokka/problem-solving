n, m = map(int, input().split())

a = list(map(int, input().split()))

cont = 0
for i in range(n):
	for j in range(i+1, n):
		if a[i] != a[j]:
			cont += 1

print(cont)
			