n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
	if b[i] > a[i]:
		a[i] = b[i]
	else: break # 이것 추가해주면 훨씬 코드가 빨라질 듯!

print(sum(a))