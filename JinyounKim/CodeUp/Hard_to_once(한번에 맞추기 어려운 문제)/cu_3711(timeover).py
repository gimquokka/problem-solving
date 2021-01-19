a, b, c = map(int, input().split())

arr = [0]*(b+1)
result = 0

for i in range(b+1):
	n, m = divmod(i, 10)
	if n != 0:
		arr[i] = arr[n]
	if (c == 0)&(m==0):
		arr[i] += 1
	elif (c != 0)&(m==c):
		arr[i] += 1
	if a <= i:
		result += arr[i]

print(result)
