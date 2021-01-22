# def binary_search(arr, target, start, end):
# 	mid = (start+end)//2

# 	if target == arr[mid]:
# 		# print('check')
# 		return mid
# 	elif target > arr[mid]:
# 		return binary_search(arr, target, mid+1, end)
# 	else:
# 		return binary_search(arr, target, start, mid-1)

import math

def binary_search(arr, target, start, end):
	for _ in range(int(math.log(len(arr), 2) + 1)):
		mid = (start + end)//2
		if target == arr[mid]:
			return arr[mid]
		elif target > arr[mid]:
			start = mid+1
		else: end = mid-1
	return None


	

	

print(binary_search([0, 1, 2, 3, 4], 0, 0, 4))

