n = input()
num = [0]*len(n)
for i in range(len(n)):
    num[i] = n[i]

left_sum = 0
right_sum = 0
for i in range(0, len(num)//2):
    left_sum += int(n[i])

for i in range(len(num)//2, len(num)):
    right_sum += int(n[i])

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')

