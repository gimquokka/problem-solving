# Get sum of even num until input
n = int(input())
n = int(n/2)+1

s = 0
for i in range(1, n):
	s += 2*i

print(s)