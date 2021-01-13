# Get the image file's size with width(w), h(height), b(bit)
w, h, b = map(int, input().split())

print('%.2f'%((w*h*b)/((2**20)*(8))), 'MB')

