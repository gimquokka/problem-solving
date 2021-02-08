n, m = map(int, input().split())
a = list(map(int, input().split()))

h_min = 0
h_max = max(a)
h_ans = 0

result = 0

while h_min<=h_max:
	result = 0
	h_mid = (h_min+h_max)//2

	for i in a:
		if i > h_mid: 
			result += (i-h_mid)
	
	# 이렇게 짜는게 더 효율적!!
	if result < m:
		h_max = h_mid-1
	else:
		h_min = h_mid+1
		result = h_mid
'''
	if result == m:
		print(h_mid)
		sys.exit()
		# if h_mid > h_ans:
		# 	h_ans = h_mid
	elif result > m:
		h_min = h_mid+1
		if h_mid > h_ans:
			h_ans = h_mid
	else:
		h_max = h_mid-1
'''
	
print(h_ans)

		
		
	