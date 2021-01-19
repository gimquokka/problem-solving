# print multipliziton table with 3n => X
n = int(input())

print(1, end = '')
for i in range(2, n+1):
	if i%3==0:
		print(' X', end = '')
	else:
		print('',i, end = '')
	