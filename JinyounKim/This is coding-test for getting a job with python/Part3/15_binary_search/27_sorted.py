from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
a = list(map(int, input().split()))

def find_num_of_x(a, x):
	s = bisect_left(a, x)
	e = bisect_right(a, x)

	num_of_element = e - s
	
	if num_of_element == 0:
		return -1
	else:
		return num_of_element

print(find_num_of_x(a, x))
	
