# 3 6 9 game '4' -> 1 2 X 4

a = int(input())

for i in range(1, a + 1):

    if i % 3 == 0:
        print("X", end = ' ')

    else: print(i, end = ' ')


