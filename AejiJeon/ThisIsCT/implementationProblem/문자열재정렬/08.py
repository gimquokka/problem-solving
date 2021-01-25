lst = input()    # 'K1KA5CB7'

alphabets = []
numbers_sum = 0

for elem in lst:
    if elem >= 'A' and elem <= 'Z':
        alphabets.append(elem) 
    
    else:
        numbers_sum += int(elem)

alphabets.sort()
for i in alphabets:
    print(i, end='')
print(numbers_sum)
