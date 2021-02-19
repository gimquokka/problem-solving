n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

first, second = arr[0], arr[1]

ans = 0

# 내가 교제보다 잘짜는 듯...?
limit = k
for i in range(1, m+1):
	limit -= 1
	if limit != 0:
		ans += first
	else:
		ans += second
		limit = k

print(ans)
