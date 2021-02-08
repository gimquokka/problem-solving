n = int(input())
a = list(map(int, input().split()))

e = len(a)-1
s = 0
m = (e+s)//2

result = -1
while s <= e:
	if a[m] == m:
		result = m
		break
	if a[m] > m:
		e = m-1
	else:
		s = m+1

	m = (s+e)//2
print(result)



