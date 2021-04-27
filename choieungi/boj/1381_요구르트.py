n,k = map(int,input().split())
yogurt = [ ]

for _ in range(n):
    p,q = map(int,input().split())
    yogurt.append((p,q/100))

yogurt.sort(key=lambda x: (-x[0] ,x[1]))

result = 1
for i in range(k):
    temp = 1- yogurt[i][1]
    result *= temp

result = 1 - result

if float("%.3f" %result) < 0.001:
    print("GG")
else:
    result *= 100
    print("%.03f" %result)


