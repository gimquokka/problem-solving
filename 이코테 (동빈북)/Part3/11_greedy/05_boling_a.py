n, m = map(int, input().split())

data = list(map(int, input().split()))

a = [0]*11

for x in data:
	a[x] += 1

result = 0
for i in range(1, 11):
	n -= a[i]
	result += a[i]*n
	# print(result)
	
# print(a)
print(result)