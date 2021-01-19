# print multiplication table with hexa
a = input()

s = 0
for i in range(15):
	s += 1
	result = int(a, 16)*s
	print(a+'*{0:X}={1:X}'.format(s, result))
	
