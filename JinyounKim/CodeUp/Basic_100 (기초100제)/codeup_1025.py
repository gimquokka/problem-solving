text = input()

n = len(text)
for i in text:
	n -= 1
	i = int(i)
	print('['+str(i*(10**n))+']')