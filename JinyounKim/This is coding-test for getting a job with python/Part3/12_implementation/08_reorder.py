data = input()

char = []
num = []

for i in data:
	if 0 <= (ord(i)-48) <= 9:
		num.append(int(i))
	else: char.append(i)

num.sort()
char.sort()

for i in char:
	print(i, sep = '', end = '')
for i in num:
	print(i, sep = '', end = '')

