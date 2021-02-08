import operator

n = int(input())

data = list(map(int, input().split()))

data.sort()

''' My code is very intuitive one.

s = int(1e9)
result = 0
for i in data:
	tmp = list(map(operator.add, data, [-i]*n))
	tmp = sum(list(map(abs, tmp)))
	if tmp < s:
		s = tmp
		result = i

print(result)
'''
# My think it is wrong. We should compare n-1//2, (n-1//2)+1
print(data[(n-1)//2])

