n = input()

x = ord(n[0]) - ord('a') + 1

y = int(n[1])

count = 0

for i in range(2): # 수평 2칸 수직 1칸 if i is 0, 수평 1칸 수직 2칸 if i is 1

    for two in [-2, 2]:
        for one in [-1, 1]:

            _x = x + (two if i == 0 else one)
            _y = y + (one if i == 0 else two)

            if _x < 1 or _y < 1 or _x > 8 or _y > 8:
                continue
            count += 1

print(count)
