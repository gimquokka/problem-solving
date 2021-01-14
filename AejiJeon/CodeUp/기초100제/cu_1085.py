# input h b c s -> print MB unit of needed space for saving

h, b, c, s = input().split()

h = int(h)
b = int(b)
c = int(c)
s = int(s)

bit = h*b*c*s / pow(2, 23)

print("%.1f MB" %bit)
