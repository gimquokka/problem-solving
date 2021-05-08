'''
# 내 코드
n = int(input())
a = [0]*4

if n >= 500: 
	a[0], remain = divmod(n, 500)
if remain >= 100: 
	a[1], remain = divmod(remain, 100)
if remain >= 50:
	a[2], remain = divmod(remain, 50)
if remain >= 10:
	a[3], remain = divmod(remain, 10)

print('500:', a[0], '100:', a[1], '50:', a[2], '10:', a[3])
'''

n = int(input())

count = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
	count += n//coin
	n %= coin

print(count)