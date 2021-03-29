data = input()

left = sum(int(i) for i in data[:(len(data)//2)])
right = sum(int(i) for i in data[(len(data)//2):])

print('LUCKY' if left == right else 'READY')
