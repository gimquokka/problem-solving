# print input before get 0
array = input().split()

for i in array:
	i = int(i)
	
	if i == 0:
		break

	print(i)

		