# two 1 or 0 -> true if both of them are false
a, b = input().split()

bool = not int(a) and not int(b)

print("%d" %bool)
