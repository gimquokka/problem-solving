# Check plus or minus and even or odd
array = input().split()

for element in array:
	element = int(element)
	
	if element < 0:
		print('minus')
	else:
		print('plus')

	# Check odd/even
	if element%2 == 0:
		print('even')
	else:
		print('odd')