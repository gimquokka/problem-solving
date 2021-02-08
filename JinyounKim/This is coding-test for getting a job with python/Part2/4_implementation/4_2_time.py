n = int(input())

h, m, s = 0, 0, 0
t = 1
cont = 0
while(h != (n+1)):
	h, m = divmod(t, 3600)
	m, s = divmod(m, 60)
	
	cases = str(h) + str(m) + str(s)

	cont += 1 if ('3' in cases) else 0

	t += 1

print(cont)