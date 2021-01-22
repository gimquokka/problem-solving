def fibo(x):
	a =[0]*x
	a[0], a[1] = 1, 1
	for i in range(2,x):
		a[i] = a[i-1]+a[i-2]
	print(a[x-1])

fibo(3)

