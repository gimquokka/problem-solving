c = input()

# int(ord(c[0])) - int(ord['a']) + 1 
# 이렇게 하면 쉽게 1~8 사이의 값 얻을 수 있음!!
char_to_num = {'a': 1, 'b': 2,'c': 3,'d': 4,'e': 5, 'f': 6, 'g': 7, 'h': 8}

x, y = int(c[1]), char_to_num[c[0]]


# steps = [(2, 1), () ...] 
# 이런식으로 list만들어서 활용하면 더욱 단순화 할 수 있음!
one = [-1, 1]
two = [-2, 2]

cont = 0

for dy in two:
	if 1 <= y+dy <= 8:
		for dx in one:
			if 1 <= x+dx <= 8:
				cont += 1
for dx in two:
	if 1 <= x+dx <= 8:
		for dy in one:
			if 1 <= y+dy <= 8:
				cont += 1

print(cont)