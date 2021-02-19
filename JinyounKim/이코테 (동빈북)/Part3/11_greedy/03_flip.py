a = list(map(int, input()))

n = len(a)

cont = 0

for i in range(1, n):
	if a[i] == a[i-1]:
		continue
	else: cont += 1

print((cont+1)//2)


