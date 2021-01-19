a, b = map(int, input().split())

sum_arr = [0]*(b+1)
result = 0

for i in range(b+1):
	m, n = divmod(i, 10)
	sum_arr[i] = sum_arr[m]
	if (n!=0)&(n%3==0):
		sum_arr[i] += 1
	i += 1

for i in range(a, b+1):
	result += sum_arr[i]


print(result)

	