def factorial_arr(n):
	arr = [1]*(n+1)
	for i in range(1, n+1):
		arr[i] = arr[i-1]*i
	return arr

def factorial_recursion(n):
	if n == 1:
		return 1
	return (factorial_recursion(n-1)*n)

# print(factorial_arr(10))
print(factorial_recursion(10))