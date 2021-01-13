# Get size of audio file that h(Hz), b(bit), c(channel), s(time)
h, b, c, s = map(int, input().split())


print("%.1f"%((h*b*c*s)/(8*(2**20))), 'MB')