# 잘 이해가 안되니, 나중에 또 두고두고 보면서 이해 ㄱㄱ
n = int(input())

data = list(map(int, input().split()))

target = 1

for x in data:
	if target < x:
		break
	target += x

print(target)