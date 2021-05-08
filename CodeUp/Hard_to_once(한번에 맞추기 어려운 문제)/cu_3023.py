str_a = input()
str_b = input()

n_a = len(str_a)
n_b = len(str_b)

# Pythonic way to allocate str to int list
a = [int(i) for i in str_a]
b = [int(i) for i in str_b]

axb = [0]*(n_a + n_b + 2)

# 1칸씩 밀어서 더하고, 10씩 나눠서 옆으로 넘기기
for i in range(n_b):
	for j in range(i,(n_a + i)):
		axb[j] += a*(b[i])
print(axb)