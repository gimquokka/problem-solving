# print 1 ~ n without 3n
n = int(input())

print(1, end='')
for i in range(2, n+1):
	if i%3 == 0:
		continue
	print('', i, end='')