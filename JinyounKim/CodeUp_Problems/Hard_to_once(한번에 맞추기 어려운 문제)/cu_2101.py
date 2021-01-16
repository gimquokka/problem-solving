a = int(input())

# a^2 + b^2 = c^2 => a*a = (c-b)(c+b)
# a < b < c < a+b

cont = 0

# let q = c - b, w = c + b
for q in range(1, a):
	w, remainder = divmod(a**2,q)
	if remainder == 0:
		c = (q+w)/2
		b = (w-q)/2
		if (c == int(c)) and (b == int(b)) and a < b :
			# print(b, c)
			cont += 1

print(cont)

