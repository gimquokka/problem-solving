def recursion(i):
	if i == 10: return
	recursion(i+1)
	print(i, '번째 재귀함수 호출 됨')

recursion(1)
	