# hexadecimal multiplication

a = input()
a = int(a, 16)
for i in range(1, 16):
    print(("%x*%x=%x").upper() %(a, i, a*i))
