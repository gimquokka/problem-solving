# Print possible combination of (0 ~ a-1, 0 ~ b-1, 0 ~ c-1) and find a num of it
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

for i in range(a):
	for j in range(b):
		for k in range(c):
			print(i, j, k)

print(a*b*c)